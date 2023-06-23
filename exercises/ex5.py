def replace_period(sentence, punct ):
    new_sentence=sentence.replace(".",punct)
    print(new_sentence)

sentence = "Test.  This is a test.  Testing."
sentence2 = replace_period(sentence, "!")
print(sentence2)