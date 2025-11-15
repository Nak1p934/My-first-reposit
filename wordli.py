import random
word_list = ["солце", "море", "горы"]
a = random.choice(word_list)
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
         if b in a:
               guessed_letters.append(b.upper())
               print(f"Молодец, буква угаданна! Количество букв в слове:{a.count(b)}")
play(a)