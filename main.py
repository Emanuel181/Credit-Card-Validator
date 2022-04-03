def checkInput(str):
    for i in str:
        if not i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return 0
    return 1



def convertToInt(str):
    return [int(i) for i in str]



def checkLen(str):
    if len(str) < 13 or len(str) > 16:
        return 0



def checkFirstDigit(str):
    if (str[0] != '4' and str[0] != '5' and str[0] != '6' and (str[0] != '3' and str[1] != '7')):
        return 0



def evenIndicesSum(str):
    evenSum = 0

    for i in range(len(str) - 2, -1, -2):
        if i >= 0:
            str[i] *= 2
            if(str[i] > 9):
                str[i] = int((str[i] % 10) + (str[i] / 10))
            evenSum += str[i]

    return evenSum



def oddIndicesSum(str):
    oddSum = 0

    for i in range(len(str) - 1, -1, -2):
        if i > -1:
            oddSum += str[i]

    return oddSum



def check(str):

    str = convertToInt(str)

    if(checkLen(str) and checkFirstDigit(str) == 0):
        return 0

    return (((evenIndicesSum(str) + oddIndicesSum(str)) % 10) == 0)





str = input("\nIntroduceti numarul cardului: ")
print()
checkInput = checkInput(str)

if(checkInput == 0):
    print("Trebuie introdus un sir de cifre !(Input neacceptat)")

else:
    ok = check(str)

    if(ok):
        print("Cardul este valid")
    else:
        print("Cardul nu este valid")
