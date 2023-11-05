import os
from gensim.models.fasttext import FastText
from gensim.utils import simple_preprocess


documents_directory = "Articles"

tokenized_documents = []

for filename in os.listdir(documents_directory):
    if filename.endswith(".txt"):  
        with open(os.path.join(documents_directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            tokens = simple_preprocess(content)
            tokenized_documents.append(tokens)

model = FastText(tokenized_documents, vector_size=100, window=30, min_count=1, sg=1)

model.save("fasttext_model.model")