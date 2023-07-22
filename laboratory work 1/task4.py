users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

userset = set(users)
dict = {
    "Общее количество": len(users),
    "Уникальные посещения": len(userset)
}

print(dict)
