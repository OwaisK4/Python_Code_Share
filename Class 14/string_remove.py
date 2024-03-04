s = "these are words"
f = "these2are2words2an"


def spacerFiller(sentence: str):
    list = sentence.split()
    counts = []
    for word in list:
        counts.append(len(word))
    minNum = min(counts)
    sentence = sentence[:5] + str(minNum) + sentence[6:]
    # print(sentence)
    answer = ""
    for i in sentence:
        if i == " ":
            answer = answer + (str(minNum))
        else:
            answer = answer + i
    print(answer)


spacerFiller(s)

#  [5]
#  [3]
#  [2]
#  [5]
#  ""
#  "t"
#  "th"
#  "the"
#  "thes"
#  "these"
#  "these2"
#  "these2a"
#  "these2are"

# "a" + "b"
#  "ab"
