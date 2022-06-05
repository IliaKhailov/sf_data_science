""" our game give us oportunity to find a random number"""

import numpy as np

# number = np.random.randint(1.101)#getting the number
# count=0

# while True:
#     predict_number=int(input("give a number from 1 to 100:  "))
#     count+=1
#     if predict_number > number:
#         print("the mumber has to be smaller")
#     elif predict_number < number:
#         print("the mumber has to be bigger")
#     else:
#         print(f"you got the right number {number} in {count} tries!")
#         break
def random_predict(number:int=1) ->int:
    

