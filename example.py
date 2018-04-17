from ttt import TicTacToe

game = TicTacToe(X="Bob", O="ai")

while not game.game_over():
    test = input(">>> ")
    game.play("Bob", test)
    print(game.print_board())
    # test = input(">>> ")
    value = game.play("ai", test)
    print("AI picked {}".format(value))
    print(game.print_board())

print(game.print_board())
print(game.winner + " is the winner")

