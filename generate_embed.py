from openai import OpenAI
import pandas as pd

with open("APIKEY", "r") as f:
    API_KEY = f.read().strip()

client = OpenAI(api_key=API_KEY)

def get_embedding(text, model="text-embedding-3-small"):
    if pd.isna(text):
        return [0.0] * 1536

    text = str(text).replace("\n", " ")
    response = client.embeddings.create(
        model=model,
        input=[text]
    )
    return response.data[0].embedding

df = pd.read_csv("StructuredQA_final.csv")

embeddings = df["Question"].apply(get_embedding)

embedding_df = pd.DataFrame(embeddings.tolist())

embedding_df.to_csv("EmbeddingsFinal.csv", index=False)

print("Embeddings generated successfully.")