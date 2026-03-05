#Написать скрипт, который выводит на экран «True», если элементы программно задаваемого списка представляют собой возрастающую последовательность, иначе – «False».
numbers = [1, 3, 5, 7, 9]
is_ascending = True
for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        is_ascending = False
        break 
# Выводим результат (True или False)
print(is_ascending)