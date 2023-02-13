import matplotlib.pyplot as plt
import math

t, T, h = 0, 1000, 10**-2
b = 0.208186
x, y, z = [1], [1], [1]

print("Початкові умови: t = " + str(t))
print("                 (x; y; z) = (" + str(x[0]) + "; " + str(y[0]) + "; " + str(z[-1]) + ") \n")

print("Обчислення запущено...")
while t < T:
    x.append(x[-1] + h * (math.sin(y[-1]) - b * x[-1]))
    y.append(y[-1] + h * (math.sin(z[-1]) - b * y[-1]))
    z.append(z[-1] + h * (math.sin(x[-1]) - b * z[-1]))

    x[-1] = x[-2] + h*(math.sin(y[-1]) - b * x[-1] + math.sin(y[-2]) - b * x[-2])
    y[-1] = y[-2] + h*(math.sin(z[-1]) - b * y[-1] + math.sin(z[-2]) - b * y[-2])
    z[-1] = z[-2] + h*(math.sin(x[-1]) - b * z[-1] + math.sin(x[-2]) - b * z[-2])

    t_old = t
    t = t + h

    if (t > T/4) & (t_old < T/4):
        print("25% . . .")
    elif (t > T/2) & (t_old < T/2):
        print("50% . . .")
    elif (t > T*3/4) & (t_old < T*3/4):
        print("75% . . .")

print("Систему проінтегровано!")
ax = plt.axes(projection="3d")
ax.plot(x, y, z, linewidth=0.5, color='r')
plt.title("Фазовий портрет")
plt.show()
