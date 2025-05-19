import re

ptn = r'\b[0-9]+\b'

txt = 'value: 34543 example @domain.com'

print(re.findall(ptn, txt))
