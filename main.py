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

c1 = Cell() 
c1.create_btn(center_frame)
c1.cell_btn.place(
    x=0, y=0 
)

c2 = Cell() 
c2.create_btn(center_frame) 
c2.cell_btn.place(
    
)

# # Buttons 
# btn1 = Button(
#     center_frame, 
#     bg='blue',
#     text='First Button',
# )
# btn1.place(x=0, y=0)

# Run the window 
root.mainloop()