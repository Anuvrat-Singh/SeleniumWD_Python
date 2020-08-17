def product(inputList, size):
    outputList = []
    prod = 0
    for i in range(size):
        if i == size - 2:
            prod = inputList[i+1] * inputList[0]
            outputList.append(prod)
        elif i == size -1:
            prod = inputList[0] * inputList[1]
            outputList.append(prod)
        else:
            prod = inputList[i+1] * inputList[i+2]
            outputList.append(prod)

    print(outputList)


inputList = list(map(int, input("Enter the array of int space seperated: ").split()))
size = len(inputList)

if size < 3:
    print("Incorrect Input. Enter at least 3 elements.")
else:
    product(inputList, size)
#[1,2,3,4,5] ----->>>>>>> [6,12,20,5,2]
#[1,2,3] ---->>> [6,3,2]
