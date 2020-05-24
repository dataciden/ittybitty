sen = input ("Write your sentence: ")
dict = {}
for i in sen:
    dict[i] = (len(sen.split(i))-1)
print (dict)
    