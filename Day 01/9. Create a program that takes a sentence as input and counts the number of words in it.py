#9. Create a program that takes a sentence as input and counts the number of words in it.py
def word_count(sentence):
    word=sentence.split()
    return len(word)

sen=input('ENter a sentence : ')

words=word_count(sen)

print(words)