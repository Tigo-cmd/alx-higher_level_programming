#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    words = dir(hidden_4)
    final = []
    for word in words:
        if word.startswith("__"):
            continue
        final.append(word)
    final.sort()
    for i in final:
        print(i)
