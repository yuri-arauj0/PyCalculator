import decimal
decimal.getcontext().prec = 1000

def doTheMath():
    print('\n*********************************************')
    n1 = float(input('Enter one number: '))
    n2 = float(input('Enter another number: '))
    result = 0

    print('''
    Choose an operation:
    +  -> addition
    -  -> subtraction
    *  -> multiplication
    /  -> division
    %  -> modulo (division remains)
    ** -> power
        ''')

    operation = input('My choice: ')

    if operation == '+':
        result = n1 + n2 
        print('\n{} + {} = {}'.format(n1, n2, result))

    elif operation == '-':
        result = n1 - n2
        print('\n{} - {} = {}'.format(n1, n2, result))

    elif operation == '*':
        result = n1 * n2
        print('\n{} * {} = {}'.format(n1, n2, result))

    elif operation == '/':
        result = n1 / n2
        print('\n{} / {} = {}'.format(n1, n2, result))

    elif operation == '%':
        result = n1 % n2
        print('\n{} % {} = {}'.format(n1, n2, result))

    elif operation == '**':
        result = n1 ** n2
        print('\n{} ** {} = {}'.format(n1, n2, result))

    else:
        print('\nYou have not choosen an operation I\'m aware of. Please, run me again\n')

    goAgain()

# ======================== END OF THE MATH FUNCTION ======================== #

def goAgain():
    print('\n\nY for YES || N for NO')
    doItAgain = input('Wanna go again? ')

    if doItAgain.upper() == 'Y':
        doTheMath()
    elif doItAgain.upper() == 'N':
        print('\nAfter A While, Crocodile!')
        print('*********************************************\n')
    else:
        goAgain()

# ========================= END OF THE REPEAT FUNC ========================= #

doTheMath()