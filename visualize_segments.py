import re
import matplotlib.pyplot as plt
import random

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# Відкриття файлу та зчитування координат відрізків
with open("segments", "r") as file:
    contentSegmentsFile = file.read()

x_values = []
y_values = []
labels = []

matches = re.findall(r"\(([+-]?\d+(?:\.\d+)?),\s*([+-]?\d+(?:\.\d+)?)\)", contentSegmentsFile)  # Пошук координат за допомогою регулярного виразу
colors = []

if len(matches) > 0:
    coords = [list(map(float, match)) for match in matches]
    labels = re.findall(r"([A-Z])\(", contentSegmentsFile)  # Пошук імен точок
    for coord in coords:
        x_values.append(coord[0])
        y_values.append(coord[1])
        random_color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])  # Генерація випадкового HEX-кольору
        colors.extend([random_color, random_color])

# Виведення масиву x_values
print(x_values)
print(y_values)
print(labels)

# Побудова відрізків
for i in range(0, len(x_values), 2):
    plt.plot([x_values[i], x_values[i + 1]], [y_values[i], y_values[i + 1]], 'bo-', linestyle="-", color=colors[i])
    plt.text(x_values[i] - 0.015, y_values[i] + 0.25, f"Point {labels[i]}")
    plt.text(x_values[i + 1] - 0.050, y_values[i + 1] - 0.25, f"Point {labels[i + 1]}")



# Зчитування координат точок перетину відрізків з файлу
intersection_points = []
with open("intersection_points", "r") as file:
    for line in file:
        x, y = line.strip().split(' ')
        intersection_points.append((float(x), float(y)))

# Побудова точок перетину 
for i, point in enumerate(intersection_points):
    plt.text(point[0], point[1], f"Point {i+1}", verticalalignment='bottom', horizontalalignment='right')
    plt.plot(point[0], point[1], 'ro')


plt.grid(True)  # Включення сітки
plt.gca().set_aspect('equal')  # Налаштування квадратної сітки
plt.show()