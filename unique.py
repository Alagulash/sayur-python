sentence=input("enter a string:")
sentence.lower()
words=sentence.split()
unique_word={}
for word in words:
    if not word in unique_word:
        unique_word[word]=0
        print(word,end=" ")