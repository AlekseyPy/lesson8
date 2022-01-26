
for i in car:
    text = f"Я хочу машину под маркой {i.upper()}"
    print(text)

car = ['honda', 'lamborgHini', 'mazda']

car = ['honda', 'lamborgHini', 'mazda']
print(car)
car[2] = 'ducati'
print(car)

car = ['honda', 'lamborgHini', 'mazda']
print(car)
car[2] = 'ducati'
print(car)
car.append('mazda')
print(car)
car.insert(0, 'zighoul')
print(car)

car = ['honda', 'lamborgHini', 'mazda']
print(car)
car[2] = 'ducati'
print(car)
car.append('mazda') # добавляет в конец списка
print(car)
car.insert(0, 'zighoul')
print(car)

user = ['u1', 'u2', 'u3', 'u4']

user_V = []
print(user)
while user:
    u = user.pop(0)
    user_V.append(u)
    print(f"Пользователи прошли вeрификацию {u.title()}")
print(user)
print(f"Пользователи прошли вeрификацию {user_V}")