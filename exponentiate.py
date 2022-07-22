from time import sleep

while True:
    usableBase = False
    usableTime = False
    retryConfirmed = False

    while usableBase == False: 
        try:
            base = float(input("Input a base: ")); usableBase = True
        except ValueError:
            print("Error code 1: illegal input - contains unconvertable characters")
    while usableTime == False:
        try:
            exponentTimes = float(input("Input a maximum exponentation: ")); usableTime = True
            if exponentTimes == 0: print("Error code 2: illegal input - exponent cannot be zero"); usableTime = False
        except ValueError:
            print("Error code 1: illegal input - contains unconvertable characters")

    print("")
    def exponentiate(base,exponent):
        return base ** exponent

    if exponentTimes > 0:
        exponent = 1
        while exponent <= exponentTimes:
            print(int(exponentiate(base,exponent)), " [", exponent, "]")
            exponent += 1
            sleep(0.2)
    else:
        exponent = -1
        while exponent >= exponentTimes:
            print(exponentiate(base,exponent), " [", exponent, "]")
            exponent -= 1
            sleep(0.2)

    sleep(0.7); print("")
    while retryConfirmed == False:
        retryConfirmation = input("Would you like to use this exponentiation calculator again? (y/n) ")
        if any(x in retryConfirmation.lower() for x in ['n','no']): quit()
        elif any(x in retryConfirmation.lower() for x in ['y','ye','yes']): retryConfirmed = True
        else: print("Error code 3: incorrect input - must contain: [case-insensitive]"); print("  Deny: 'n', 'no' | Affirm: 'y', 'ye', 'yes'")