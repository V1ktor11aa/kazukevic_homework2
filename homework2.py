# Artur Kazukevich 
# Date: 12/10/2023 
# Description: Homework 2 
# Grodno IT Academy Python 3.10 
 
# Объяснение работы с функциями: 
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3) 
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем) 
 
# оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов 
# нельзя менять названия функций/файлов/входные данные. Можно менять решение, менять/добавлять return. 
 
# пример названия репозитория для гитхаба: kazukevich_homework2 
# добавьте в репозиторий с домашним задание файл readme.md с датой сдачи, фамилией и именем выполнившего и кратким 
# описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown 
 
 
# Напишите программу, ĸоторая считает общую цену. 
# Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара. 
# Посчитайте общую цену в рублях и ĸопейĸах за l товаров. 
# Уточнение: 
# Используйте функцию return чтобы ответ был в рублях и копейках. 
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров" 
 
# * Для одного из тестов нужно применять какую-то библиотеку =) 
 
def common_price(m, n, s, l): 
    if ...: 
        return False 
 
    return "Общая цена составляет " + str(a) + " рублей и " + str(v) + " копеек за " + str(d) + " товаров" 
 
 
 
# Даны: три стороны треугольника. 
# Требуется: проверить, действительно ли это стороны треугольника. 
# Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных. 
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321 
# Если нет, вывести False. 
# Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник. 
 
 
def triangle(a, b, c): 
    return False 
 
 
# Найти самое длинное слово в введенном предложении. 
# Учтите что в предложении могут быть знаки препинания. 
# Пример: если введено "This is a sample sentence where the longest word is in the middle!", 
# то надо вернуть "sentence" 
def longest_word(sentence): 
    return False 
 
 
# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. 
# Например, если было введено "abc cde def", то должно быть выведено "abcdef". 
def uniques(repeating_string): 
    return False 
 
 
# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. 
# Проверка рассчитана только на английские буквы. 
def count_string_capitalization(mixed_string): 
    return False