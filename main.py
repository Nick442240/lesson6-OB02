class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def access_level(self):
        return self._access_level

    def __str__(self):
        return f'User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})'


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_list, user):
        if not any(u.user_id == user.user_id for u in user_list):
            user_list.append(user)
            print(f'Пользователь {user.name} успешно добавлен.')
        else:
            print(f'Пользователь {user.name} уже имеется.')

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.user_id == user_id:
                user_list.remove(user)
                print(f'Пользователь {user.name} успешно удален.')
                return
        print(f'Пользователь с ID {user_id} не найден.')

    def __str__(self):
        return f'Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})'


# Пример использования:
if __name__ == "__main__":
    # Создаем пользователей и администратора
    user1 = User(1, 'Иван')
    user2 = User(2, 'Василий')
    admin = Admin(3, 'Федор')

    # Список пользователей
    user_list = [user1, user2]

    # Выводим список пользователей
    print("Первичный список пользователей:")
    for user in user_list:
        print(user)

    # Администратор добавляет нового пользователя
    new_user = User(4, 'Михаил')
    admin.add_user(user_list, new_user)

    # Выводим список пользователей после добавления
    print("\nСписок пользователей после добавления:")
    for user in user_list:
        print(user)

    # Администратор удаляет пользователя
    admin.remove_user(user_list, 2)


    # Выводим список пользователей после удаления
    print("\nСписок пользователей после удаления:")
    for user in user_list:
        print(user)

