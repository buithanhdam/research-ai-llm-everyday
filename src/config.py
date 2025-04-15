from dataclasses import dataclass
import enum
from pydantic import BaseModel
import dotenv 
dotenv.load_dotenv()
import os
from src.prompt import (LLM_SYSTEM_PROMPT)

SUPPORTED_FILE_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".html",
    ".txt",
    ".csv",
    ".xlsx",
    # ".json",
    # ".pptx",
]

class RAGType(enum.Enum):
    NORMAL = "normal_rag"
    HYBRID = "hybrid_rag"
    CONTEXTUAL = "contextual_rag"
    FUSION = "fusion_rag"
    HYDE = "hyde_rag"
    NAIVE = "naive_rag"
    
class LLMConfig(BaseModel):
    api_key: str
    model_name: str
    model_id: str
    temperature: float = 0.7
    max_tokens: int = 2048
    system_prompt: str = "You are a helpful assistant."
    
class QdrantPayload(BaseModel):
    """Payload for vectors in Qdrant"""
    document_id: str | int
    text: str
    vector_id: str
    
class Config:
    OPENAI_CONFIG = LLMConfig(
        api_key=os.environ.get('OPENAI_API_KEY'),
        model_name="GPT",
        model_id="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens= 2048,
        system_prompt=LLM_SYSTEM_PROMPT
    )

    GEMINI_CONFIG = LLMConfig(
        api_key=os.environ.get('GOOGLE_API_KEY'),
        model_name="Gemini",
        model_id="models/gemini-2.0-flash",
        temperature=0.8,
        max_tokens = 2048,
        system_prompt=LLM_SYSTEM_PROMPT
    )
    CLAUDE_CONFIG = LLMConfig(
        api_key=os.environ.get('ANTHROPIC_API_KEY'),
        model_name="Claude",
        model_id="claude-3-haiku-20240307",
        temperature=0.7,
        max_tokens=4000,
        system_prompt=LLM_SYSTEM_PROMPT
    )

