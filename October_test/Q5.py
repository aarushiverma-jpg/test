sentence="Python is easy and Python is powerful"

lis=sentence.split()

d={}

for word in lis:
    key=word.lower()
    d[key]=d.get(key,0)+1

print(d)