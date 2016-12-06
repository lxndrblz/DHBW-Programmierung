#encoding=utf-8
def encode(s):
    previous = s[0]
    amount = 1
    encoded = ""
    for i in range(1, len(s)):
        if s[i] == previous:
            amount += 1
        else:

            encoded +=str(amount) + previous
            previous = s[i]
            amount = 1

    #Results from last iteration
    encoded += str(amount) + previous
    return encoded

def decode(s):
    amount = ""
    output = ""
    for char in s:
        if char.isdigit() == True:
            amount += char
        else:
            output += char*int(amount)
            amount = ""
    return output
print(encode("AAAAAAAAAABBBBBCCCCCCCCCC"))
print(decode("10A3B10C"))