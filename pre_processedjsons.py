import requests
import os
import json
import pandas as pd
import joblib

BATCH_SIZE = 50


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


jsons = os.listdir("jsons")

my_dicts = []
chunk_id = 0

for json_file in jsons:

    with open(f"jsons/{json_file}", "r", encoding="utf-8") as f:
        content = json.load(f)

    print(f"Creating Embeddings for {json_file}")

    all_embeddings = []

    for i in range(0, len(content["chunks"]), BATCH_SIZE):

        print(f"Embedding batch {i // BATCH_SIZE + 1}")

        batch_texts = [
            c["text"]
            for c in content["chunks"][i:i + BATCH_SIZE]
        ]

        batch_embeddings = create_embedding(batch_texts)

        all_embeddings.extend(batch_embeddings)

    print("Chunks:", len(content["chunks"]))
    print("Embeddings:", len(all_embeddings))

    for i, chunk in enumerate(content["chunks"]):

        chunk["chunk_id"] = chunk_id
        chunk["embedding"] = all_embeddings[i]

        chunk_id += 1

        my_dicts.append(chunk)

df = pd.DataFrame.from_records(my_dicts)
joblib.dump(df, "embeddings.joblib")
