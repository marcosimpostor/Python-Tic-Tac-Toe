import tkinter, random

time = [0]

turn = [1]

grid = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

def create_click_handler(row, col):
    def button_click():
        number = row * 3 + col + 1
        grid_place = (number) - 1
        if time[0] < 9:
            if turn[0] == 1:
                if grid[grid_place] == 0:
                    buttons[row][col].config(text="❌")
                    window.title("🔵's turn")
                    turn[0] = 0
                    grid[grid_place] = 1
                    time[0] += 1
            else:
                if grid[grid_place] == 0:
                    buttons[row][col].config(text="🔵")
                    window.title("❌'s turn")
                    turn[0] = 1
                    grid[grid_place] = 2
                    time[0] += 1
        has_someone_won()
    return button_click

def choose_randomly():
    global grid, turn, time
    if time[0] < 9:
        time[0] += 1
        random_button = random.choice(grid)
        empty_indices = [i for i, val in enumerate(grid) if val == 0]
        if empty_indices:
            random_index = random.choice(empty_indices)
            row = random_index // 3
            col = random_index % 3
            button = buttons[row][col]
            if grid[random_index] == 0:
                if turn[0] == 1:
                    random_button = 1
                    turn = [2]
                    for i in range(3):
                        for j in range(3):
                            button.config(text="❌")
                    grid[random_index] = 1
                else:
                    random_button = 2
                    turn = [1]
                    for i in range(3):
                        for j in range(3):
                            button.config(text="🔵")
                    grid[random_index] = 2
        has_someone_won()


def has_someone_won():
    if grid[0] == 1 and grid[1] == 1 and grid[2] == 1 or \
       grid[3] == 1 and grid[4] == 1 and grid[5] == 1 or \
       grid[6] == 1 and grid[7] == 1 and grid[8] == 1:
        window.title("❌ won!")
        time[0] = 9
    elif grid[0] == 2 and grid[1] == 2 and grid[2] == 2 or \
         grid[3] == 2 and grid[4] == 2 and grid[5] == 2 or \
         grid[6] == 2 and grid[7] == 2 and grid[8] == 2:
        window.title("🔵 won!")
        time[0] = 9
    elif grid[0] == 1 and grid[3] == 1 and grid[6] == 1 or \
         grid[1] == 1 and grid[4] == 1 and grid[7] == 1 or \
         grid[2] == 1 and grid[5] == 1 and grid[8] == 1:
        window.title("❌ won!")
        time[0] = 9
    elif grid[0] == 2 and grid[3] == 2 and grid[6] == 2 or \
         grid[1] == 2 and grid[4] == 2 and grid[7] == 2 or \
         grid[2] == 2 and grid[5] == 2 and grid[8] == 2:
        window.title("🔵 won!")
        time[0] = 9
    elif grid[0] == 1 and grid[4] == 1 and grid[8] == 1 or \
         grid[2] == 1 and grid[4] == 1 and grid[6] == 1:
        window.title("❌ won!")
        time[0] = 9
    elif grid[0] == 2 and grid[4] == 2 and grid[8] == 2 or \
         grid[2] == 2 and grid[4] == 2 and grid[6] == 2:
        window.title("🔵 won!")
        time[0] = 9
    elif grid[0] != 0 and grid[1] != 0 and grid[2] != 0 and grid[3] != 0 and grid[4] != 0 and grid[5] != 0 and grid[6] != 0 and grid[7] != 0 and grid[8] != 0:
        window.title("Tie!")

def reset_game():
    global time, turn, grid
    time = [0]
    turn = [1]
    grid[0] = 0
    grid[1] = 0
    grid[2] = 0
    grid[3] = 0
    grid[4] = 0
    grid[5] = 0
    grid[6] = 0
    grid[7] = 0
    grid[8] = 0
    window.title("❌'s turn")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

window = tkinter.Tk()
window.title("❌'s turn")
window.minsize(300, 300)

buttons = []

for i in range(3):  # rows
    row = []
    for j in range(3):  # columns
        random_click = choose_randomly
        button_click_handler = create_click_handler(i, j)
        button = tkinter.Button(window, command=button_click_handler, text="")
        button.grid(row=i, column=j, sticky="nsew")
        row.append(button)
    buttons.append(row)
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)
reset_button = tkinter.Button(window, text="Reset", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)
random_button = tkinter.Button(window, text="Random", command=random_click)
random_button.grid(row=4, column=0, columnspan=3)
window.mainloop()