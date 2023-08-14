#!/usr/bin/python3
def multiple_returns(sentence):
    new_list = []
    if sentence == "":
        length = 0
        sentence = None
        new_list.append(length)
        new_list.append(sentence)
    else:
        length = len(sentence)
        i = sentence[:1]
        new_list.append(length)
        new_list.append(i)
    return tuple(new_list)
