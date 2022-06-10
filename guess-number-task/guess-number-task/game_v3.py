"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import re
from tkinter import N
import numpy as np


def random_predict(number: int = 20) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # number = np.random.randint(1.101)#getting the number
    
    count = 0
    p = 0 "p=0 if predict_number < 20, p=1 if 20<predict_number<40 and so on"
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    count+=1
    
    def search_code_20(*args) -> int:
        num = 0
        num = round(number/2) + p*20
        nonlocal count 
        if num == predict_number:
            count+=1
            return count
        elif num > predict_number:
            while True:
                count += 1
                num -= 1
                if num == predict_number:
                    break  # выход из цикла если угадали
        else:
            while True:
                count += 1
                num += 1
                if num == predict_number:
                    break  # выход из цикла если угадали
        return count
    
    if number == predict_number:
        return count
    elif number > predict_number:
        search_code_20(p=0)
    elif 40 == predict_number:
        count+=1
        return count
    elif 40 < predict_number:
        search_code_20(p=1)
    elif 60 == predict_number:
        count+=1
        return count
    elif 60 < predict_number:
        search_code_20(p=2)
    elif 80 == predict_number:
        count+=1
        return count
    elif 80 < predict_number:
        search_code_20(p=3)
    elif 100 == predict_number:
        count+=1
        return count
    else:
        search_code_20(p=4)
        
    return count 
        
        # count+=1
        # number = round(number/2)
        # if number == predict_number:
        #     count+=1
        #     return count
        # elif number > predict_number:
        #     while True:
        #         count += 1
        #         number -= 1
        #         if number == predict_number:
        #             break  # выход из цикла если угадали
        # else:
        #     while True:
        #         count += 1
        #         number += 1
        #         if number == predict_number:
        #             break  # выход из цикла если угадали
    
                
    #     if number < predict_number:
    #         number+=1      
            
    # while True:
    #     count += 1
        
    #     if number == predict_number:
    #         break  # выход из цикла если угадали
    #     count+=1
    #     if number < predict_number:
    #         number+=1
    #     else:
    #         number = round(number/2)
    #     count+=1
            
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

