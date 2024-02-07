if __name__ == "__main__":
    class Gadgets:
        def __init__(self, name: str, cpu_: int, memory: int):
            """
                        Создание и подготовка к работе объекта "Гаджеты"

                        :param name: название гаджета
                        :param cpu_: центральный процесс (количество ядер)
                        :param memory: объем внутренней памяти  Гб

                        Примеры:
                        >>>  gadgets = Gadgets('watch',8,64)  # инициализация экземпляра класса
                        """
            if not isinstance(name, str):
                raise TypeError("название должно быть типа  str")
            self.name = name
            if not isinstance(cpu_, int):
                raise TypeError("количество ядер должено быть типа int ")
            if cpu_ <= 0:
                raise ValueError("количество ядер должено быть положительным числом")
            self.cpu_ = cpu_
            if not isinstance(memory, int):
                raise TypeError("объем внутренней памяти должен быть int")
            if memory <= 0:
                raise ValueError("объем внутренней памяти не может быть отрицательным числом")
            self.memory = memory

        def __repr__(self):
            return f"{self.__class__.__name__}(name= {self.name!r}, cpu_={self.cpu_!r}, memory={self.memory!r})"

        def __str__(self):
            return f"Название{self.name}"

        def search_needed_memory(self, estimate_memory: int) -> bool:

            """
            Поиск гаджета с искомым объёмом паямти.
             :param estimate_memory: Искомый объём памяти               

             Примеры:
                    >>> gadget = Gadgets('watch',8,64)
                    >>> gadget.search_needed_memory(20)
                    """
        def specifications(self) -> list:
            """
                Получение всех характеристик гаджета( распечатать все атрибуты)
                Примеры:
                 >>> gadget = Gadgets('watch',8,64)
                 >>> gadget.specifications()
            """

    class Phones(Gadgets):
        def __init__(self, name: str, cpu_: int, memory: int, display: str):
            super().__init__(name, cpu_, memory)
            """
              Создание и подготовка к работе объекта "Телефоны"
              
                 Унаследованные атрибуты
                :param name: название гаджета 
                :param cpu_: центральный процесс( количество ядер)
                :param memory:объем внутренней памяти составляет в Гб
                
                добавленный атрибут 
                :param display: дисплей OLED или IPS

                Примеры:
                 >>>  phone = Phones('samsung',8,64,'OLED' )  # инициализация экземпляра класса
            """
            if not isinstance(display, str):
                raise TypeError(" тип диплея должен быть типа  str")
            self.display = display

        def __repr__(self):
            return f"{self.__class__.__name__}(name= {self.name!r}, cpu_={self.cpu_!r}, " \
                   f"memory={self.memory!r},display={self.display!r})"
        """
        Метод __repr__ перегружен так как экземпяры класса  Phone имеют больше атрибутов чем в базовом классе.
            
        """
        def specifications(self):
            """
                метод перегружен так как у класса Phone больше атрибутов.
                Получение всех характеристик гаджета( распечатать все атрибуты)
                Примеры:
                 >>> gadget = Phones('watch',8,64,'OLED')
                 >>> gadget.specifications()
            """
    # Write your solution here
    pass
