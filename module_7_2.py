def custom_write(file_name, strings):
    number_strings = 0 # счетчик строк
    list_text = [] # список для текста из info
    list_number = [] # список для кортежей с номером строки и байта
    for i in strings: # цикл для перебора элементов strings
        file = open(file_name, 'a', encoding='utf-8')  # открыли файл
        byte_beginning_string = file.tell()
        list_text.append(i)
        file.write(f'{i}\n')
        number_strings += 1
        tuple_ = (number_strings,) + (byte_beginning_string,)
        list_number.append(tuple_)
        strings_positions = dict(zip(list_number, list_text))
        file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
        ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
