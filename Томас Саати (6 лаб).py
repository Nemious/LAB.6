import tkinter as tk
from tkinter import messagebox


def calculate_weights(n):
    matrix = []

    # Ввод данных попарного сравнения критериев
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            elif i < j:
                while True:
                    try:
                        value = float(
                            input(f"Введите отношение важности критерия {i + 1} к критерию {j + 1}, от 1 до 10: "))
                        if value <= 0 or value >= 10:
                            raise ValueError("Значение не может быть равно нулю или больше 10")
                        break
                    except ValueError as e:
                        messagebox.showerror("Ошибка", str(e))
                row.append(value)
            else:
                row.append(1 / matrix[j][i])
        matrix.append(row)

    # Нормализация матрицы попарных сравнений
    normalized_matrix = []
    for i in range(n):
        row_sum = sum(matrix[i])
        normalized_row = [value / row_sum for value in matrix[i]]
        normalized_matrix.append(normalized_row)

    # Расчет весовых коэффициентов
    weights = [sum(column) / n for column in zip(*normalized_matrix)]

    return weights


def main():
    root = tk.Tk()
    root.title("Метод анализа иерархий")

    def calculate():
        try:
            n = int(entry.get())
            if n <= 0:
                raise ValueError("Количество критериев должно быть больше 1")

            weights = calculate_weights(n)

            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Весовые коэффициенты:\n")
            for i, weight in enumerate(weights):
                result_text.insert(tk.END, f"Критерий {i + 1}: {weight:.2f}\n")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    label = tk.Label(root, text="Введите количество критериев:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Рассчитать", command=calculate)
    button.pack()

    result_text = tk.Text(root, height=10, width=30)
    result_text.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
