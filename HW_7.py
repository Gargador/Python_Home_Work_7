# Задача 34:

def check_rhythm(poem):
    phrases = poem.split()
    syllables = []
    for phrase in phrases:
        syllables.append(len([c for c in phrase if c in "аеёиоуыэюя"]))
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

Пример использования:
poem = "пара-ра-рам рам-пам-папам па-ра-па-да"
print(check_rhythm(poem)) # Вывод: Парам пам-пам


# Задача 36:

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        row = ""
        for j in range(1, num_columns+1):
            row += str(operation(i,j)) + " "
        print(row.strip())


# Пример использования:
print_operation_table(lambda x, y: x * y)
