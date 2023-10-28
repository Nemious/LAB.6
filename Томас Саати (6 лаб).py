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
                        print("Ошибка", e)
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
    while True:
        try:
            n = int(input("Введите количество критериев: "))
            if n <= 0:
                raise ValueError("Количество критериев должнобыть больше 1")
            break
        except ValueError as e:
            print("Ошибка", e)
    # Расчет весовых коэффициентов
    weights = calculate_weights(n)

    # Вывод весовых коэффициентов
    print("Весовые коэффициенты:")
    for i, weight in enumerate(weights):
        print(f"Критерий {i + 1}: {weight:.2f}")


if __name__ == "__main__":
    main()