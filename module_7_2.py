def custom_write(file_name, strings):
    number_strings = 0  # счетчик строк
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')  # открыли файл
    for i in strings:  # цикл для перебора элементов strings
        byte_beginning_string = file.tell()
        number_strings += 1
        strings_positions.update({((number_strings,) + (byte_beginning_string,)): i})
        file.write(f'{i}\n')
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
