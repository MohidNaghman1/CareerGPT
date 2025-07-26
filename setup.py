
import os
# --- NEW: Import the dotenv library ---
from dotenv import load_dotenv 
import google.generativeai as genai
from read_pdfs import process_all_folders
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# --- NEW: Load environment variables from the .env file ---
# This line should be at the very top, right after the imports.
load_dotenv()

# --- Configuration (rest of the script is the same) ---
BASE_FOLDER = "carrer_docs"
FOLDERS_TO_PROCESS = [
    os.path.join(BASE_FOLDER, "Roadmap"),
    os.path.join(BASE_FOLDER, "Resume"),
    os.path.join(BASE_FOLDER, "Courses")
]
VECTOR_STORE_PATH = "faiss_index"

def main():
    """
    Main function to create and save the vector store using Google's embeddings.
    """
    print("--- Starting the creation of the vector store using Google AI ---")

    # This part will now work because load_dotenv() has loaded the key
    try:
        GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
        genai.configure(api_key=GOOGLE_API_KEY)
        print("Google API Key loaded successfully from .env file.")
    except KeyError:
        print("❌ Error: GOOGLE_API_KEY not found in .env file or environment.")
        print("Please ensure your .env file is in the same directory and contains the key.")
        return

    # ... the rest of your script remains unchanged ...
    
    print("\nStep 1: Loading and chunking documents...")
    documents = process_all_folders(FOLDERS_TO_PROCESS)
    if not documents:
        print("No documents were processed. Exiting.")
        return
    print(f"Successfully loaded and chunked {len(documents)} documents.")
    
    print("\nStep 2: Initializing the Google Generative AI embedding model...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    print("Google embedding model initialized.")
    
    print("\nStep 3: Embedding documents and creating FAISS vector store...")
    vector_store = FAISS.from_documents(
        documents=documents, 
        embedding=embeddings
    )
    print("Vector store created successfully.")
    
    print(f"\nStep 4: Saving the vector store to '{VECTOR_STORE_PATH}'...")
    vector_store.save_local(VECTOR_STORE_PATH)
    print("✅✅✅ Vector store saved successfully! ✅✅✅")
    print("The 'faiss_index' directory is now ready for your chatbot.")

if __name__ == "__main__":
    main()