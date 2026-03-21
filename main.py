import tkinter as tk
import random
import math

def random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def make_blob(canvas, center_x, center_y, r, points=12):
    blob_points = []
    for i in range(points):
        angle = i * 2 * math.pi / points
        radius = r * random.uniform(0.7, 1.3)
        px = center_x + radius * math.cos(angle)
        py = center_y + radius * math.sin(angle)
        blob_points.extend([px, py])
    canvas.create_polygon(blob_points, fill=random_color(), smooth=True, outline="")

    eye_img = tk.PhotoImage(file="eye.png")
    resize_factor = random.randint(3, 5)
    eye_img = eye_img.subsample(resize_factor, resize_factor)
    if not hasattr(canvas, 'images'): canvas.images = []
    canvas.images.append(eye_img)
    canvas.create_image(center_x + random.randint(-r // 2, r // 2),center_y + random.randint(-r // 2, r // 2), image=eye_img)


root = tk.Tk()
root.title("Blob Generator")
canvas_width = 800
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

center_x = canvas_width // 2
center_y = canvas_height // 2


def next_blob():
    canvas.delete("all")
    make_blob(canvas, center_x, center_y, r=100, points=20)
btn = tk.Button(root, text="Next Blob", command=lambda: next_blob())
btn.pack()

root.mainloop()