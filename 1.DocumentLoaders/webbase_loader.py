from langchain_community.document_loaders import WebBaseLoader 
from bs4 import BeautifulSoup
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/L-GEN_AI/RAG/.env")

url = "https://www.wisdomlib.org/definition/arja"

url2 = "https://www.york.ac.uk/teaching/cws/wws/webpage1.html"

url_loader = WebBaseLoader(url) 

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate (
    template= "summarize this following \n {text}", 
    input_variables= ['text']
)

docs = list(url_loader.load())


chain = prompt | model | parser 

result = chain.invoke ({'text':docs[0].page_content})

print( result )