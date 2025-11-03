import requests
import os
import pandas as pd
import json
import joblib
def create_embedding(text_list):
    # https://github.com/ollama/ollama/blob/main/docs/api.md#generate-embeddings
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embedding = r.json()["embeddings"] 
    return embedding
# Make sure output directory exists
chunk_id = 0
my_dict = []
j = os.listdir("json")
os.makedirs("embeddings", exist_ok=True)
for file in j:
    with open(os.path.join("json",file), 'r', encoding='utf-8') as f:
        data = json.load(f)
    texts = [chunk['text'] for chunk in data['chunks']]
    embeddings = create_embedding(texts)
    for i,chunk in enumerate(data['chunks']):
        chunk['id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        chunk['title'] = data['chunks'][0]['title']
        chunk['number'] = data['chunks'][0]['number']
        my_dict.append(chunk)
    print(f"✅ Processed file: {file}\n")
df = pd.DataFrame.from_records(my_dict)
print(df.columns)
# joblib.dump(df, "embedding.joblib")