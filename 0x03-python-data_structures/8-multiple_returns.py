#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        a = None
        result = (len(sentence), a)
    else:
        result = (len(sentence), sentence[0])
    return result

