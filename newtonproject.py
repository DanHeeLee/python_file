import tkinter as tk

# 초기화
root = tk.Tk()
root.title("가속도의 법칙 시뮬레이션")

# 색상
black = "black"
white = "white"

# 화면 크기
width, height = 800, 600

# 공 초기 설정
ball_radius = 20
initial_x = width // 4
ball1_x, ball2_x = initial_x, 3 * width // 4
ball_y = height // 2
ball1_speed_x, ball2_speed_x = 0, 0

# 질량 설정
mass1, mass2 = 2, 8

# 사용자가 가하는 힘 초기화
user_force1, user_force2 = 0, 0

# Canvas 생성
canvas = tk.Canvas(root, width=width, height=height, bg=black)
canvas.pack()

def apply_force1():
    global user_force1
    user_force1 = float(entry1.get())

def apply_force2():
    global user_force2
    user_force2 = float(entry2.get())

def restart():
    global ball1_x, ball2_x, ball1_speed_x, ball2_speed_x, user_force1, user_force2
    ball1_x, ball2_x = initial_x, 3 * width // 4
    ball1_speed_x, ball2_speed_x = 0, 0
    user_force1, user_force2 = 0, 0

# 가하는 힘 입력 창 생성
label1 = tk.Label(root, text="첫 번째 공에 가하고 싶은 힘:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
button1 = tk.Button(root, text="적용", command=apply_force1)
button1.pack()

label2 = tk.Label(root, text="두 번째 공에 가하고 싶은 힘:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
button2 = tk.Button(root, text="적용", command=apply_force2)
button2.pack()

# 다시 시작 버튼
restart_button = tk.Button(root, text="다시 시작", command=restart)
restart_button.pack()

# 주 흐름
def update():
    global ball1_x, ball2_x, ball1_speed_x, ball2_speed_x
    a1 = user_force1 / mass1
    a2 = user_force2 / mass2
    ball1_speed_x += a1
    ball2_speed_x += a2
    ball1_x += ball1_speed_x
    ball2_x -= ball2_speed_x

    canvas.delete("all")
    canvas.create_oval(ball1_x - ball_radius, ball_y - ball_radius, ball1_x + ball_radius, ball_y + ball_radius, fill=white)
    # 두 번째 공의 크기를 키웁니다.
    canvas.create_oval(ball2_x - 1.5 * ball_radius, ball_y - 1.5 * ball_radius, ball2_x + 1.5 * ball_radius, ball_y + 1.5 * ball_radius, fill=white)

    root.after(16, update)  # 약 60 FPS로 업데이트

root.after(0, update)
root.mainloop()
