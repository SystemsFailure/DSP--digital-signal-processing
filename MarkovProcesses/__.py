# Программа для отображения слкчайной траиктории тела в пространстве и времени с учетом скорости и начального положения

import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры модели
num_steps = 100  # Количество временных шагов
start_position = np.array([0, 0])  # Начальная позиция воздушного тела [x, y]
velocity_mean = np.array([1, 1])  # Средняя скорость воздушного тела [vx, vy]
velocity_cov = np.array([[1, 0], [0, 1]])  # Ковариационная матрица скорости

# Генерируем случайную траекторию воздушного тела
np.random.seed(0)
velocities = np.random.multivariate_normal(velocity_mean, velocity_cov, num_steps)
trajectory = np.cumsum(velocities, axis=0) + start_position

# Отображаем результаты
plt.plot(trajectory[:, 0], trajectory[:, 1])
plt.scatter(start_position[0], start_position[1], color='red', label='Start')
plt.scatter(trajectory[-1, 0], trajectory[-1, 1], color='green', label='End')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Airplane Trajectory')
plt.legend()
plt.show()