from collections import Counter
from operator import itemgetter

class LenMismatchError(Exception):
    """ Raise when length of list after split of input string is not equal two """

def finding_no_of_tweets(name_list):
    """ This will give the name of user with maximum number of tweets"""
    counter_dict = Counter(name_list)
    max_val = max(counter_dict.values())
    name_list = [ key for key, val in counter_dict.items() if val==max_val ]
    name_list.sort()
   
    return name_list, max_val
    
def taking_user_ip():
    """ This will take user input for number of test cases,
        number of tweets and space separed user input of 
        name and tweet for test case """
    while True:
        try:
            no_of_test_case = int(input("Enter the number of test cases : ").strip())
            break
        except ValueError as e:
            print(f"Please give integer input : {e}")

    for _ in range(no_of_test_case):
        name_list = []

        while True:
            try:
                no_of_tweets = int(input(f"Enter the number of tweets for test case {_+1}: ").strip())
                break
            except ValueError as e:
                print(f"Please give integer input : {e}")

        for _ in range(no_of_tweets):
            while True:
                try: 
                    temp = input("Enter name and tweet number with a space in between : ").strip().split()
                    if len(temp) !=2:
                        raise LenMismatchError 
                    else:
                        name_list.append(temp[0])
                        break
                except LenMismatchError as e:
                    print("You have entered the name and tweer_id in wrong format")

        names, cnt = finding_no_of_tweets(name_list)

        for _ in names:
            print(f"{_} \t {cnt}")
    
    return name_list



if __name__=="__main__":
    name = taking_user_ip()
    finding_no_of_tweets(name)