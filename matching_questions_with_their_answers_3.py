import fileinput
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

i = -1
questions = []
for line in fileinput.input():
    if i == -1:
        sentences = [x.strip().lower() for x in line.strip().split(".") if x.strip()]
        i += 1
    else:
        questions.append(line.strip().lower())

answer_set_original = questions[-1]
questions = questions[:-1]
answer_set = answer_set_original.split(";")

all_data = sentences + questions + answer_set
tfidf_vec = TfidfVectorizer().fit(all_data)

sentence_vecs = tfidf_vec.transform(sentences)
question_vecs = tfidf_vec.transform(questions)
answer_vecs = tfidf_vec.transform(answer_set)

exact_match = {}
for q_idx, q_vec in enumerate(question_vecs):
    max_score = 0
    best_ans_idx = -1
    for a_idx, a_vec in enumerate(answer_vecs):
        for s_vec in sentence_vecs:
            sim_q = cosine_similarity(s_vec, q_vec)[0][0]
            sim_a = cosine_similarity(s_vec, a_vec)[0][0]
            joint_sim = sim_q * sim_a
            if joint_sim > max_score:
                max_score = joint_sim
                best_ans_idx = a_idx
    exact_match[q_idx] = best_ans_idx

for i in range(len(questions)):
    print(answer_set[exact_match[i]])
