def removeadjacentDuplicate():
    str1 = "aabbbccdeabccdcdcdcllll"
    output = ""
    size = len(str1)

    for i in range(size):

        if i != 0:
            if(str1[i] == str1[i-1]):
                continue
            else:
                output += str1[i]
        else:
            output += str1[i]

    print(output)

removeadjacentDuplicate()