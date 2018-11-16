words = input('Enter sentence: ').split(' ')
lower_words = [word.lower() for word in words]
for i in range(len(lower_words)):
    word = lower_words[i]
    if 'ei' in word and not 'cei' in word:
        print('{} : {}'.format(i + 1, words[i]))
