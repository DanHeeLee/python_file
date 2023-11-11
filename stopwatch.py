import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("스톱워치")

        self.running = False
        self.elapsed_time = 0
        self.start_time = 0
        self.lap_times = []
        self.lap_count = 0

        self.time_label = tk.Label(root, text="0:00.000", font=("Arial", 30))
        self.start_button = tk.Button(root, text="시작", command=self.start)
        self.pause_button = tk.Button(root, text="일시정지", command=self.pause)
        self.reset_button = tk.Button(root, text="리셋", command=self.reset)
        self.lap_button = tk.Button(root, text="랩 타임", command=self.record_lap)

        self.lap_listbox = tk.Listbox(root, height=10)
        self.lap_listbox.pack()

        self.time_label.pack()
        self.start_button.pack()
        self.pause_button.pack()
        self.reset_button.pack()
        self.lap_button.pack()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update()

    def pause(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.lap_times = []
        self.lap_count = 0
        self.update()
        self.lap_listbox.delete(0, tk.END)
        self.time_label.config(text="0:00.000")  # 타이머를 0으로 초기화

    def record_lap(self):
        if self.running:
            lap_time = time.time() - self.start_time
            self.lap_count += 1
            self.lap_times.append(lap_time)
            self.lap_listbox.insert(tk.END, f"랩 {self.lap_count}: {self.format_time(lap_time)}")

            if self.lap_count >= 10:  # 랩 기록 창이 10개 이상이면 스크롤 다운
                self.lap_listbox.yview_moveto(1)

    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.time_label.config(text=self.format_time(self.elapsed_time))
            self.time_label.after(10, self.update)  # 10ms마다 업데이트

    def format_time(self, elapsed_time):
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 1000) % 1000)
        return f"{minutes}:{seconds:02d}.{milliseconds:03d}"

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
