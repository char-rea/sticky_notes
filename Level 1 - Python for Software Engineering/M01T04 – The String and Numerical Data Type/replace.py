sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

print(sentence)

sentence = sentence.replace("!", " ")
print(sentence)

upper_sentence = sentence.upper()
print(upper_sentence)

sentence = sentence.replace("!", "")
print(sentence[-1:0:-1])