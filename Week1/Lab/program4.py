def main():
    player1 = input("Player 1: Enter R for rock, P for paper or S for scissors: ")
    player1 = player1.lower()
    player2 = input("Player 2: Enter R for rock, P for paper or S for scissors: ")
    player2 = player2.lower()

    if (len(player1) > 1 or len(player2) > 1):
        print("That's not a choice")
        return

    if player1 == player2:
        print("DRAW!")
        return

    if player1 == "s":
        if player2 == "r":
            print("PLAYER 2 WINS")
        else:
            print("PLAYER 1 WINS")

    if player1 == "p":
        if player2 == "s":
            print("PLAYER 2 WINS")
        else:
            print("PLAYER 1 WINS")

    if player1 == "r":
        if player2 == "p":
            print("PLAYER 2 WINS")
        else:
            print("PLAYER 1 WINS")


if __name__ == "__main__":
    main()
