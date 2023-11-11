
import tkinter as tk
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageGrab, Image

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.master.title("그림판")

        self.canvas_width = 800
        self.canvas_height = 600
        self.brush_size = 2
        self.brush_color = "black"

        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.clear_button = tk.Button(master, text="지우기", command=self.save_image)
        self.clear_button.pack(pady=10)

        self.save_button = tk.Button(master, text="저장", command=self.save_image)
        self.save_button.pack(pady=10)

        self.color_button = tk.Button(master, text="색상 변경", command=self.change_color)
        self.color_button.pack(pady=10)

        self.brush_size_slider = tk.Scale(master, from_=1, to=10, orient="horizontal", label="브러시 크기", command=self.change_brush_size)
        self.brush_size_slider.pack(pady=10)

        self.init_button = tk.Button(master, text="초기화", command=self.init_settings)
        self.init_button.pack(pady=10)

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.brush_color, width=self.brush_size)
        self.last_x, self.last_y = x, y

    def clear_canvas(self):
        self.canvas.delete("all")

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def change_brush_size(self, size):
        self.brush_size = int(size)

    def init_settings(self):
        self.brush_size_slider.set(2)
        self.brush_color = "black"

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG files", "*.jpg")])
        # if file_path:
        #     ps_file = file_path + ".eps"
        #     self.canvas.postscript(file=ps_file, colormode='color')
        #     self.convert_ps_to_image(ps_file, file_path)
        self.canvas.postscript(file=file_path, colormode='color')

    def convert_ps_to_image(self, ps_file, image_file):
        image = Image.open(ps_file)
        image.save(image_file, "png")
        image.close()




if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
