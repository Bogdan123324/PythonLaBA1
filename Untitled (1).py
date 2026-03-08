#!/usr/bin/env python
# coding: utf-8

# In[1]:


def task1():
    try:
        s = input("Введите вещественное число: ").replace(',', '.')
        num = float(s)
        if num < 0:
            raise ValueError("Некорректный формат!")
        rub = int(num)
        kop = round((num - rub) * 100)
        print(f"{rub} руб. {kop:02d} коп.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    task1()


# In[2]:


def task2():
    lst = [1, 3, 5, 7, 9]  # пример, можно изменить
    is_ascending = all(lst[i] < lst[i+1] for i in range(len(lst)-1))
    print(is_ascending)

if __name__ == "__main__":
    task2()


# In[5]:


def task3():
    card = input("Введите номер карты (16 цифр): ").replace(" ", "")
    if not card.isdigit() or len(card) != 16:
        print("Некорректный номер!")
        return
    hidden = f"{card[:4]} **** **** {card[-4:]}"
    print(hidden)

if __name__ == "__main__":
    task3()


# In[6]:


def task4():
    text = input("Введите текст: ")
    words = text.split()
    long = [w for w in words if len(w) > 7]
    medium = [w for w in words if 4 <= len(w) <= 7]
    short = [w for w in words if len(w) < 4]
    print("Слова длиннее 7 символов:", *long)
    print("Слова от 4 до 7 символов:", *medium)
    print("Остальные:", *short)

if __name__ == "__main__":
    task4()


# In[23]:


import re

def task5():
    text = input("Введите предложение: ")
    # разбиваем на слова и разделители (пробелы, запятые)
    parts = re.split(r'(\W+)', text)
    result = []
    for part in parts:
        if part and part[0].isalpha() and part[0].isupper():
            result.append(part.upper())
        else:
            result.append(part)
    print(''.join(result))

if __name__ == "__main__":
    task5()


# In[26]:


def task6():
    text = input("Введите текст: ")
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    unique = [ch for ch, cnt in freq.items() if cnt == 1]
    print("Символы, встречающиеся один раз:", ''.join(unique))

if __name__ == "__main__":
    task6()


# In[28]:


def task7():
    addresses = [
        "www.example",
        "google.com",
        "www.site.net",
        "yandex.ru",
        "www.news.org"
    ]
    processed = [
        (("http://" + addr) if addr.startswith("www") else addr) +
        (".com" if not addr.endswith(".com") else "")
        for addr in addresses
    ]
    print(processed)

if __name__ == "__main__":
    task7()


# In[29]:


import random
import math

def task8():
    n = random.randint(1, 10000)
    arr = [random.randint(0, 100) for _ in range(n)]
    # ближайшая степень двойки сверху
    next_pow2 = 1 << (n - 1).bit_length()  # или 2**math.ceil(math.log2(n))
    arr.extend([0] * (next_pow2 - n))
    print(f"n = {n}, размер после дополнения: {len(arr)}")
    # print(arr)  # раскомментировать для просмотра

if __name__ == "__main__":
    task8()


# In[31]:


def task9():
    available = {1000: 10, 500: 10, 100: 10, 50: 10, 10: 10}
    amount = int(input("Введите сумму: "))
    remaining = amount
    result = []
    for nominal in sorted(available.keys(), reverse=True):
        if remaining <= 0:
            break
        max_count = available[nominal]
        need = remaining // nominal
        if need > 0:
            count = min(need, max_count)
            if count > 0:
                result.append(f"{count}*{nominal}")
                remaining -= count * nominal
    if remaining != 0:
        print("Операция не может быть выполнена!")
    else:
        print(" + ".join(result))

if __name__ == "__main__":
    task9()


# In[33]:


def task10():
    password = input("Введите пароль: ")
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    if score <= 2:
        print("Ненадежный пароль")
    elif score <= 3:
        print("Средней надежности")
    else:
        print("Надежный пароль")

if __name__ == "__main__":
    task10()


# In[34]:


def frange(start, stop, step):
    if step == 0:
        raise ValueError("step не может быть нулевым")
    if step > 0:
        while start < stop:
            yield round(start, 10)  # округление для избежания накопления ошибок
            start += step
    else:
        while start > stop:
            yield round(start, 10)
            start += step

# Пример использования
if __name__ == "__main__":
    for x in frange(1, 5, 0.1):
        print(x)


# In[35]:


def get_frames(signal, size, overlap):
    step = int(size * (1 - overlap))
    if step <= 0:
        raise ValueError("Слишком большое перекрытие (step <= 0)")
    for i in range(0, len(signal) - size + 1, step):
        yield signal[i:i+size]

# Пример
if __name__ == "__main__":
    signal = list(range(100))
    for frame in get_frames(signal, size=10, overlap=0.5):
        print(frame)


# In[36]:


def extra_enumerate(iterable):
    total = sum(iterable)
    cum = 0
    for i, elem in enumerate(iterable):
        cum += elem
        frac = cum / total if total != 0 else 0
        yield i, elem, cum, round(frac, 3)  # округлим для красоты

# Пример
if __name__ == "__main__":
    x = [1, 3, 4, 2]
    for i, elem, cum, frac in extra_enumerate(x):
        print(elem, cum, frac)


# In[37]:


def non_empty(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            return [item for item in result if item not in ('', None)]
        return result
    return wrapper

@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1']

if __name__ == "__main__":
    print(get_pages())


# In[38]:


def pre_process(a=0.97):
    def decorator(func):
        def wrapper(s):
            processed = s[:]
            for i in range(1, len(processed)):
                processed[i] = processed[i] - a * processed[i-1]
            return func(processed)
        return wrapper
    return decorator

@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)

if __name__ == "__main__":
    signal = [10, 20, 30, 40, 50]
    plot_signal(signal)


# In[39]:


import random
import itertools
from datetime import datetime, timedelta

def task16():
    teams = [
        "Спартак", "Зенит", "ЦСКА", "Локомотив",
        "Краснодар", "Ростов", "Динамо", "Рубин",
        "Уфа", "Арсенал", "Крылья Советов", "Оренбург",
        "Сочи", "Тамбов", "Ахмат", "Урал"
    ]
    random.shuffle(teams)
    groups = [teams[i*4:(i+1)*4] for i in range(4)]

    print("Группы:")
    for i, group in enumerate(groups, 1):
        print(f"Группа {i}: {', '.join(group)}")

    # Генерация всех матчей (внутри каждой группы)
    matches = []
    for group in groups:
        for match in itertools.combinations(group, 2):
            matches.append(match)

    # Начальная дата: 14 сентября 2016, среда
    start_date = datetime(2016, 9, 14, 22, 45)  # время 22:45
    print("\nКалендарь игр:")
    for i, match in enumerate(matches):
        game_date = start_date + timedelta(weeks=2*i)
        date_str = game_date.strftime("%d/%m/%Y, %H:%M")
        print(f"{match[0]} — {match[1]}: {date_str}")

if __name__ == "__main__":
    task16()


# In[ ]:




