import re

s = "A man, a plan, a canal: Panama"

s = s.lower()
s = re.sub('[^a-z0-9]','',s)

print(s)
print(s[::-1])