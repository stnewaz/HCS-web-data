import pandas as pd

print("check_embeddings.py is running...\n")

try:
    qa = pd.read_csv("StructuredQA_final.csv", encoding="latin1")
    emb = pd.read_csv("EmbeddingsFinal.csv", encoding="latin1")

except FileNotFoundError as e:
    print("File not found:", e)
    raise SystemExit()

print("StructuredQA_final shape:", qa.shape)
print("EmbeddingsFinal shape:", emb.shape)

zero_rows = (emb.sum(axis=1) == 0).sum()
print("Number of all-zero rows in embeddings:", zero_rows)

# Show sample rows
print("\nStructuredQA_final head:")
print(qa.head(3))

print("\nEmbeddingsFinal head:")
print(emb.head(2))
