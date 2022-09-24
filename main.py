
board_scale = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in board_scale:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(board_scale)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if board_scale[move] == ' ':
            board_scale[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if board_scale['7'] == board_scale['8'] == board_scale['9'] != ' ':  # across the top
                printBoard(board_scale)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board_scale['4'] == board_scale['5'] == board_scale['6'] != ' ':  # across the middle
                printBoard(board_scale)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board_scale['1'] == board_scale['2'] == board_scale['3'] != ' ':  # across the bottom
                printBoard(board_scale)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board_scale['1'] == board_scale['4'] == board_scale['7'] != ' ':  # down the left side
                printBoard(board_scale)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board_scale['2'] == board_scale['5'] == board_scale['8'] != ' ':  # down the middle
                printBoard(board_scale)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board_scale['3'] == board_scale['6'] == board_scale['9'] != ' ':  # down the right side
                printBoard(board_scale)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board_scale['7'] == board_scale['5'] == board_scale['3'] != ' ':  # diagonal
                printBoard(board_scale)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif board_scale['1'] == board_scale['5'] == board_scale['9'] != ' ':  # diagonal
                printBoard(board_scale)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board_scale[key] = " "

        game()


if __name__ == "__main__":
    game()