import os
import sys
from Backend.Core.Features.RagPipeLine.IngestionPipeLine import INGESTION_PIPELINE_MODEL

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test():

    ipm = INGESTION_PIPELINE_MODEL()
    documents = ipm.load_all_docs(file_path="Assets/pdf")
    clean_document = ipm.clean_docs(documents)
    chunks = ipm.text_to_chunks(clean_document)
    db_store = ipm.create_vector_db(chunks=chunks)
    return db_store

if __name__ == "__main__":
    test()