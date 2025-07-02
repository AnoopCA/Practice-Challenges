from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

s = ["I'd like an apple.", "An apple a day keeps the doctor away.", "Never compare an apple to an orange.", "I prefer scikit-learn to orange."]

similarity_list = []
for ln in range(len(s)):
    vec = TfidfVectorizer()
    if ln < (len(s)-1):
        matx = vec.fit_transform([s[0], s[ln+1]])
        similarity = cosine_similarity(matx[0:1], matx[1:2])[0][0]
        similarity_list.append(similarity)
print(similarity_list.index(min(similarity_list))+1)
