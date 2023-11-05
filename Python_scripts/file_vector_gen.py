import os
from gensim.models.fasttext import FastText
from gensim.utils import simple_preprocess
import numpy as np

model = FastText.load("fasttext_model.model")

documents_directory = "D:\\FYP\\Articles"

file_vectors = []

for filename in os.listdir(documents_directory):
    if filename.endswith(".txt"):  
        with open(os.path.join(documents_directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            tokens = simple_preprocess(content)

            word_vector = [model.wv[word] for word in tokens if word in model.wv]
            file_vectors += [np.mean(word_vector, axis=0)]