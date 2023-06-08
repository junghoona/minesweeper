from tkinter import Button, Label
import random 
import settings


class Cell: 
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_obj = None 
    
    def __init__(self, x, y, is_mine=False): 
        self.is_mine = is_mine 
        self.is_opened = False 
        self.cell_btn_obj= None 
        self.x = x
        self.y = y
        
        # Append the object to the Cell.all list 
        Cell.all.append(self) 
    
    def create_btn(self, location): 
        btn = Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.left_click_actions)     # Left Click 
        btn.bind('<Button-3>', self.right_click_actions)    # Right Click
        self.cell_btn_obj = btn 
    
    # Decorator for use case of the class, not every instance 
    @staticmethod 
    def create_cell_count_label(location): 
        lbl = Label(
            location, 
            bg='black', 
            fg='white',
            text=f"Cells Left: {Cell.cell_count}",
            font=("", 30) 
        )
        Cell.cell_count_label_obj = lbl 
    
    def left_click_actions(self, event): 
        if self.is_mine: 
            self.show_mine() 
        else: 
            if self.surrounded_cells_mines_length == 0: 
                for cell_btn_obj in self.surrounded_cells: 
                    cell_btn_obj.show_cell() 
            self.show_cell()
    
    def get_cell_by_axis(self, x, y): 
        # Return a cell object based on values of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y: 
                return cell 
    
    @property
    def surrounded_cells(self): 
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1), 
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        
        cells = [cell for cell in cells if cell is not None]
        return cells 
    
    @property 
    def surrounded_cells_mines_length(self): 
        counter = 0 
        for cell in self.surrounded_cells: 
            if cell.is_mine: 
                counter += 1 
        return counter 
    
    def show_cell(self): 
        if not self.is_opened:
            Cell.cell_count -= 1 
            self.cell_btn_obj.config(text=self.surrounded_cells_mines_length)
            # Replace the text of cell count label with the newer count 
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.config(
                    text=f"Cells Left: {Cell.cell_count}",
                )
        # Mark the cell as opened (Use this as the last line of this method) 
        self.is_opened = True 
    
    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost
        self.cell_btn_obj.config(bg='red') 
    
    def right_click_actions(self, event): 
        print(event) 
        print("I am right clicked!")
    
    
    @staticmethod
    def randomize_mines(): 
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for cells in picked_cells: 
            cells.is_mine = True 
    
    
    # Method to change the way object is represented 
    def __repr__(self): 
        return f"Cell({self.x}, {self.y})"
    