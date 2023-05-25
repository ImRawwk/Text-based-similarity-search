# Text-based-similarity-search
Contains notebook for text based similarity search for clothing products
This project focuses on performing semantic similarity search on a collection of clothing product descriptions. The goal is to provide recommendations for similar products based on a given query text.

Overview
The project consists of several steps:

Scraping product descriptions: Scrapes product descriptions from a website (ASOS) using web scraping techniques. The scraped data includes the product links and corresponding descriptions.

Preprocessing the data: Cleans and preprocesses the scraped product descriptions. The preprocessing steps include lowercasing, removing numbers and special characters, removing stopwords, and lemmatization.

Building a similarity search engine: Utilizes different approaches to perform similarity search. The project uses both TF-IDF vectorization and the Sentence Transformers library for semantic embedding of the text descriptions.

Searching for similar products: Applies the similarity search techniques to find the top similar products based on a given query text.

Saving the results: Stores the index and model for later use in order to perform similarity searches on new queries without re-computing the embeddings.

**Instructions for deployment -**

To deploy the code for semantic search using FAISS and Sentence Transformers, follow these steps:

Install the required packages:

Run pip install faiss-cpu to install the FAISS library for efficient similarity search.
Run pip install sentence-transformers to install the Sentence Transformers library for text embedding.
Prepare the data:

Make sure you have a CSV file named data.csv containing the product data, with a column named "Product description" that includes the text descriptions of the products.
Load the index and model:

Load the saved index and model using the pickle files.

Prepare the embeddings and create the index:

Encode the text descriptions using the Sentence Transformer model and create the FAISS index.

Define the query function:

Define a function that takes a query text as input and retrieves the most similar product descriptions.

Deploy the code:

Now, you can deploy the code by calling the get_similarity function with a query text to get the most similar product descriptions.

This will print the top 5 similar product descriptions based on the provided query.
