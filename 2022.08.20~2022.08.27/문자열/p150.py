import collections
import re


paragraph = "abc abc? abcd the jeff!"
banned = ["abc","abcd","jeff"]

# paragraph = paragraph.lower()
# new_paragraph = re.sub("[!?',;.]",' ',paragraph)
# new_paragraph = new_paragraph.split()
# new_paragraph = [i for i in new_paragraph if i not in banned]
# new_paragraph_count = collections.Counter(new_paragraph)
# print(new_paragraph_count.most_common(1)[0][0])


#책 풀이

words = [word for word in re.sub(r'[^\w]',' ',paragraph)
        .lower().split()
        if word not in banned]

counts = collections.Counter(words)
print(counts.most_common(1)[0][0])
