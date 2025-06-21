import sys
import json

if __name__ == "__main__":
    with open('training.json', 'r') as f:
        data = f.readlines()
    
    subj_list = ['English', 'Physics', 'Chemistry', 'Mathematics', 'Computer Science', 'Biology', 'Physical Education', 'Economics', 'Accountancy', 'Business Studies', 'serial']
    for i in data[1:]:
        temp = json.loads(i)
        print(temp)
    

    #data = sys.stdin.read().strip().split('\n')
