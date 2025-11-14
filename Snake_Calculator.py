import tkinter as tk
from tkinter import messagebox, simpledialog
import math

# =============================
# Snake Calculator - Full UI Version - v2
# =============================

root = tk.Tk()
root.title("Snake Calculator UI")
root.geometry("500x600")
root.config(bg="#1e1e1e")

# ---------- Functions ----------

def do_arithmetic():
    try:
        count = simpledialog.askinteger("Arithmetic", "How many numbers?")
        if count is None or count < 1:
            return
        op = simpledialog.askstring("Operator", "Choose +, -, *, /")
        if op not in ['+', '-', '*', '/']:
            messagebox.showerror("Invalid", "Invalid operator")
            return
        result = None
        for i in range(count):
            num = simpledialog.askfloat("Number", f"Enter number {i+1}:")
            if num is None:
                return
            if result is None:
                result = num
            else:
                if op == '+': result += num
                elif op == '-': result -= num
                elif op == '*': result *= num
                elif op == '/': result /= num
        messagebox.showinfo("Result", f"Answer: {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def do_sqrt():
    n = simpledialog.askfloat("Square Root", "Enter number:")
    if n is not None:
        messagebox.showinfo("Result", math.sqrt(n))


def do_exponent():
    base = simpledialog.askfloat("Exponent", "Base:")
    power = simpledialog.askfloat("Exponent", "Power:")
    if base is not None and power is not None:
        messagebox.showinfo("Result", base ** power)


def do_fraction_decimal():
    num = simpledialog.askfloat("Fraction", "Numerator:")
    den = simpledialog.askfloat("Fraction", "Denominator:")
    if num is None or den in [None, 0]:
        return
    messagebox.showinfo("Decimal", num / den)


def do_cube_root():
    n = simpledialog.askfloat("Cube Root", "Enter number:")
    if n is not None:
        messagebox.showinfo("Cube Root", n ** (1/3))


def do_abs():
    n = simpledialog.askfloat("Absolute Value", "Enter number:")
    if n is not None:
        messagebox.showinfo("Result", abs(n))


def do_factorial():
    n = simpledialog.askinteger("Factorial", "Enter integer:")
    if n is not None:
        messagebox.showinfo("Result", math.factorial(n))


def do_log():
    base = simpledialog.askfloat("Log Base", "Base:")
    expo = simpledialog.askfloat("Log", "Exponent:")
    if base and expo:
        messagebox.showinfo("Result", math.log(expo, base))


def do_floor_div():
    a = simpledialog.askinteger("Floor Division", "Dividend:")
    b = simpledialog.askinteger("Floor Division", "Divisor:")
    if a and b:
        messagebox.showinfo("Result", a // b)


def do_area():
    shape = simpledialog.askstring("Area", "Square or Triangle?")
    if not shape:
        return
    if shape.lower() == "square":
        s = simpledialog.askfloat("Square", "Side length:")
        messagebox.showinfo("Result", s * s)
    elif shape.lower() == "triangle":
        b = simpledialog.askfloat("Triangle", "Base:")
        h = simpledialog.askfloat("Triangle", "Height:")
        messagebox.showinfo("Result", (b * h) / 2)


def do_perimeter():
    count = simpledialog.askinteger("Perimeter", "Number of sides:")
    if not count:
        return
    total = 0
    for i in range(count):
        side = simpledialog.askfloat("Side", f"Side {i+1}:")
        if side: total += side
    messagebox.showinfo("Perimeter", total)


def do_sine():
    angle = simpledialog.askfloat("Sine", "Angle in degrees:")
    if angle is not None:
        messagebox.showinfo("Sine", math.sin(math.radians(angle)))


def do_triangle_angle():
    a = simpledialog.askfloat("Triangle", "Angle 1:")
    b = simpledialog.askfloat("Triangle", "Angle 2:")
    if a and b:
        messagebox.showinfo("Angle", 180 - (a + b))


def do_gcf():
    a = simpledialog.askinteger("GCF", "First number:")
    b = simpledialog.askinteger("GCF", "Second number:")
    if a and b:
        messagebox.showinfo("GCF", math.gcd(a, b))


def do_line_equation():
    x1 = simpledialog.askfloat("Line", "x1:")
    y1 = simpledialog.askfloat("Line", "y1:")
    x2 = simpledialog.askfloat("Line", "x2:")
    y2 = simpledialog.askfloat("Line", "y2:")
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return

    if x2 - x1 == 0:
        messagebox.showinfo("Line", f"Vertical line: x = {x1}")
        return

    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    sign = " + " if b >= 0 else " - "
    messagebox.showinfo("Line", f"y = {m}x{sign}{abs(b)}")


def do_rounding():
    n = simpledialog.askfloat("Rounding", "Number:")
    if n is None:
        return
    mode = simpledialog.askstring("Rounding", "1=int, 2=0.1, 3=0.01, 4=0.001")
    if mode == '1': r = round(n, 0)
    elif mode == '2': r = round(n, 1)
    elif mode == '3': r = round(n, 2)
    elif mode == '4': r = round(n, 3)
    else:
        messagebox.showerror("Invalid", "Not a valid option.")
        return
    messagebox.showinfo("Rounded", r)

# ---------- UI Buttons ----------

btns = [
    ("Arithmetic", do_arithmetic),
    ("Square Root", do_sqrt),
    ("Exponents", do_exponent),
    ("Fraction to Decimal", do_fraction_decimal),
    ("Cube Root", do_cube_root),
    ("Absolute Value", do_abs),
    ("Factorial", do_factorial),
    ("Logarithm", do_log),
    ("Floor Division", do_floor_div),
    ("Area", do_area),
    ("Perimeter", do_perimeter),
    ("Sine", do_sine),
    ("Triangle Angle", do_triangle_angle),
    ("GCF", do_gcf),
    ("Line Equation", do_line_equation),
    ("Rounding", do_rounding)
]

for text, cmd in btns:
    tk.Button(root, text=text, command=cmd, height=2, width=25, bg="#2d2d2d", fg="white").pack(pady=5)

root.mainloop()
