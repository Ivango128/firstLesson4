# Функция для расчета массы готовых продуктов
def calculate_products(milk_mass):
    # Распределение молока на продукты
    mass_oil = milk_mass * 0.30
    mass_cream = milk_mass * 0.25
    mass_cottage_cheese = milk_mass * (1 - 0.30 - 0.25)  # Остаток на творог

    # Уменьшение массы готовых продуктов
    final_mass_oil = mass_oil * 0.95  # 5% потерь
    final_mass_cream = mass_cream * 0.97  # 3% потерь
    final_mass_cottage_cheese = mass_cottage_cheese * 0.90  # 10% потерь

    return final_mass_oil, final_mass_cream, final_mass_cottage_cheese


# Функция для расчета оставшейся массы, которая не помещается в грузовики
def calculate_leftover(final_mass_oil, final_mass_cream, final_mass_cottage_cheese):
    total_mass = final_mass_oil + final_mass_cream + final_mass_cottage_cheese
    truck_capacity = 3 * 5000  # 3 грузовика по 5 тонн
    leftover_mass = total_mass - truck_capacity

    return total_mass, leftover_mass


# Запрашиваем у пользователя массу молока
milk_mass = float(input("Введите массу молока, поступившего на завод (в кг): "))

# Рассчитываем массу готовых продуктов
final_mass_oil, final_mass_cream, final_mass_cottage_cheese = calculate_products(milk_mass)

# Рассчитываем оставшуюся массу
total_mass, leftover_mass = calculate_leftover(final_mass_oil, final_mass_cream, final_mass_cottage_cheese)

# Выводим результаты
print(f"Масса масла: {final_mass_oil} кг")
print(f"Масса сливок: {final_mass_cream} кг")
print(f"Масса творога: {final_mass_cottage_cheese} кг")
print(f"Общая масса готовых продуктов: {total_mass} кг")

print(f"Количество кг, которое не поместилось в грузовики или не было догружено: {leftover_mass} кг")

