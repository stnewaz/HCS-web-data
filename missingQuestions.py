import os
import re
import pandas as pd

# -------------------------------
# Load CSV and extract numeric names
# -------------------------------
csv_df = pd.read_csv("HCS_website_edited.csv")

csv_numbers = (
    csv_df["name"]
    .astype(str)
    .str.strip()
    .tolist()
)

# -------------------------------
# Extract numeric names from question files
# -------------------------------
questions_dir = "new_questions_output"

question_numbers = []

for f in os.listdir(questions_dir):
    if f.endswith("_questions.txt"):
        num = re.sub(r"_questions\.txt$", "", f)
        question_numbers.append(num)

# -------------------------------
# Find missing numbers (CSV - Questions)
# -------------------------------
missing_in_questions = sorted(
    set(csv_numbers) - set(question_numbers),
    key=lambda x: [int(n) for n in x.split("_")]
)

# -------------------------------
# Output results
# -------------------------------
print("Missing numeric files:")
for m in missing_in_questions:
    print(m)

print("\nTotal missing:", len(missing_in_questions))
