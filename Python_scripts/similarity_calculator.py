import numpy as np
from file_tf_idf import tf_idf_matrices 
from sklearn.metrics.pairwise import cosine_similarity
from file_vector_gen import file_vectors
from file_score_handler import update_file_score

d ={}
sim_list = []
for i in range(1):
    for j in range(5000):

        tf_idf_sim = cosine_similarity(tf_idf_matrices[j],tf_idf_matrices[5000+i])[0,0]

        m1 = np.linalg.norm(file_vectors[j])
        m2 = np.linalg.norm(file_vectors[5000+i])
        dot_prod = np.dot(file_vectors[j].T,file_vectors[5000+i].T)

        fast_sim = dot_prod/(m1*m2)

        over_sim = tf_idf_sim*fast_sim

        file_name = "article"+str(j+1)+".txt"

        sim_list += [over_sim]

        d[file_name] = over_sim

        if(over_sim > 0.2):
            score = 1
        else:
            score = -0.25

        update_file_score(file_name,score)

print(sorted(d.items(), key=lambda x: x[1], reverse=True))
