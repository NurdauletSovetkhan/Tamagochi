from blessed import Terminal
import time

term = Terminal()
print(term.clear + term.green("Привет! Это Tamagotchi!"))

for i in range(5, 0, -1):
    print(term.move_xy(0, 2) + term.cyan(f"Игрок сделает ход через {i}..."), end="\n")
    time.sleep(1)

print(term.move_xy(0, 4) + term.bold_red("Игра началась!"))
