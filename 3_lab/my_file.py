class Phone:
    # тут ми динамічно придумували які атрибути буде мати клас
    pass

class PhoneWithAttributes:
    def __init__(self, vendor, model, ram:int, made_in = None):
        """Це є конструктор для створення обєкту телефон
        """
        # Цей клас має наперед визначені атрибути
        self.vendor = vendor # Публічні атрибути
        self.model = model
        self.ram = ram
        self.made_in = made_in
        self._reserved_memory:float = round(0.1 * int(ram), 2) # Це є захищений атрибут
        self.__privat_message = "Всі телефони зроблені в Китаї"

    @property
    def get_availabl_memory(self):
        return self.ram - self._reserved_memory
    
    @property
    def secret(self):
        return f"Ось наш секрет: {self.__privat_message}"