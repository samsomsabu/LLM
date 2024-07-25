import os
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
#we load our api key from the .env file we have created 
# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Story Generator"),
    ("user", "Question:{question}")
])

# Initialize Streamlit UI
st.title("Story telling bot")
input_text = st.text_input("Give the the type of story(Genre ) youb want ")

# Configure the Groq LLM
groq_api = ChatGroq(model="gemma-7b-It", temperature=0)#here we give the temperaty=ure we i.e how much humane the answer should be
output_parser = StrOutputParser()
chain = prompt | groq_api | output_parser

# Process user input
if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)
