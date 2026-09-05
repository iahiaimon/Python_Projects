from tkinter import *
from tkinter.ttk import *
import random


class Gamebox:

    def __init__(self, master=None):
        self.master = master

        self.player_boxes = set()
        self.computer_boxes = set()

        self.game_over = False

        self.create()

    def create(self):
        self.canvas = Canvas(
            self.master,
            bg="white"
        )

        cell_size = 120

        self.all_boxes = []
        self.box_coordinates = {}

        for row in range(3):
            for col in range(3):

                x1 = 70 + (col * cell_size)
                y1 = 80 + (row * cell_size)

                x2 = x1 + cell_size
                y2 = y1 + cell_size

                box = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    outline="black",
                    fill="white",
                    width=2
                )

                self.all_boxes.append(box)

                self.box_coordinates[box] = (
                    x1, y1, x2, y2
                )

                self.canvas.tag_bind(
                    box,
                    "<Button-1>",
                    lambda event, box=box:
                    self.box_clicked(event, box)
                )

        self.canvas.pack(fill=BOTH, expand=1)
        
        self.restart_button = Button(
        self.master,
        text="Restart",
        command=self.restart_game
    )

        self.restart_button.pack(pady=10)

    # PLAYER CLICK

    def box_clicked(self, event, box):

        if self.game_over:
            return

        # Already occupied
        if box in self.player_boxes or box in self.computer_boxes:
            return

        # Player X
        self.player_boxes.add(box)

        self.draw_x(box)

        # Check player win
        if self.check_winner(self.player_boxes):

            self.game_over = True

            self.show_message("You Win! 🎉")
            return

        # Check draw
        if len(self.player_boxes) + len(self.computer_boxes) == 9:

            self.game_over = True

            self.show_message("Draw!")
            return

        # Computer thinks for 1 second
        self.master.after(500, self.computer_move)

    # DRAW X

    def draw_x(self, box):

        x1, y1, x2, y2 = self.box_coordinates[box]

        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        size = 30

        self.canvas.create_line(
            center_x - size,
            center_y - size,
            center_x + size,
            center_y + size,
            width=4,
            fill="blue"
        )

        self.canvas.create_line(
            center_x + size,
            center_y - size,
            center_x - size,
            center_y + size,
            width=4,
            fill="blue"
        )

    # DRAW O

    def draw_o(self, box):

        x1, y1, x2, y2 = self.box_coordinates[box]

        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        size = 30

        self.canvas.create_oval(
            center_x - size,
            center_y - size,
            center_x + size,
            center_y + size,
            width=4,
            outline="red"
        )

    # COMPUTER MOVE

    def computer_move(self):

        if self.game_over:
            return

        empty_boxes = [
            box for box in self.all_boxes
            if box not in self.player_boxes
            and box not in self.computer_boxes
        ]

        if not empty_boxes:
            return

        # --------------------------------------------
        # First move: random corner/center
        # --------------------------------------------

        if len(self.player_boxes) == 0:

            box = random.choice(empty_boxes)

        else:

            # Minimax finds best move
            box = self.find_best_move()

        self.computer_boxes.add(box)

        self.draw_o(box)

        # Check computer win
        if self.check_winner(self.computer_boxes):

            self.game_over = True

            self.show_message("Computer Wins! 🤖")
            return

        # Check draw
        if len(self.player_boxes) + len(self.computer_boxes) == 9:

            self.game_over = True

            self.show_message("Draw!")
            return

    # FIND BEST MOVE

    def find_best_move(self):

        best_score = -float("inf")
        best_move = None

        empty_boxes = [
            box for box in self.all_boxes
            if box not in self.player_boxes
            and box not in self.computer_boxes
        ]

        for box in empty_boxes:

            self.computer_boxes.add(box)

            score = self.minimax(
                depth=0,
                is_maximizing=False
            )

            self.computer_boxes.remove(box)

            if score > best_score:

                best_score = score
                best_move = box

        return best_move

    # MINIMAX

    def minimax(self, depth, is_maximizing):

        # Computer wins
        if self.check_winner(self.computer_boxes):
            return 10 - depth

        # Player wins
        if self.check_winner(self.player_boxes):
            return depth - 10

        # Draw
        total_moves = (
            len(self.player_boxes)
            + len(self.computer_boxes)
        )

        if total_moves == 9:
            return 0

        # --------------------------------------------
        # COMPUTER = MAXIMIZER
        # --------------------------------------------

        if is_maximizing:

            best_score = -float("inf")

            empty_boxes = [
                box for box in self.all_boxes
                if box not in self.player_boxes
                and box not in self.computer_boxes
            ]

            for box in empty_boxes:

                self.computer_boxes.add(box)

                score = self.minimax(
                    depth + 1,
                    False
                )

                self.computer_boxes.remove(box)

                best_score = max(
                    best_score,
                    score
                )

            return best_score

        # --------------------------------------------
        # PLAYER = MINIMIZER
        # --------------------------------------------

        else:

            best_score = float("inf")

            empty_boxes = [
                box for box in self.all_boxes
                if box not in self.player_boxes
                and box not in self.computer_boxes
            ]

            for box in empty_boxes:

                self.player_boxes.add(box)

                score = self.minimax(
                    depth + 1,
                    True
                )

                self.player_boxes.remove(box)

                best_score = min(
                    best_score,
                    score
                )

            return best_score

    # WIN CHECK

    def check_winner(self, boxes):

        if len(boxes) < 3:
            return False

        # Convert boxes into positions
        positions = []

        for box in boxes:

            index = self.all_boxes.index(box)

            row = index // 3
            col = index % 3

            positions.append((row, col))

        # --------------------------------------------
        # Rows
        # --------------------------------------------

        for row in range(3):

            if all(
                (row, col) in positions
                for col in range(3)
            ):
                return True

        # --------------------------------------------
        # Columns
        # --------------------------------------------

        for col in range(3):

            if all(
                (row, col) in positions
                for row in range(3)
            ):
                return True

        # --------------------------------------------
        # Main diagonal
        # --------------------------------------------

        if all(
            (i, i) in positions
            for i in range(3)
        ):
            return True

        # --------------------------------------------
        # Other diagonal
        # --------------------------------------------

        if all(
            (i, 2 - i) in positions
            for i in range(3)
        ):
            return True

        return False

    # MESSAGE

    def show_message(self, message):

        self.canvas.create_text(
            250,
            40,
            text=message,
            font=("Arial", 20, "bold"),
            fill="green"
        )

    # RESTART GAME

    def restart_game(self):

        # Game state reset
        self.clicked_boxes.clear()
        self.computer_boxes.clear()

        self.game_over = False

        # Board-এর X, O এবং message remove
        self.canvas.delete("all")

        # Board আবার তৈরি
        self.create()


# MAIN


if __name__ == "__main__":

    master = Tk()

    shape = Gamebox(master)

    master.title("Tic Tac Toe")

    master.geometry("500x600")

    master.resizable(False, False)

    mainloop()
