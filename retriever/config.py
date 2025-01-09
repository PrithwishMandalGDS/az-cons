from llm.config import initialize_llm_config
from chromaDB.chromadb_config import initialize_chroma
from embeddings.embeddings import initialize_openai_embedding_function
from autogen.agentchat.contrib.vectordb.chromadb import ChromaVectorDB
# inventory_path = "tmp/chromaDB/az"

def initialize_config(chunk_token_size, docs_path, n_results, get_or_create, overwrite, update_context, INVENTORY_PATH):
    INVENTORY_PATH = INVENTORY_PATH
    chroma_client, AZ_collection, INVENTORY_PATH, CHROMA_COLLECTION = initialize_chroma(INVENTORY_PATH)
    AZ_collection = chroma_client.get_or_create_collection(name=CHROMA_COLLECTION)
    openai_ef = initialize_openai_embedding_function()
    az_vector_db = ChromaVectorDB(path=INVENTORY_PATH, embedding_function = openai_ef)
    llm_config = initialize_llm_config(timeout=600, temperature=0.9)
    aiops_config = {
        "task": "qa",
        "model": llm_config['config_list'][0]['model'],
        "update_context": update_context,
        "chunk_token_size": chunk_token_size,
        "n_results": n_results,
        "docs_path": docs_path,
        "get_or_create": get_or_create,
        "overwrite": overwrite,
        "vector_db": az_vector_db,
        "collection_name": CHROMA_COLLECTION,
        "embedding_function": openai_ef
    }
    return aiops_config