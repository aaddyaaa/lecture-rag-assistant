import requests
import numpy as np
import pandas as pd
import joblib

from sklearn.metrics.pairwise import cosine_similarity


def create_embedding(text_list):
    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": "bge-m3",
            "input": text_list
        }
    )

    data = r.json()

    if "embeddings" in data:
        return data["embeddings"]

    if "embedding" in data:
        return data["embedding"]

    raise Exception(data)

def inference(prompt, model):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    response = r.json()
    print(response)
    return response

# Load saved embeddings
df = joblib.load("embeddings.joblib")
print(df.columns)
print(df.head())

# Ask user question
incoming_query = input("Ask a Question: ")

# Create embedding for question
question_embedding = create_embedding([incoming_query])[0]

# Calculate cosine similarity
similarities = cosine_similarity(
    np.vstack(df["embedding"]),
    [question_embedding]
).flatten()

# Get top 3 results
top_results = 5
max_indx = similarities.argsort()[::-1][:top_results]

# Retrieve matching chunks
results = df.loc[max_indx]

# print("\nTop Results:\n")

#for _, row in results.iterrows():
#    print({row['title']})
#    print({row['number']})
#    print({row['text']})
prompt = f"""
I am teaching an Artificial Intelligence course.

Here are the retrieved video chunks:

{results[["title", "number", "text", "start", "end"]].to_json(orient="records")}

The user asked:

{incoming_query}

Instructions:
1. Answer ONLY using the information present in the retrieved chunks.
2. Mention the video title and timestamp whenever possible.
3. If the answer is not present in the chunks, say:
   "I could not find the answer in the course content."
"""
response = inference(prompt, "llama3.2")["response"]
print(response)
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response)
with open("prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt)


#for index, item in results.iterrows():
#    print(index, item["title"], item["number"], item["text"], item["start"], item["end"])