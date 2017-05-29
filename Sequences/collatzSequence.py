#collatz sequence
def calculateCollatzSeq (num):
    while(num > 1):        
        if (num % 2 == 0):
            num //= 2

        else:
            num = (3 * num) + 1

        print('*' * num)

print('Enter an integer')
try:
    userInput = int(raw_input())
except ValueError:
    print("Invalid Input")
    
calculateCollatzSeq(userInput)
