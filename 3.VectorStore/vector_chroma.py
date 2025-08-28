from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/gagan/Desktop/L-GEN_AI/RAG/.env")



doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )
docs = [doc1, doc2, doc3, doc4, doc5]
 
vector_store = Chroma(
    embedding_function= GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"),
    persist_directory='my_chroma_db',
    collection_name='sample'
)

ids = vector_store.add_documents(docs)
#also generate id's of the each docs

data = vector_store.get(include=['embeddings','documents', 'metadatas'])

result = vector_store.similarity_search(
    query='who among these are a bowler?', 
    k=1
)

# result2 = vector_store.similarity_search_with_score(
#     query='who among these are a bowler', 
#     k=2
# )
#will give us the distance between the embedding vectors
# means jitna jyada km utna aacha

# result3 = vector_store.similarity_search_with_score(
#     query="",
#     filter= {"team":"Chennai Super Kings"}
# )

# updated_doc1 = Document(
#     page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
#     metadata={"team": "Royal Challengers Bangalore"}
# )

# vector_store.update_document(document_id='73a00e4e-ed23-4c5a-851c-77779c96a8c4', document=updated_doc1)

# vector_store.delete(ids=['73a00e4e-ed23-4c5a-851c-77779c96a8c4'])
# print(result)
print(data)