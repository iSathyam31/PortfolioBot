import streamlit as st
import time
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import getpass
import os
from dotenv import load_dotenv

load_dotenv()

## Load the Groq API key
groq_api_key = os.environ['GROQ_API_KEY']

## Calling the API Key
if "GOOGLE_API_KEY" not in os.environ:
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("GOOGLE_API_KEY")

if "vector" not in st.session_state:
  st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
  st.session_state.loader = WebBaseLoader("https://isathyam31.github.io/Portfolio/")
  st.session_state.docs = st.session_state.loader.load()

  st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
  st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
  st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

# Add background image from URL
st.set_page_config(page_title="Portfolio ChatBot", page_icon="", layout="wide")

# Title section
st.markdown("# Portfolio ChatBot")
st.markdown("### Ask any question related to the provided portfolio")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

prompt_template = ChatPromptTemplate.from_template(
  """
  Please answer the following questions based solely on the provided context. 
  Ensure that your responses are accurate and directly related to the information given.

  <context>
  {context}
  </context>
  Questions:
  {input}
  """
)
document_chain = create_stuff_documents_chain(llm, prompt_template)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

prompt = st.text_input("Input your prompt here")

if prompt:
  start = time.process_time()
  response = retrieval_chain.invoke({"input": prompt})
  end = time.process_time()
  response_time = end - start

  st.markdown("### Response")
  st.write(response['answer'])
  st.markdown(f"**Response time:** {response_time:.2f} seconds")

  # Document Similarity Search section (optional, uncomment if you want to display)
  # with st.expander("Document Similarity Search"):
  #   # Find the relevant chunks
  #   for i, doc in enumerate(response["context"]):
  #     st.markdown(f"**Document {i+1}:**")
  #     st.write(doc.
