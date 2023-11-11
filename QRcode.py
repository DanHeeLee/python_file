import tkinter as tk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    link = entry.get()
    
    if link:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.img = img_tk  # Tkinter에서 이미지 유지

        result_label.config(text="QR 코드 생성 완료!")
    else:
        result_label.config(text="링크를 입력하세요!")

def save_qr_code():
    img = Image.open("qrcode.png")
    img.save("qrcode_saved.png")
    result_label.config(text="QR 코드 저장 완료!")

# Tkinter GUI 생성
root = tk.Tk()
root.title("QR 코드 생성기")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="링크 입력:")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

generate_button = tk.Button(root, text="QR 코드 생성", command=generate_qr_code)
generate_button.pack()

save_button = tk.Button(root, text="QR 코드 저장", command=save_qr_code)
save_button.pack()

result_label = tk.Label(root, text="", fg="green")
result_label.pack()

qr_label = tk.Label(root)
qr_label.pack()

root.mainloop()
