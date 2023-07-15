def generate_estimation():
    estimation_text = ""
    total_cost = 0

    while True:
        work = input("Введите название работы (или 'выход' для завершения): ")
        if work == "выход":
            break

        unit = input("Выберите единицу измерения (м2/п.м/шт): ")
        if unit != "м2" and unit != "п.м" and unit != "шт":
            print("Неправильно выбрана единица измерения. Пожалуйста, выберите м2, п.м или шт.")
            continue

        if unit == "шт":
            quantity = float(input("Введите количество штук: "))
            cost = float(input(f"Введите цену за {unit}: "))

            result = quantity * cost
            estimation_text += f"\nРабота: {work}\nЕдиница измерения: {unit}\nКоличество: {quantity} {unit}\nЦена за {unit}: {cost}\nРезультат: {quantity} {unit} * {cost} = {result}\n"
        else:
            measurement = float(input(f"Введите {unit.capitalize()}: "))
            cost = float(input(f"Введите цену за {unit}: "))

            unit_name = "Площадь" if unit == "м2" else "Расстояние"
            result = measurement * cost
            estimation_text += f"\nРабота: {work}\nЕдиница измерения: {unit}\n{unit_name}: {measurement} {unit}\nЦена за {unit}: {cost}\nРезультат: {measurement} {unit} * {cost} = {result}\n"

        total_cost += result

    estimation_text += f"\nОбщая сумма работ: {total_cost}\n"

    estimation_text += "Комментарий: \n"
    estimation_text += "- Расстояние (п.м), площадь (м2) и штуки (шт) оплачиваются отдельно, согласно договоренности.\n"
    estimation_text += "- Дополнительные работы не входят в общую сумму и требуют дополнительного соглашения.\n"

    return estimation_text


def save_estimation(file_name, estimation_text):
    try:
        with open(file_name, "w") as file:
            file.write(estimation_text)
        print(f"Смета сохранена в файле {file_name}")
    except Exception as e:
        print(f"Ошибка при сохранении сметы: {e}")


def main():
    print("Смета на строительные работы:")
    estimation = generate_estimation()
    print("\nРезультат сметы на строительные работы:")
    print(estimation)

    file_name = input("Введите имя файла для сохранения сметы: ")
    save_estimation(file_name, estimation)


if __name__ == "__main__":
    main()
