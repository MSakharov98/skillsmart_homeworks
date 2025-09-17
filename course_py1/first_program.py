'''Данная функция ищет вхождение подстроки в строку.** Сначала найдем "точку входа" подстроки – 
где первый первый ее символ совпадает с одним из символов строки. Как только нашли – 
проверяем на совпадение остальные символы. Если все успешно – функция вернет True, если нет 
– функция будет искать следующую "точку входа". 
По условия задачи нельзя использовать дополнительные инструменты, поэтому 
написана функция my_len() для определения длины строки и подстроки.'''

def my_len(string):
    count = 0 # счетчик
    try:
        while True:
            string[count] # обращение по индексу
            count += 1 
    except IndexError:
        return count
    

def is_substring_in_string(substring, string):
    for i in range(len(string)):
            for j in range(len(substring)):
                if (i + j) >= len(string) or string[i + j] != substring[j]:
                    break
            else:
                return True
    return False

string = 'смотрим на число три, написанное... на счете тридцать три она закрыла глаза...'
substring = 'тридцать три она '
print(is_substring_in_string(substring, string))
print(is_substring_in_string('23', '12345'))