def american_to_metric(length, unit):
    if unit == "inches":
        return length * 2.54  # 1 дюйм = 2.54 см
    elif unit == "feet":
        return length * 30.48  # 1 фут = 30.48 см
    else:
        return "Неизвестная единица измерения"

def metric_to_american(length, unit):
    if unit == "centimeters":
        return length / 2.54  # 1 см = 1/2.54 дюйма
    elif unit == "meters":
        return length / 30.48  # 1 м = 1/30.48 фута
    else:
        return "Неизвестная единица измерения"

def main():
    print("Конвертер различных величин")
    print("1. Американская система в метрическую")
    print("2. Метрическая система в американскую")
    choice = input("Выберите режим (1/2): ")

    if choice == "1":
        length = float(input("Введите длину: "))
        unit = input("Выберите единицу измерения (inches/feet): ")
        result = american_to_metric(length, unit)
        print(f"Результат: {result} см")
    elif choice == "2":
        length = float(input("Введите длину: "))
        unit = input("Выберите единицу измерения (centimeters/meters): ")
        result = metric_to_american(length, unit)
        print(f"Результат: {result} дюймов/футов")
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
