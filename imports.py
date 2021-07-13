from functions import calculate_tip, letter_grade as grade
import itertools
from math import factorial
import json

data = json.load(open('profiles.json'))

active_users = 0
inactive_users = 0
all_balances = 0
min_balance = 10**6
max_balance = 0
fruits = dict()
all_unread = 0

for u in data:

    if u['isActive']:
        active_users += 1
    else:
        inactive_users += 1
    
    bal = float(u['balance'].replace(",","")[1:])
    fruit = u['favoriteFruit']

    all_balances += bal
    if bal < min_balance:
        min_balance = bal
    if bal > max_balance:
        max_balance = bal

    if fruit in fruits.keys():
        fruits[fruit] += 1
    else:
        fruits[fruit] = 1

    g = u['greeting']
    #weird way of returning last number in the string
    all_unread += int(''.join([c for c in g if c.isnumeric()])[-1])

total_users = active_users + inactive_users
avg_balance = all_balances / total_users
# I know
commonest_fruit =  'strawberry'
strangest_fruit = 'apple'

if __name__ == '__main__':
    print(calculate_tip(.1,9800))
    print(grade(99))

	#720 permutations of 6-char string (6!)
    print(len(list(itertools.permutations('abc123'))))
    print(factorial(6))

    #4 choose 2: 4!/2! = 12
    print(len(list(itertools.permutations('abcd',2))))
    #when order doesn't matter: 4!/(2!*2!) = 6
    print(len(list(itertools.combinations('abcd',2))))

    print("\nProfile questions")
    print(str(active_users) + " active")
    print(str(inactive_users) + " inactive")
    print(str(total_users) + " total")
    print(str(all_balances) + " all")
    print(str(avg_balance) + " avg")
    print(str(min_balance) + " min")
    print(str(max_balance) + " max")
    print(str(commonest_fruit) + " common fruit")
    print(str(strangest_fruit) + " rare fruit")
    print(str(all_unread) + " unread msg")

