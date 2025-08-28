from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path = 'books', 
    glob = '*.pdf', 
    loader_cls=PyPDFLoader
)

result = loader.lazy_load()
# ye same time par file ko lega uska metadata load karega aur fir use hone ke baad delete kar deta

# agr load use karte toh voh pehle sara data load karta then usko print karta 
for document in result:
    print( document.metadata)