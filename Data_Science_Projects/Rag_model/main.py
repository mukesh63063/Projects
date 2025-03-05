import streamlit as st
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import VectorDBQA

# Load documentssr
loader = TextLoader(r"C:\Users\Mukesh Prajapati\turtleproject\Rag_model\Student_data.txt")
documents = loader.load()
google_api_key = "AIzaSyDQajyVWsTlh3_alMJag3RmOvT047utVbk"

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Set up embeddings and vector store
embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001', google_api_key=google_api_key, task_type='retrieval_query')
vectordb = Chroma.from_documents(documents=texts, embedding=embeddings)

# Set up the chat model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)
qa = VectorDBQA.from_chain_type(llm=chat_model, vectorstore=vectordb)

# Streamlit UI
st.title("Text Prediction App")
user_query = st.text_input("Ask a question:")

if st.button("Submit"):
    if user_query:
        response = qa.invoke(user_query)
        st.write("Answer:", response)
    else:
        st.write("Please enter a question.")
