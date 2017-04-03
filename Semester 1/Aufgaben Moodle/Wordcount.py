# coding=utf-8
def word_count(s):
    output = {}
    for word in s.split():
        if word in output:
            output[word] += 1
        else:
            output[word] = 1
    return output

print(word_count("the quick brown fox jumps over the lazy dog"))