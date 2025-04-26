import os
from llmware.library import Library
from llmware.setup import Setup
from llmware.retrieval import Query
from llmware.models import ModelCatalog
import os


# 1. Initialize LLMWare and Download Required Files
# Set your LLMWare license key (required for certain models)
# os.environ["LLMWare_License_Key"] = "YOUR_LLMWare_License_Key"  # Replace with your key

# print ("Step 1: Downloading and Installing Model Assets")
# Setup().run()  #  Download all required models


# 2. Create a Library and Load the PDF
print ("Step 2: Creating and Loading a Library")
library_name = "my_pdf_rag_library"  # Choose a name for your library

# Check if the library already exists, and create it if not
library = Library().create_new_library(library_name)

# Add your PDF file to the library
pdf_file_path = "C:\\Users\\aybakana\\source\\repos\\00_AI_Agents_Experiments\\05_LLMWare_Agent\\"  # Replace with the actual path to your PDF file
library.add_files(pdf_file_path)
print(f"Added {pdf_file_path} to the library.")


# 3. Index the Library for Retrieval (Important for efficient searching)
print ("Step 3: Indexing the Library")
library.index()



# 4. Define the SLIM Model
print ("Step 4: Defining the SLIM Model")

# Get the SLIM model ID from the model catalog

# Using a more robust approach to ensure the model ID is correct
slim_model_info = ModelCatalog().check_details(model_name="slim")
slim_model_id = slim_model_info["model_id"]  # Extract the model_id

print(f"Using SLIM model ID: {slim_model_id}")


# 5. Define the Query Object and Run the RAG
print ("Step 5: Asking Questions and Getting Answers")

query = Query(library)

while True:
    user_question = input("Ask a question about the PDF (or type 'exit'): ")
    if user_question.lower() == 'exit':
        break


    # Run the query with the SLIM model
    # You can customize retrieval_count to control the number of documents retrieved
    response = query.run(user_question, model_name=slim_model_id, prompt_name="default", retrieval_count=3)


    # Print the results
    print("\nAnswer:")
    print(response["answer"])

    print("\nSupporting Context:")
    for context in response["prompt_based_answer"]["evidence"]:
        print(context)

print("Finished.")