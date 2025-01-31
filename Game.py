# import random

# def create_grid(size):
#     grid = [' ' for _ in range(size)]
#     treasure_index = random.randint(0, size - 1)
#     bomb_index = random.randint(0, size - 1)
    
#     # Убедимся, что клад и бомба не находятся в одной ячейке
#     while bomb_index == treasure_index:
#         bomb_index = random.randint(0, size - 1)
    
#     grid[treasure_index] = 'T'  # T for Treasure
#     grid[bomb_index] = 'B'      # B for Bomb
#     return grid

# def display_grid(grid):
#     print("Current grid:")
#     for i in range(len(grid)):
#         print(f"{i}: {grid[i]}")
#     print()

# def main():
#     size = 10
#     grid = create_grid(size)
#     attempts = 0
#     found = False

#     print("Welcome to the Treasure Hunt Game!")
#     print("Dig in the grid to find the treasure (T) or the bomb (B).")
    
#     while attempts < 5 and not found:
#         display_grid(grid)
#         try:
#             choice = int(input("Choose a cell to dig (0-9): "))
#             if grid[choice] == 'T':
#                 print("Congratulations! You found the treasure!")
#                 found = True
#             elif grid[choice] == 'B':
#                 print("Boom! You hit a bomb. Game over.")
#                 found = True
#             else:
#                 print("Nothing here. Keep digging!")
#                 grid[choice] = 'X'  # Mark the dug cell
#                 attempts += 1
#         except (ValueError, IndexError):
#             print("Invalid choice. Please choose a number between 0 and 9.")

#     if not found:
#         print("You've used all your attempts! Better luck next time.")
#         display_grid(grid)

# if __name__ == "__main__":
#     main()


# import random

# def игра():
#     ячейки = 10
#     клад = random.randint(0, ячейки - 1)
#     бомба = random.randint(0, ячейки - 1)
#     while бомба == клад:
#         бомба = random.randint(0, ячейки - 1)

#     попытки = 10

#     print("Добро пожаловать в игру 'Копай и находи'!")
#     print("У Вас есть 10 попытки, чтобы найти клад или наткнуться на бомбу.")

#     for _ in range(попытки):
#         выбор = int(input(f"Выберите ячейку от 0 до {ячейки - 1}: "))

#         if выбор == клад:
#             print("Поздравляю! Вы нашли клад!")
#             break
#         elif выбор == бомба:
#             print("Ой! Вы наткнулись на бомбу! Игра окончена.")
#             break
#         else:
#             print("Здесь ничего нет. Попробуйте снова.")
#     else:
#         print("Вы исчерпали все попытки. Игра окончена.")

# игра()



# Игра "Крестики-нолики"

def печать_полей(поле):
    for строка in поле:
        print(" | ".join(строка))
        print("-" * 9)

def проверка_победы(поле):

    for строка in поле:
        if строка[0] == строка[1] == строка[2] != " ":
            return строка[0]

    for кол in range(3):
        if поле[0][кол] == поле[1][кол] == поле[2][кол] != " ":
            return поле[0][кол]
        
    if поле[0][0] == поле[1][1] == поле[2][2] != " ":
        return поле[0][0]
    if поле[0][2] == поле[1][1] == поле[2][0] != " ":
        return поле[0][2]
    return None

def игра():
    поле = [[" " for _ in range(3)] for _ in range(3)]
    текущий_игрок = "X"
    количество_ходов = 0

    while True:
        печать_полей(поле)
        строка = int(input(f"Игрок {текущий_игрок}, введите номер строки (0-2): "))
        кол = int(input(f"Игрок {текущий_игрок}, введите номер столбца (0-2): "))

        if поле[строка][кол] == " ":
            поле[строка][кол] = текущий_игрок
            количество_ходов += 1

            победитель = проверка_победы(поле)
            if победитель:
                печать_полей(поле)
                print(f"Игрок {победитель} победил!")
                break
            if количество_ходов == 9:
                печать_полей(поле)
                print("Ничья!")
                break

            текущий_игрок = "O" if текущий_игрок == "X" else "X"
        else:
            print("Эта клетка уже занята, попробуйте снова.")

if __name__ == "__main__":
    игра()