import tkinter as tk
import random
from tkinter import messagebox
 
class NumberBaseballGame:
    def __init__(self, master):
        self.master = master
        self.master.title("숫자 야구 게임")
        self.secret_number = self.generate_secret_number()
        print(self.secret_number)
        self.attempts = 0

        self.label = tk.Label(master, text="숫자를 입력하세요:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="확인", command=self.check_guess)
        self.submit_button.pack()

    def generate_secret_number(self):
        return random.sample(range(1, 10), 3)

    def check_guess(self):
        guess = self.entry.get()
        if len(guess) != 3 or not guess.isdigit():
            messagebox.showwarning("경고", "3자리 숫자를 입력하세요.")
            return

        guess = [int(digit) for digit in guess]
        self.attempts += 1
        result = self.calculate_result(guess)

        if result == (3, 0):
            messagebox.showinfo("정답", f"축하합니다! {self.attempts}번 시도 후 정답을 맞추셨습니다.")
            self.master.destroy()
        else:
            messagebox.showinfo("결과", f"시도 {self.attempts}: {result[0]}스트라이크, {result[1]}볼")

    def calculate_result(self, guess):
        strikes = sum(1 for i in range(3) if guess[i] == self.secret_number[i])
        balls = sum(1 for digit in guess if digit in self.secret_number) - strikes
        return strikes, balls

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberBaseballGame(root)
    root.mainloop()
