# tiac-tac-toe
A simple tic tac toe library

## Two possibilities
Two players:
```py
from ttt import TicTacToe

game = TicTacToe(X="Bob", O="John")

while not game.game_over():
    test = input(">>> ")
    while not game.validate(test):
        test = input(">>> ")
    game.play("Bob", test)
    print(game.print_board())
    test = input(">>> ")
    while not game.validate(test):
        test = input(">>> ")
    game.play("John", test)
    print(game.print_board())

print(game.print_board())
print(game.winner + " is the winner")
```

Alone against the AI:
```py
from ttt import TicTacToe

game = TicTacToe(X="Bob", O="ai")

while not game.game_over():
    test = input(">>> ")
    while not game.validate(test):
        test = input(">>> ")
    game.play("Bob", test)
    print(game.print_board())
    game.play("ai", test)
    print(game.print_board())

print(game.print_board())
print(game.winner + " is the winner")
```
