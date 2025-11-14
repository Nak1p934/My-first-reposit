naprov = input("Шифровать или дешефровать? (Ш/Д):\n")
language = input("Выберите язык (en/ru):\n")
r = input("Шаг известен? (Да/Нет)\n")
if r == "Да":
    step = int(input("Введите шаг:\n"))
soo = input("Введите текст:\n")
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def deshif(a, step, lang):
    if lang == "en":
        for i in range(len(a)):
            if a[i].isalpha() and a[i].islower():
                print(eng_lower_alphabet[((eng_lower_alphabet.index(a[i])) - step) % 26], end = "")
            elif a[i].isalpha() and a[i].isupper():
                print(eng_upper_alphabet[((eng_upper_alphabet.index(a[i])) - step) % 26], end = "")
            else:
                print(a[i], end = "")
        print("\n")
    elif lang == "ru":
        for j in range(len(a)):
            if a[j].isalpha() and a[j].islower():
                print(rus_lower_alphabet[((rus_lower_alphabet.index(a[j])) - step) % 32], end = "")
            elif a[j].isalpha() and a[j].isupper():
                print(rus_upper_alphabet[((rus_upper_alphabet.index(a[j])) - step) % 32], end = "")
            else:
                print(a[j], end = "")
        print("\n")
def shif(a, step, lang):
    if lang == "en":
        for i in range(len(a)):
            if a[i].isalpha() and a[i].islower():
                print(eng_lower_alphabet[(eng_lower_alphabet.index(a[i]) + step) % 26], end = "")
            elif a[i].isalpha() and a[i].isupper():
                print(eng_upper_alphabet[(eng_upper_alphabet.index(a[i]) + step) % 26], end = "")
            else:
                print(a[i], end = "")
        print("\n")
    elif lang == "ru":
        for rushif in range(len(a)):
            if a[rushif].isalpha() and a[rushif].islower():
                print(rus_lower_alphabet[((rus_lower_alphabet.index(a[rushif])) + step) % 32], end = "")
            elif a[rushif].isalpha() and a[rushif].isupper():
                print(rus_upper_alphabet[((rus_upper_alphabet.index(a[rushif])) + step) % 32], end = "")
            else:
                print(a[rushif], end = "")
        print("\n")
if r == "Да":
    if naprov == 'Д':
        deshif(soo, step, language)
    elif naprov == "Ш":
        shif(soo, step, language)
else:
    if language == "en":
        for f in range(1, 27):
            deshif(soo, f, language)
    elif language == "ru":
        for f in range(1, 33):
            deshif(soo, f, language)