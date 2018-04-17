from ttt import TicTacToe

game = TicTacToe(X="Bob", O="John")

while not game.game_over():
    test = input(">>> ")
    game.play("Bob", test)
    print(game.print_board())
    test = input(">>> ")
    game.play("John", test)
    print(game.print_board())

print(game.print_board())
print(game.winner + " is the winner")

