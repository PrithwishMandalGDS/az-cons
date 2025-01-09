import chromadb
from chromadb.utils import embedding_functions

def initialize_openai_embedding_function():
    OPENAI_EMBEDDING_MODEL = 'text-embedding-ada-002'
    OPENAI_API_KEY = 'dFndVNaSSIzadHvG0LFCkIA7GIuQaeiz'
    OPENAI_API_BASE = 'https://eyq-incubator.asiapac.fabric.ey.com/eyq/as/api'
    OPENAI_API_TYPE = 'azure'
    OPENAI_API_VERSION = '2023-05-15'

    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        model_name=OPENAI_EMBEDDING_MODEL,
        api_key=OPENAI_API_KEY,
        api_base=OPENAI_API_BASE,
        api_type=OPENAI_API_TYPE,
        api_version=OPENAI_API_VERSION
    )

    return openai_ef