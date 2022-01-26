from traceback import print_tb


people = ["Бабушка","Дедушка","Мама"]
print(people)
for i in people:
    print(f"Здравствуйтем {i}.Я вас приглашаю на конференсию в...")
del people[2]
print(people)
people.insert(2, "Папа")
print(people)
for i in people:
    print(f"Здравствуйтем {i}.Я вас приглашаю на конференсию в...")
people.insert(0, "Сестра")
people.insert(2, "Брат")
people.append("Тетя")
print(people)
for i in people:
    print(f"Здравствуйтем {i}.Я вас приглашаю на конференсию в...")