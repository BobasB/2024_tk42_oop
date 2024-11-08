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
        self._video_calls = 0

    @property
    def get_availabl_memory(self):
        return self.ram - self._reserved_memory
    
    @property
    def secret(self):
        return f"Ось наш секрет: {self.__privat_message}"
    
    def call(self, phone_number):
        print(f"Набираємо номер телефона: {phone_number}")
        self.ram -= 0.5
        print(f"Програма опрацювання відеодзвінка, тепер доступно : {self.ram} оперативки")
        self._video_calls += 1
        return True
    
    def get_call(self):
        print("Отримали виклик від когось")

    def stop_call(self):
        if self._video_calls > 0:
            self.ram += 0.5
            self._video_calls -= 1
            return True
        return False
