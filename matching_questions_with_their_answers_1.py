import sys
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.optimize import linear_sum_assignment

data = sys.stdin.read().strip().split('\n')

paragraph = data[0]
questions = data[1:6]
answers = data[6].split(';')

all_data = [paragraph] + questions + answers
#vectorizer = CountVectorizer().fit(corpus)
tfidf_vec = TfidfVectorizer().fit(all_data)
question_vecs = tfidf_vec.transform(questions)
answer_vecs = tfidf_vec.transform(answers)

similarity_matrix = cosine_similarity(question_vecs, answer_vecs)
row_ind, col_ind = linear_sum_assignment(-similarity_matrix)

for j in col_ind:
    print(answers[j])
