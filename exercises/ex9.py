def vowel_counter(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count




sentence = "This is a test"
num_vowels = vowel_counter(sentence)
print(num_vowels)