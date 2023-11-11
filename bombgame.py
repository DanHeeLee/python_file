import tkinter as tk
import random

BOARD_SIZE = 10

def initialize_board():
    global board, mines, flagged, clicked, game_over, total_mines
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    mines = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    flagged = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    clicked = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    game_over = False
    total_mines = random.randint(10, 20)
    place_mines()
    calculate_numbers()

def place_mines():
    for _ in range(total_mines):
        x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
        while mines[y][x]:
            x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
        mines[y][x] = True

def calculate_numbers():
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if not mines[y][x]:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < BOARD_SIZE and 0 <= y + dy < BOARD_SIZE and mines[y + dy][x + dx]:
                            board[y][x] += 1

def click(x, y):
    global game_over  # Declare game_over as a global variable
    if game_over or clicked[y][x] or flagged[y][x]:
        return

    if mines[y][x]:
        reveal_mines()
        game_over = True
        message_label.config(text="패배!")
    else:
        uncover(x, y)
        check_win()

def uncover(x, y):
    clicked[y][x] = True
    buttons[y][x].config(state="disabled", relief=tk.SUNKEN)
    if board[y][x] == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < BOARD_SIZE and 0 <= y + dy < BOARD_SIZE and not clicked[y + dy][x + dx]:
                    uncover(x + dx, y + dy)
    elif board[y][x] > 0:
        buttons[y][x].config(text=str(board[y][x]))

def reveal_mines():
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if mines[y][x]:
                buttons[y][x].config(text="X", state="disabled", relief=tk.SUNKEN)

def right_click(x, y):
    if not game_over and not clicked[y][x]:
        flagged[y][x] = not flagged[y][x]
        if flagged[y][x]:
            buttons[y][x].config(text="F")
        else:
            buttons[y][x].config(text="")

def check_win():
    if all(clicked[y][x] or mines[y][x] for x in range(BOARD_SIZE) for y in range(BOARD_SIZE)):
        game_over = True
        message_label.config(text="승리!")

def restart_game():
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            buttons[y][x].config(text="", state="normal", relief=tk.RAISED)
    initialize_board()
    message_label.config(text="지뢰 찾기")

app = tk.Tk()
app.title("지뢰 찾기")
initialize_board()

buttons = []
for y in range(BOARD_SIZE):
    row = []
    for x in range(BOARD_SIZE):
        button = tk.Button(app, width=4, height=2)
        button.grid(row=y, column=x)
        button.bind("<Button-1>", lambda event, x=x, y=y: click(x, y))
        button.bind("<Button-3>", lambda event, x=x, y=y: right_click(x, y))
        row.append(button)
    buttons.append(row)

restart_button = tk.Button(app, text="다시 시작", command=restart_game)
restart_button.grid(row=BOARD_SIZE, columnspan=BOARD_SIZE)

message_label = tk.Label(app, text="지뢰 찾기")
message_label.grid(row=BOARD_SIZE + 1, columnspan=BOARD_SIZE)

app.mainloop()
