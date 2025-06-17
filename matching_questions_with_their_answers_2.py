import fileinput
import string
import re
### Stop words list
stop=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'yo', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']

questions_word=['which','what','who','how']
stop.extend(questions_word)

# Find the ratio of count of common words between sentence1 and sentence2 for count of words in sentence2 
def similarity(sentence1,sentence2):
    sentence1_set = set(sentence1.split(" "))
    sentence2_set = set(sentence2.split(" "))
    score = float(len(sentence1_set.intersection(sentence2_set)))/len(sentence2_set)
    return score

# Extract sentences, questions, answers
i=-1
questions=[]
for line in fileinput.input():
    if i==-1:
        sentences =[x.replace("\n","").lower() for x in line.split(".")]
        i=i+1
    else:
        questions.append(line.replace("\n","").lower())
answer_set_orginal = questions[-1]
questions.remove(answer_set_orginal)
answer_set = answer_set_orginal.split(";")

#process the question, answers by removing stop words and punctuations
processed_questions=[]
processed_answers=[]
for each_question in questions:
    processed_string = " ".join([x.lower() for x in each_question.split(" ") if x.lower() not in stop])
    processed_questions.append(re.sub("[^a-zA-Z]"," ",processed_string))

for each_answer in answer_set:
    processed_answer = " ".join([x.lower() for x in each_answer.split(" ") if x.lower() not in stop])
    processed_answers.append(re.sub("[^a-zA-Z]"," ",processed_answer))

# Find the matching pair of questions with high similarity    
exact_match={}
for i in range(len(processed_questions)):
    max_sim=0;
    for j in range(len(processed_answers)):
        for each_sentence in sentences:
            # similarity is calculated by product of similarity(sentence,question) and similarity(sentence,answer)
            sim = similarity(each_sentence,processed_questions[i])*similarity(each_sentence,processed_answers[j])
            if sim > max_sim:
                max_sim=sim
                exact_match[i]=j
    
    
# print the exact match    
for i in range(len(questions)):
    print(answer_set[exact_match[i]])
