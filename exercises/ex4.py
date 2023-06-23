def count_words(sentence):
    number = sentence.split()
    print(len(number))

sentence = input("Enter sentence: ")
num_words = count_words(sentence)
print(num_words)