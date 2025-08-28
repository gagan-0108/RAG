from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/L-GEN_AI/RAG/.env")

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

loader = TextLoader( 'random_text.txt', encoding='utf-8')

docs = loader.load()

prompt= PromptTemplate(
    template="Write a summary of the following poem - \n {poem}",
    input_variables=['poem']
)
parser= StrOutputParser()

chain = prompt | model | parser 

result = chain.invoke({'poem': docs[0].page_content})

print(result)