contract = { "I'm": 'I am', "I've":'I have', "I'll":'I will'}
sentence = input('Enter sentence: ')
for key in contract:
    sentence = sentence.replace(key, contract[key])
print(sentence)