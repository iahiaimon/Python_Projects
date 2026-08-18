from tkinter import *
from tkinter.ttk import *


class Gamebox:
    def __init__(self, master=None):
        self.master = master
        self.clicked_boxes = set()
        self.create()

    def box_clicked(self, event, box, x1, y1, x2, y2):  

        if box in self.clicked_boxes:
            return

        self.clicked_boxes.add(box)

        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        size = 30

        self.canvas.create_line(
            center_x - size, center_y - size,
            center_x + size, center_y + size,
            width=4
        )

        self.canvas.create_line(
            center_x + size, center_y - size,
            center_x - size, center_y + size,
            width=4
        )

    def create(self):
        self.canvas = Canvas(self.master)

        # 3 x 3 Grid
        cell_size = 120

        for row in range(3):
            for col in range(3):
                x1 = 70 + (col * cell_size)
                y1 = 80 + (row * cell_size)

                x2 = x1 + cell_size
                y2 = y1 + cell_size

                box = self.canvas.create_rectangle(
                    x1, y1, x2, y2, outline="black", fill="white", width=2
                )

                self.canvas.tag_bind(box, "<Button-1>", lambda event, box=box, x1=x1, y1=y1, x2=x2, y2=y2:
        self.box_clicked(event, box, x1, y1, x2, y2))

        self.canvas.pack(fill=BOTH, expand=1)


if __name__ == "__main__":

    master = Tk()
    shape = Gamebox(master)

    master.title("Gamebox")
    master.geometry("500x600")

    mainloop()
