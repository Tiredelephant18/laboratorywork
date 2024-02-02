import doctest


class People:
    def __int__(self, name: str, character: list):
        """
             Создание и подготовка к работе объекта "Человек"

             :param name: Имя человека
             :param character: Характер

             Примеры:
             >>> people = People('Bob', 'angry')  # инициализация экземпляра класса
             """
        if not isinstance(name, str):
            raise TypeError
        if name is None:
            raise ValueError("У человека должно быть имя")
        self.name = name
        if not isinstance(character, list):
            raise TypeError
        if character is None:
            raise ValueError("У человека должен быть характер ")
        self.character = character

    def compatibility_test(self, estimate_character: str) -> bool:
        """
        Функция которая проверяет обладает ли человек интересующим нас качеством

        :return: обладает ли человек необходимым качеством

        Примеры:
        >>> people = People('Bob', 'angry')
        >>> people.compatibility_test('kind')
        """

    def add_character(self, character_trait: str) -> list:
        """
        Добавление нового качетво в перечень уже имеющихся.
        :param character_trait: Добавляемое качество
        :return: измененный список качеств человека

        Примеры:
        >>> people = People('Bob', 'angry')
        >>> people.add_character('hard-working ')
        """


class Dog:
    def __int__(self,  pet_name: str, species: str):
        if not isinstance(pet_name, str):
            raise TypeError
        if pet_name is None:
            raise ValueError("У собаки должно быть имя")
        self.pet_name = pet_name
        if not isinstance(species, str):
            raise TypeError
        if species is None:
            raise ValueError("У собаки должна  быть порода")
        self.species = species

    def search_dog(self, estimate_name: str) -> bool:
        """
        Функция которая проверяет по имени тот ли этот пес,что мы ищем
        :param estimate_name: Кличка искомой собаки
        :return: найдена ли интересующая нас собака

        Примеры:
        >>> dog = Dog('Bob', 'spaniel')
        >>> dog.search_dog('Boby')
        """

    def search_species(self, estimate_species: str) -> bool:
        """
        Функция которая проверяет породу собаки
        :param estimate_species: Искомая порода
        :return: найдена ли интересующая нас порода

        Примеры:
        >>> dog = Dog('Bob', 'spaniel')
        >>> dog.search_species('korg')
        """


class Teeth:
    def __int__(self, number: int, count: int):
        if not isinstance(number, int):
            raise TypeError
        if number <= 0:
            raise ValueError("Номер зуба должно быть целым  числом")
        self.number = number
        if not isinstance(count, int):
            raise TypeError
        if count < 0:
            raise ValueError("Количество зубов не отрицательное число  ")
        self.count = count

    def delete_teeth(self, quantity: int) -> int:
        """
            Удаление зубов, измегение количества имеющихся зубов.
            :param quantity: количество удаляемых зубов

            :return возвращает количество оставшихся зубов

            Примеры:
            >>> teeth= Teeth(3, 10)
            >>> teeth.delete_teeth(2)
            """

    def search_teeth(self, item: int) -> bool:
        """

            Поиск нужного зуба по номеру
            :param item : номер искомого зуба
            :return возвращает  обладает ли проверяеммый зуб искомым номером

            Примеры:
            >>> teeth = Teeth(3, 10)
            >>> teeth.search_teeth(4)
        """
        if __name__ == "__main__":
            doctest.testmod()
            pass
