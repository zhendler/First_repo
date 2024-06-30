import random

def get_numbers_ticket(min, max, quantity):
  """
  Функція, що генерує випадковий набір унікальних чисел для лотерейного квитка з перевіркою через try-except.

  Args:
      min: Мінімальне можливе число у наборі (не менше 1).
      max: Максимальне можливе число у наборі (не більше 1000).
      quantity: Кількість чисел, які потрібно вибрати (значення між min і max).

  Returns:
      Відсортований список унікальних випадкових чисел або пустий список, якщо параметри некоректні.
  """

  try:
    # Перевірка вхідних даних
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
      raise ValueError("Некоректні параметри")

    # Створення множини для зберігання унікальних чисел
    numbers_set = set()

    # Генерація випадкових чисел до досягнення необхідної кількості
    while len(numbers_set) < quantity:
      random_num = random.randint(min, max)
      numbers_set.add(random_num)

    # Перетворення множини в список і сортування
    numbers_list = list(numbers_set)
    numbers_list.sort()

    return numbers_list

  except ValueError as e:
    print(f"Помилка: {e}")
    return []

# Приклад використання
min_num = 1
max_num = 1001
quantity_num = 6

try:
  lottery_numbers = get_numbers_ticket(min_num, max_num, quantity_num)
  print(f"Ваші випадкові лотерейні номери: {lottery_numbers}")
except Exception as e:
  print(f"Непередбачувана помилка: {e}")
