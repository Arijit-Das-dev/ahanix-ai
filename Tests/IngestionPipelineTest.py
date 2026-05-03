from Backend.Core.Features.RagPipeLine.IngestionPipeLine import INGESTION_PIPELINE_MODEL

def test():

    ipm = INGESTION_PIPELINE_MODEL()
    document = ipm.load_all_docs(file_path="Assets/pdf")
    chunks = ipm.text_to_chunks(documents=document)
    vectorStore = ipm.create_vector_db(chunks=chunks)
    return vectorStore
    
if __name__ == "__main__":
    test()