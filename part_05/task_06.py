# Напишите программу, удаляющую из текста все слова содержащие "абв"

init_text = 'Напишитеабв программу, удаляющуюабв из текста всеабв слова содержащие "абв"'

result_list = [i for i in init_text.split(' ') if 'абв' not in i]

print(init_text)
print(' '.join(result_list))
