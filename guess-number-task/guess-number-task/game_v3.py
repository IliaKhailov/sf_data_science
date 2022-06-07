"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

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
    
    predict_number = np.random.randint(1, 101)  # предполагаемое число

    while True:
        count += 1
        
        if number == predict_number:
            break  # выход из цикла если угадали
        count+=1
        if number < predict_number:
            number+=1
        else:
            number = round(number/2)
        count+=1
            
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