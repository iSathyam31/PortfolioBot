# Portfolio ChatBot

I recently developed a portfolio website to showcase my professional experience, projects, and personal information. As an extension, I decided to enhance user interaction by integrating a Portfolio ChatBot. This project leverages Streamlit and utilizes the powerful Groq inferencing engine with the Llama3 model. The ChatBot enables visitors to ask questions directly related to the content presented on my portfolio, providing a dynamic and interactive experience.

## Project Structure
```
Portfolio_ChatBot/
│
├── assets/
│   ├── image1.png
│   ├── image2.png
│   └── image3.png
│
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Environment Setup

To run the Portfolio ChatBot locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iSathyam31/PortfolioBot.git
   cd portfolio-chatbot
   ```

2. **Install dependencies**: Ensure Python and pip are installed. Then, install the required packages listed in `requirements.txt`:
```
pip install -r requirements.txt
```

3. Set up environment variables:

* Obtain a Groq API key and set it in your environment variables.
* Optionally, set up a Google API key if required for your embeddings model.

4. Run the Streamlit app:
Run the application using the following command:
```
streamlit run main.py
```

5. Interact with the Portfolio ChatBot: Open your browser and navigate to the Streamlit app running at `localhost:8501`. Input prompts related to the portfolio to interact with the ChatBot.


## License
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.

## Acknowledgements
* **Groq Inferencing Engine**: Powered by Groq's inferencing engine with the Llama3 model.
* **Streamlit**: Used for creating the interactive web application interface.
* **Google Generative AI Embeddings**: Utilized for generating embeddings of text content.
* **FAISS**: Efficient similarity search library used for document similarity.