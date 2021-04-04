def separator():
    print("----------------------------------------")


def start_game():
    a = input("Let's start? Enter y or n (yes or no):\n")
    separator()
    if a == "y":
        print("Great! Let's go!")
        separator()
    elif a == "n":
        print("See you! See you again! Thank you!")
        separator()
    else:
        print("Incorrect input! Enter, please, y or n and push enter(yes or no)")
        separator()
        return start_game()
    return a


def clear_field():
    print(" ", 0, 1, 2)
    for i, line in enumerate(game_field):
        print(i, *line)


def user_move():
    print("Look to the field and enter digits of your moving.")
    separator()
    while True:
        try:
            x = int(input("Enter the number of line: "))
            y = int(input("Enter the number of column: "))
            break
        except ValueError:
            print("Incorrect input.")
            return user_move()
    if x < 3 and y < 3 and game_field[x][y] == "-":
        move = [x, y]
        return move
    else:
        separator()
        print("Incorrect input or this cell is busy.")
        return user_move()


def draw_xo(move, n):
    if n == 1:
        game_field[move[0]][move[1]] = "x"
    elif n == 2:
        game_field[move[0]][move[1]] = "o"


def check_win(game_field):
    for i in range(3):
        if game_field[i][0] == game_field[i][1] == game_field[i][2] == "x" or \
                game_field[0][i] == game_field[1][i] == game_field[2][i] == "x" or\
                game_field[0][0] == game_field[1][1] == game_field[2][2] == "x" or\
                game_field[0][0] == game_field[1][1] == game_field[2][2] == "x" or\
                game_field[0][2] == game_field[1][1] == game_field[2][0] == "x":
            return "x"
        elif game_field[i][0] == game_field[i][1] == game_field[i][2] == "o" or \
                game_field[0][i] == game_field[1][i] == game_field[2][i] == "o" or \
                game_field[0][0] == game_field[1][1] == game_field[2][2] == "o" or \
                game_field[0][0] == game_field[1][1] == game_field[2][2] == "o" or \
                game_field[0][2] == game_field[1][1] == game_field[2][0] == "o":
            return "o"


def main_logic_game():
    print("Hi! It's the game 'Tic tac toe'.")
    separator()
    print("This is an empty field. You're playing together. The first player is 'x'.")
    clear_field()
    separator()
    start_game()
    clear_field()
    counter = 0

    while True:

        print("The first player('x')!")
        draw_xo(user_move(), 1)
        clear_field()
        separator()
        counter += 1
        if counter == 9:
            print("Draw! Thank you!")
            print("Let's play again? Press Ctrl+Shift+F10")
            separator()
            separator()
            break
        win = check_win(game_field)
        if win == "x":
            print("'x' win! Thank you!")
            print("Let's play again? Press Ctrl+Shift+F10")
            separator()
            separator()
            break

        print("The second player('o')!")
        draw_xo(user_move(), 2)
        clear_field()
        separator()
        win = check_win(game_field)
        counter += 1
        if win == "o":
            print("'o' win! Thank you!")
            print("Let's play again? Press Ctrl+Shift+F10")
            separator()
            separator()
            break


game_field = [["-" for i in range(3)] for i in range(3)]
main_logic_game()
