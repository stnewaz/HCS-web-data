import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_text_from_webpage(url, txt_file_name):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    paragraphs = soup.find_all('p')

    # Extract text from each paragraph and store in a list
    text_data = [p.get_text() for p in paragraphs]

    # Define the output txt file
    file_name = f"C:/Users/samsa/Documents/CLASSES/IAT 360/final/output/web-scraped/{txt_file_name}.txt"

    # Open the file in write mode
    with open(file_name, 'w', encoding='utf-8') as file:
        # Write each paragraph to the file
        for paragraph in text_data:
            file.write(paragraph + '\n\n')  # Add extra newline for readability

    print(f'Data successfully saved to {file_name}')

csv_file = "C:/Users/samsa/Documents/CLASSES/IAT 360/final/datasets/HCS_website2.csv"
df = pd.read_csv(csv_file)

list_of_exceptions = ["1_1_15",
                    "1_1_2_2",
                    "1_1_2_3",
                    "1_1_5_2",
                    "1_1_12_8_1",
                    "1_1_12_10_2",
                    "1_1_12_10_3",
                    "1_2_4_1",
                    "1_2_11_9",
                    "1_2_11_10",
                    "1_2_3_5_2",
                    "1_2_3_5_3",
                    "1_1_12_6_2"]

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    url = row['link']
    file_name = row['name']
    if file_name in list_of_exceptions:
        continue
    extract_text_from_webpage(url, file_name)
