def test(user_input, size):
    dict1 = {}

    for i in range(size):
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    # stored freq in dict1

    for k,v in dict1.items():
        if v >= 2:
            print("Duplicate key is: " + k + " frequency: " + v)

    set1 = set(user_input)
    for j in {1,2,3,4,5}:
        if j not in set1:
            print("Missing value is: " + str(j))


user_input = list(map(int, input().split()))
size = len(user_input)
test(user_input, size)