# Storing LLM models => LLaMa, Mistral, Gemini

# AI MODEL (GENERATIVE AI MODELS)
class LLM_SERVICE_PROVIDER:

    MODEL_LLAMA = "llama-3.3-70b-versatile"
    MODEL_MISTRAL_1 = "ministral-8b-latest"
    MODEL_MISTRAL_2 = "mistral-small-latest"
    MODEL_GEMINI = "gemini-2.5-flash-lite"
    MODEL_COHERE = ""
    
# EMBEDDING MODELS BY HUGGINGFACE
class EMBEDDING_MODEL_PROVIDER:

    HUGGING_FACE_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

embedding_model_provider = EMBEDDING_MODEL_PROVIDER()
llm_service_provider = LLM_SERVICE_PROVIDER()