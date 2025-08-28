from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/L-GEN_AI/RAG/.env")

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

text_splitter = SemanticChunker(
    embeddings , 
    breakpoint_threshold_type= "standard_deviation",
    breakpoint_threshold_amount=0.5,
)

sample = """
The Eiffel Tower is located in Paris and is one of the most famous landmarks in the world.
Python is a popular programming language known for its simplicity and readability.
Cristiano Ronaldo is a professional football player who has played for Manchester United and Real Madrid.
The Pacific Ocean is the largest ocean on Earth, covering more than 60 million square miles.
Machine learning is a subset of artificial intelligence that focuses on pattern recognition.
Mount Everest, located in the Himalayas, is the tallest mountain in the world.
Electric cars are becoming increasingly popular as people shift towards sustainable energy.
Naruto is a Japanese anime that follows the journey of a young ninja.
The iPhone 15 was released with new camera features and improved performance.
Yoga helps improve flexibility, strength, and mental health.
"""

docs = text_splitter.create_documents([sample])

print( len(docs))
print( docs )