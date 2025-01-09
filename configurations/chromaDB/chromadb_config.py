import chromadb

def initialize_chroma(INVENTORY_PATH):
    INVENTORY_PATH = INVENTORY_PATH
    CHROMA_COLLECTION = "autogen-docs"
    chroma_client = chromadb.PersistentClient(path=INVENTORY_PATH)
    AZ_collection = chroma_client.get_or_create_collection(name=CHROMA_COLLECTION)
    return chroma_client, AZ_collection, INVENTORY_PATH, CHROMA_COLLECTION
