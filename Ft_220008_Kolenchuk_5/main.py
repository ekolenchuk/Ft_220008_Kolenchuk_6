print('Введите текст:')
text = input()
text_length = len(text)

while True:
    try:
        step = int(input('Введите шаг сдвига (целое число):  '))
        break
    except ValueError:
        print("Вы ввели не целое число. Повторите ввод")

alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
            'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')
alphabet_upper_case = ('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
                       'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я')
alph_length = len(alphabet)


def key_transform(shift):
    if shift < 0:
        return alph_length + shift % alph_length
    else:
        return shift % alph_length


key = key_transform(step)
shifr = []
symbol = ''
for i in range(text_length):
    symbol = text[i]
    for j in range(alph_length):
        if text[i].isupper() and text[i] == alphabet_upper_case[j]:
            symbol = alphabet_upper_case[(j + key) % alph_length]
        elif text[i] == alphabet[j]:
            symbol = alphabet[(j + key) % alph_length]
    shifr.append(symbol)

print(''.join(shifr))
