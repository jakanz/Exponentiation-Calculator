from time import sleep

while True:
    usableBase = False
    usableTime = False
    retryConfirmed = False

    while usableBase == False: 
        try:
            base = float(input("Input a base: ")); usableBase = True
            if '.' in str(base):
                if str(base).endswith('.0'): continue
                else:
                    print('')
                    print('! WARNING !  You inputted a decimal number. Due to utilization of floating point math,')
                    print('the result of the mathematics will inevitably degrade to rough approximations at best.')
                    print('')
                    continueConfirmed = False
                    while continueConfirmed == False:
                        continueConfirm = input('Would you still like to continue with the program? (y/n) ')
                        if any(x in continueConfirm.lower() for x in ['y','yes']):
                            print('Continuing program...'); print(''); continueConfirmed = True
                        elif any(x in continueConfirm.lower() for x in ['n','no']):
                            print('Restarting to base input...'); print(''); continueConfirmed = True; usableBase = False
                        else: print("Error code 3: incorrect input - must contain: [case-insensitive]"); print("  Deny: 'n', 'no' | Affirm: 'y', 'ye', 'yes'")
        except ValueError:
            print("Error code 1: illegal input - contains unconvertable characters"); print('')

    while usableTime == False:
        try:
            exponentTimes = float(input("Input a maximum exponentation: ")); usableTime = True
            if exponentTimes == 0: print("Error code 2: illegal input - exponent cannot be zero"); print(''); usableTime = False
            if '.' in str(exponentTimes):
                if str(exponentTimes).endswith('.0'): continue
                else:
                    print('')
                    print('! WARNING !  You inputted a decimal number. Due to utilization of floating point math,')
                    print('the result of the mathematics will inevitably degrade to rough approximations at best.')
                    print('')
                    continueConfirmed = False
                    while continueConfirmed == False:
                        continueConfirm = input('Would you still like to continue with the program? (y/n) ')
                        if any(x in continueConfirm.lower() for x in ['y','yes']):
                            print('Continuing program...'); print(''); continueConfirmed = True
                        elif any(x in continueConfirm.lower() for x in ['n','no']):
                            print('Restarting to exponent input...'); print(''); continueConfirmed = True; usableTime = False
                        else: print("Error code 3: incorrect input - must contain: [case-insensitive]"); print("  Deny: 'n', 'no' | Affirm: 'y', 'ye', 'yes'"); print('')
        except ValueError:
            print("Error code 1: illegal input - contains unconvertable characters"); print('')

    print("")
    def exponentiate(base,exponent):
        return base ** exponent

    if str(base).endswith('.0') and str(exponentTimes).endswith('.0'):
        if exponentTimes > 0:
            exponent = 1
            while exponent <= exponentTimes:
                print(int(exponentiate(base,exponent)), " [", exponent, "]")
                exponent += 1
                sleep(0.2)
        else:
            exponent = -1
            while exponent >= exponentTimes:
                print(int(exponentiate(base,exponent)), " [", exponent, "]")
                exponent -= 1
                sleep(0.2)
    else:
        if exponentTimes > 0:
            exponent = 1
            while exponent <= exponentTimes:
                print(exponentiate(base,exponent), " [", exponent, "]")
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