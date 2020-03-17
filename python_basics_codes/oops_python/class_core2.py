# raising manual error

class lenMismatchError(Exception):
    """ Raise when length of list after split of input string is not equal two """

def error_print():
    len_val = 2
    while True:
        try:
            temp = input("Enter the name and tweet separated by space : ").strip().split()
            if len(temp)!=2:
                raise lenMismatchError
            else:
                break
        except lenMismatchError:
            print('Please enter the test input in proper format.')
    print(temp)

error_print()
