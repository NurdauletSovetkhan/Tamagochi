import os
import time
import random

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 50
        self.mood = 70
        self.energy = 80

    def status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n👾 {self.name}'s Status:")
        print(f"❤️ Health: {self.health}")
        print(f"🍗 Hunger: {self.hunger}")
        print(f"😊 Mood: {self.mood}")
        print(f"⚡ Energy: {self.energy}")
        print("-" * 20)

    def eat(self):
        foods = ["🍎 яблоко", "🍔 бургер", "🍣 суши", "🌮 тако", "🥗 салат", "🍩 пончик"]
        food = random.choice(foods)
        effect = random.randint(10, 30)
        self.hunger = max(0, self.hunger - effect)
        self.mood += random.randint(5, 15)
        print(f"{self.name} съел {food}! Это восстановило {effect} сытости.")
        self.show_animation("ЕСТЬ")
        time.sleep(2)

    def play_game(self):
        games = ["⚽ футбол", "🎮 видеоигры", "🧩 пазлы"]
        game = random.choice(games)
        effect = random.randint(15, 25)
        if self.energy >= 20:
            self.mood += effect
            self.energy -= random.randint(10, 20)
            print(f"{self.name} играл в {game}! Это подняло настроение на {effect}.")
            self.show_animation("ИГРАТЬ")
        else:
            print(f"{self.name} слишком устал для {game}.")
        time.sleep(2)

    def sleep(self):
        print(f"{self.name} сладко засыпает... 🛌")
        self.show_animation("СПАТЬ")
        self.energy = min(100, self.energy + random.randint(20, 40))
        self.health += random.randint(5, 15)
        time.sleep(3)

    def tick(self):
        self.hunger += random.randint(5, 15)
        self.mood -= random.randint(5, 10)
        if self.hunger > 100:
            self.health -= random.randint(5, 15)
        elif self.hunger > 70:
            self.mood -= random.randint(5, 10)
        if self.mood < 20:
            self.health -= random.randint(5, 10)

    def is_alive(self):
        return self.health > 0

    def show_animation(self, action):
        frames = {
            "ЕСТЬ": ["(>^_^<)", "(>o_o<)", "(>n_n<)"],
            "ИГРАТЬ": ["o(^_^)o", "\\(^_^)/", "/(^_^)\\"],
            "СПАТЬ": ["[zZz]", "[ Zz ]", "[  Z ]"]
        }
        for frame in frames[action]:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{self.name} делает действие: {frame}")
            time.sleep(0.5)

# Основная функция
def main():
    name = input("Как назовем твоего питомца? 🐾: ")
    pet = Tamagotchi(name)

    while pet.is_alive():
        pet.status()
        print("1. Покормить\n2. Поиграть\n3. Положить спать\n4. Пропустить ход")
        choice = input("Выбери действие: ")

        if choice == '1':
            pet.eat()
        elif choice == '2':
            pet.play_game()
        elif choice == '3':
            pet.sleep()
        else:
            print("Пропуск хода...")

        pet.tick()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"💀 {pet.name} больше не с нами...")

if __name__ == "__main__":
    main()
