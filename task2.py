import matplotlib.pyplot as plt
import math

def draw_pythagoras_tree(x, y, angle, length, level):
    if level == 0:
        return
    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)
    plt.plot([x, x2], [y, y2], color='brown')
    new_length = length * math.sqrt(2) / 2
    angle_left = angle + math.pi / 4
    angle_right = angle - math.pi / 4
    draw_pythagoras_tree(x2, y2, angle_left, new_length, level - 1)
    draw_pythagoras_tree(x2, y2, angle_right, new_length, level - 1)

def main():
    level = int(input("Введіть рівень рекурсії: "))
    plt.figure(figsize=(10, 10))
    draw_pythagoras_tree(0, 0, math.pi / 2, 100, level)
    plt.axis("equal")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
