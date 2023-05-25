def count_words(sentence):
    sentence = sentence.lower()
    resultdict = {}
    for ch in sentence:
        if not ch.isalpha() and not ch.isnumeric() and ch != "'":
            sentence = sentence.replace(ch, " ")
    wordlist = sentence.split()
    for word in wordlist:
        if word not in resultdict:
            resultdict[word] = 1
        else:
            resultdict[word] += 1
    return resultdict
