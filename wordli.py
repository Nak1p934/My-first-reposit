import random
word_list = ["солце", "море", "горы"]
a = random.choice(word_list)
ee = []
# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def play(a):
    word_completion = '_' * len(a)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 
    print("Давайте играть в угадайку слов")
    while not guessed and tries > 0:               
      print(display_hangman(tries))
      print(word_completion)
      b = input()
      if len(b) == 1 and b.isalpha():
         b = b.lower()
         if b in a and b not in guessed_letters:
            guessed_letters.append(b)
            print(f"Молодец, буква угаданна! Количество букв в слове:{a.count(b)}")
            ee.extend(word_completion)
            e = a.index(b)
            ee.insert(e, b)
            del ee[e + 1]
            word_completion = "".join(ee)
         elif b in guessed_letters:
            print("Вы уже вводили  жту букву")
         else:
            print("Данной буквы нет в слове")
            tries -= 1
      elif len(b) == len(a) and b.isalpha():
         b = b.lower
         if b == a:
            print(f"Ура, вы угодали слово: .{a}.        .{b}.")
            break
         else:
            print(f"Вы не угодали слово  .{a}.   .{b}.")
            tries -= 1
      else:
         print("Ошибка ввода попробуйте ещё раз. Нужно ввести букву или всё слово", a)

play(a)
