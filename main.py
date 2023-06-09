# -*- coding: utf-8 -*-
"""function_deploy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eW_pkvsmL_kFte7NVyXbctFqkmfmYwiB
"""

#pip install faiss-cpu

#pip install sentence-transformers

from flask import Flask, request, jsonify, render_template
import re
import math
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import pickle

# Load the index from the pickle file
#with open('index.pickle', 'rb') as f:
#    index = pickle.load(f)

app = Flask(__name__)

q = ""

@app.route("/")
def loadPage():
        return render_template('home.html', query="")

@app.route("/", methods=['POST'])

def search():
    df = pd.read_csv('data.csv')
    sentences = list(df['Product description'])
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')  # Replace 'model_name' with the appropriate model
    embeddings = model.encode(sentences)
    index = faiss.IndexFlatIP(embeddings.shape[1])  # Initialize the index
    index.add(embeddings)  # Add the embeddings to the index    
# query = request.json['query']
    inputQuery1 = request.form['query1']
    # Encode the query
    query_embedding = model.encode([inputQuery1])

    # Perform the similarity search
    D, I = index.search(np.array(query_embedding), k=5)

    results = []
    for i, idx in enumerate(I[0]):
      result = f"Similarity Rank {i+1}: {sentences[idx]}"
      results.append(result)
    return render_template('home.html', output1 = results, query1 = request.form['query1'])

if __name__ == '__main__':
    app.run(debug=True)

index = faiss.IndexFlatIP(embeddings.shape[1])  # Initialize the index
index.add(embeddings)  # Add the embeddings to the index

# def get_similarity(query_text):
#   query_embedding = model.encode([query_text])
#   D, I = index.search(np.array(query_embedding), k=5)  # Retrieve top 5 most similar sentences
#   # # Display the results
#   # for i, idx in enumerate(I[0]):
#   #   return (f"Similarity Rank {i+1}: {sentences[idx]}")
#   results = []
#   for i, idx in enumerate(I[0]):
#       result = f"Similarity Rank {i+1}: {sentences[idx]}"
#       results.append(result)
#   return results

# get_similarity(query)

# query_embedding = model.encode([query])  # Encode the query sentence

# # Perform the similarity search
# D, I = index.search(np.array(query_embedding), k=5)  # Retrieve top 5 most similar sentences

# # Display the results
# for i, idx in enumerate(I[0]): 
#     print(f"Similarity Rank {i+1}: {sentences[idx]}")

#pip freeze

