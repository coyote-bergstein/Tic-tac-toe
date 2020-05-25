#!/usr/bin/env python3
class Game:
    def __init__(self):
        self.matrix = [["_", "_", "_"],
                       ["_", "_", "_"],
                       ["_", "_", "_"]]
        self.column = 0
        self.row = 0
        self.character_turn = "X"
        self.winner = None      # It's take 4 values None, X, O, draw.

    def input_coordinates(self, row="-1", column="-1"):
        if not row.isdigit() or not column.isdigit():
            print("You should enter numbers!")
        else:
            column = int(column) - 1
            row = int(row) - 1
            if column < 0 or column > 2 or row < 0 or row > 2:
                print("Coordinates should be from 1 to 3!")
            elif self.matrix[row][column] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                self.column = column
                self.row = row
                self.insert_sign()

    def insert_sign(self):
        self.matrix[self.row][self.column] = self.character_turn
        self.change_turn()
        self.check_game_status()

    def check_game_status(self):
        # This part checks arrangement vertical and horizontal
        for coordinate in range(3):
            if self.matrix[0][coordinate] == self.matrix[1][coordinate] == self.matrix[2][coordinate]:
                if self.matrix[0][coordinate] != "_":
                    self.winner = self.matrix[0][coordinate]
            if self.matrix[coordinate].count("X") == 3 or self.matrix[coordinate].count("O") == 3:
                if self.matrix[coordinate][0] != "_":
                    self.winner = self.matrix[coordinate][0]

        # This check cross arrangement
        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]:
            if self.matrix[0][0] != "_":
                self.winner = self.matrix[0][0]
        if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0]:
            if self.matrix[0][2] != "_":
                self.winner = self.matrix[0][2]

        if "_" not in self.matrix[0] and "_" not in self.matrix[1] and "_" not in self.matrix[2]:
            self.winner = "draw"

    def change_turn(self):
        if self.character_turn == "X":
            self.character_turn = "O"
        else:
            self.character_turn = "X"

    def draw(self):
        battlefield = "---------\n"
        for row in range(3):
            for column in range(3):
                if column == 0:
                    battlefield += "| "
                battlefield += f"{self.matrix[row][column]} "
                if column == 2:
                    battlefield += "|\n"
        battlefield += "---------"
        print(battlefield)
    
    def play(self):
        while self.winner is None:
            self.draw()
            self.input_coordinates(*input().split(maxsplit=1))
            self.check_game_status()
        self.draw()
        if self.winner == "draw":
            print(self.winner)
        else:
            print(self.winner, "wins")


tic_tac_toe = Game()
tic_tac_toe.play()
