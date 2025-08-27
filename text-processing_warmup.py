import sys
import re

data = sys.stdin.read().strip().split('\n')

data_1 = [i for i in data if len(i)>1]
mnths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

for text in data_1:
    found_a = re.findall(r'\ba\b', text, flags=re.IGNORECASE)
    found_an = re.findall(r'\ban\b', text, flags=re.IGNORECASE)
    found_the = re.findall(r'\bthe\b', text, flags=re.IGNORECASE)
    found_date = 0
    
    words = re.sub(r'[^A-Za-z0-9]', ' ', text).strip().lower().split()
    for i in range(len(words)):
        if i > 1:
            yr = ''
            if len(words[i])==5:
                yr = words[i][:-1]
            if len(words[i])==4:
                yr = words[i]
            if yr:
                if yr.isdigit():
                    mnth = ''
                    dt = ''
                    dt_1 = words[i-1]
                    dt_2 = words[i-2]
                    if len(dt_1) > 2:
                        for j in mnths:
                            if j in dt_1.lower():
                                mnth = dt_1
                                if dt_2.isdigit():
                                    dt = dt_2
                                break
                    if len(dt_2) > 2:
                        for j in mnths:
                            if j in dt_2.lower():
                                mnth = dt_2
                                if dt_1.isdigit():
                                    dt = dt_1
                                break
                    if dt and mnth:
                        found_date += 1
                    if words[i-1].isdigit() and words[i-2].isdigit():
                        found_date += 1
            if len(words[i]) == 2 and words[i].isdigit():
                if words[i-1].isdigit() and words[i-2].isdigit():
                    found_date += 1
    
    print(len(found_a))
    print(len(found_an))
    print(len(found_the))
    print(found_date)
