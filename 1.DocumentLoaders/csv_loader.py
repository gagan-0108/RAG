from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="/Users/gagan/Desktop/L-GEN_AI/RAG/1.DocumentLoaders/Social_Network_Ads.csv")

data = loader.load()

print(data[0].page_content)


#we can create out own document loader 
# there are various document loaders in the langchain


##?  DOCS-For the further use 
#!  https://python.langchain.com/docs/integrations/document_loaders/


##? CREAT your own document loader

#! https://python.langchain.com/docs/how_to/document_loader_custom/

