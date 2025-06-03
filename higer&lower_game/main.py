import art
from game_data import data
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

score = 0
game_should_continiue = True

while game_should_continiue:
    clear()
    print(art.logo)
    
    if score > 0:
        print(f"You're right! Current score: {score}")

    # Выбираем два разных аккаунта
    account1 = random.choice(data)
    account2 = random.choice(data)

    # Убеждаемся, что аккаунты не одинаковые
    while account1 == account2:
        account2 = random.choice(data)

    # Показываем игроку информацию
    print(f"Compare A: {account1['name']}, a {account1['description']}, from {account1['country']}")
    print(art.vs)
    print(f"Against B: {account2['name']}, a {account2['description']}, from {account2['country']}")

    # Функция сравнения
    def compare(a1, a2):
        if a1['follower_count'] > a2['follower_count']:
            return 'A'
        else:
            return 'B'

    # Получаем правильный ответ
    correct_answer = compare(account1, account2)

    # Ввод от пользователя
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Проверяем
    if user_answer == correct_answer:
        score += 1
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
