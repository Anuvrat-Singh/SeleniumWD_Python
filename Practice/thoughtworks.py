def arrange():
    testCases = int(input("No. of test cases: "))
    for i in range(testCases):
        size = int(input("Enter the no. of integers in array: "))
        inputList = []
        dict = {}
        for j in range(size):
            inputList.append(int(input()))

        if size%2 == 0:
        #   firstHalf = size/2
        #   for i in range(size):
            for i in range(size):
                if inputList[i] in dict:
                    dict[inputList[i]] += 1
                else:
                    dict[inputList[i]] = 1
            flag = False
            for v in dict.values():
                if v % 2 != 0:
                    flag = False
                    print("No... input cant be rearranged")
                    break
                else:
                    flag = True

            if flag == True:
                print("Yes, input can be arranged")

        else:
            print("No... the array cant be arranged.")


arrange()