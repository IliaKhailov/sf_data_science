import numpy as np
# print(np.iinfo(np.int16))
# # print(len(np.sctypeDict))
# # print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
# # a = np.uint8(-456)
# # print(a)
# # arr = np.array([1,2,3,4,5])
# # print(arr.dtype)
# # print(np.finfo(np.float32))
# arr, step = np.linspace(-6,21,60, endpoint=False, retstep=True)
# print(step)
# np.random.seed(1)
# print(np.random.randint(10, size = 3))
# print(np.random.randint(10, size = 3))
# print(np.random.randint(10, size=3))

# # Не забудьте импортировать numpy и сразу задать seed 2021
# import numpy as np
# np.random.seed(2021)


# # В simple сохранте случайное число в диапазоне от 0 до 1
# simple = np.random.rand()

# # Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# # в переменную randoms
# randoms = np.random.uniform(-150, 2021, size=120)

# # Получите массив из случайных целых чисел от 1 до 100 (включительно)
# # из 3 строк и 2 столбцов. Сохраните результат в table
# table = np.random.randint(1, 101, size=(3,2))

# # В переменную even сохраните четные числа от 2 до 16 (включительно)
# even = np.random.choice(np.arange(2,17), size=4, replace = False)

# # Перемешайте числа в even так, чтобы массив even изменился
# np.random.shuffle(even)


# # Получите из even 3 числа без повторений. Сохраните их в переменную select
# select = np.random.choice(even, size=3, replace = False)

# # Получите переменную triplet, которая должна содержать перемешанные
# # значения из массива select (сам select измениться не должен)
# triplet = np.random.permutation(select)

# a1 = np.zeros((5,5))
# a1[::2,1::2]=1
# a1[1::2,::2]=1
# # a1[1::2,:]=1


# print(a1)
# from numpy import uint32

# a = np.random.randint(4294967295,size=(1,), dtype = np.uint32)
# # print(np.uinfo(a))
# np.random.seed(a)
# print(np.random.permutation(array))
 

simplelist = [19, 242, 14, 152, 142, 1000]
simplelist = np.int32(simplelist)
print(np.mean(simplelist))