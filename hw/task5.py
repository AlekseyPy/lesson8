people = ["Дедушка","Бабушка","Мама"]
print(people)
for i in people:
    print(f"Здравствуйтем {i}.Я вас приглашаю на конференсию в...")
del people[2]
print(f"На жаль к нам не смогла прийти {people.pop()}")
people.insert(-1, "Папа")
print(people)
for i in people:
    print(f"Здравствуйтем {i}.Я вас приглашаю на конференсию в...")