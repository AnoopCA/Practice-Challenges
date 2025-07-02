import sys

if __name__ == '__main__':
    s = sys.stdin.read().strip()
    s = s.strip().split('.')
    s = [snt.strip().lower() for snt in s if snt!='']
    word_list = []
    for sentence in s:
        words = sentence.split()
        for w in range(len(words)):
            if w < (len(words)-2):
                word_list.append(words[w:w+3])
    word_list = [' '.join([j for j in i]) for i in word_list]
    tri_dict = {t:0 for t in word_list}
    for tri in word_list:
        if tri in tri_dict:
            tri_dict[tri] += 1

    max_freq = max(tri_dict.values())
    for key,value in tri_dict.items():
        if value == max_freq:
            print(key)
            break
