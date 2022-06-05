import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) ->int:
    """finding out the mean number of tries in 1000 games

    Args:
        random_predict (_type_): finding out function

    Returns:
        int: mean number of tries
    """
    count_ls=[]
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score=int(np.mean(count_ls))
    print(f"your algoritm mean tries is {score}")
    return(score)
# RUN
if __name__=='__main__':
    score_game(random_predict)