# пример программы на Python, использующей библиотеки Matplotlib и NumPy для описания марковской последовательности, 
# которая предсказывает положение тела

import numpy as np
import matplotlib.pyplot as plt

def markov_sequence(num_steps, initial_state, transition_matrix):
    sequence = [initial_state]
    for _ in range(num_steps):
        new_state = np.random.choice(len(transition_matrix), p=transition_matrix[sequence[-1]])
        sequence.append(new_state)
    return sequence

# Задаем матрицу переходных вероятностей
transition_matrix = np.array([[0.8, 0.2], 
                              [0.3, 0.7]])

# Задаем начальное состояние
initial_state = 0

# Создаем марковскую последовательность из 100 шагов
sequence = markov_sequence(100, initial_state, transition_matrix)

# Выводим последовательность состояний
print("Markov Sequence:", sequence)

# Создаем график положений тела в пространстве и времени
plt.figure(figsize=(8, 4))
plt.plot(sequence, marker='o')
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Markov Sequence")
plt.grid(True)
plt.show()