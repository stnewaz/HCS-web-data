AI Chatbot for the SFU Health and Counseling website.

**Technical Contributions & Data Pipeline**
Step 1: Gathering links from the SFU Health and Counselling page until the data is redundant or there are no more nested links in a CSV file.
Step 2: Creating a data folder with text scraped from the web page as individual text files
Step 3: Using GPT-4 Mini to generate possible questions for each text file (eg. webpage)
Step 4: Using GPT-4 Mini to generate answers to the corresponding question files using the data folder files as context.
Step 5: Merging the answers and questions file into one CSV file.
Step 6: Generate an embedding file of the merged QA to be used for the chatbot.
Step 7: Tested the full pipeline to verify correct retrieval, applied guardrails, and checked chatbot performance.

***Please unzip the EmbeddingsFinal.zip file - the file is too big to upload to our repository directly.***
- The file generate_embed.py includes the updated embedding code
- new_question_output includes the newly generated questions
