from src.rag.rag_manager import RAGManager
from src.config import RAGType
from src.config import global_config, LLMType
from .base import create_function_tool

RAG_DESCRIPTION = f"""
Search through business knowledge base return relevant business information
"""
def retrieve_documents(query: str) -> str:
    """
    Search through knowledge base return relevant information
            
    Args:
        query: Search query
    """
    rag_manager = RAGManager.create_rag(
            rag_type=RAGType.HYBRID,
            vector_db_url=global_config.QDRANT_URL,
            llm_type=LLMType.GEMINI,
        )
    def search_documents(query: str, collection_name: str = "test_collection", limit: int = 5) -> str:
        return rag_manager.search(query=query, collection_name=collection_name,limit=limit)
    
    return search_documents(query=query)

rag_retriever_tool = create_function_tool(
    func=retrieve_documents,
    name="rag_retriever_tool",
    description=RAG_DESCRIPTION,
)