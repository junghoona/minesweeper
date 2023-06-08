from tkinter import * 
from cell import Cell 
import settings
import utils


root = Tk() 

# Ovverride the settings of the window 
root.config(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black', # Change later
    width=settings.WIDTH, 
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame( 
    root,
    bg='black', 
    width=utils.width_prct(25),
    height=utils.height_prct(75),
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root, 
    bg='black', 
    width=utils.width_prct(75),
    height=utils.height_prct(75),
)
center_frame.place(
    x=utils.width_prct(25), 
    y=utils.height_prct(25), 
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE): 
        c = Cell(x, y)
        c.create_btn(center_frame)
        c.cell_btn_obj.grid(
            column=x, row=y
        )
# Call the label from the Cell class 
Cell.create_cell_count_label(left_frame) 
Cell.cell_count_label_obj.place(
    x=0, y=0 
)

Cell.randomize_mines()

# Run the window 
root.mainloop()