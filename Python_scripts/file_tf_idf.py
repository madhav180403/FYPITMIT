from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Directory containing documents
documents_directory = "D:\\FYP\\Articles"

# Create a list to hold document contents
document_contents = []

# Iterate through the documents in the directory
for filename in os.listdir(documents_directory):
    if filename.endswith(".txt"):  # Adjust the file extension as needed
        with open(os.path.join(documents_directory, filename), 'r', encoding='utf-8') as file:
            content = file.read()
            document_contents.append(content)

vectorizer = TfidfVectorizer()

tf_idf_matrix = vectorizer.fit_transform(document_contents)

tf_idf_matrices = []

for i in range(len(document_contents)):
    document_matrix = vectorizer.transform([document_contents[i]])
    tf_idf_matrices.append(document_matrix)
