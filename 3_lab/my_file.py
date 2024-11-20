class Phone:
    # тут ми динамічно придумували які атрибути буде мати клас
    pass

class PhoneWithAttributes:
    GLOBAL_VAR = "класова змінна"
    counter = 0

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
        PhoneWithAttributes.counter += 1 # Змінна яка накопичує кількість телефонів

    # Методи з подвійним підкресленням називаються Магічними методами
    def __del__(self):
        print("Видаляємо обєкт")
    
    def __len__(self):
        return len(self.model)
    
    def __add__(self, obj):
        print(f"Витягаємо деталі з телефона {obj.model} та переносимо його у {self.model}")

    def __mul__(self, obj):
        print("Тепер у шас два телефони!")

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
    
    @staticmethod
    def sunny_weather(team_a=0, team_b=0):
        """Статичні методи не потребують вказівника на обєкт
        """
        print(f"На дворі гарна погода, ми граємо й футбол і не користуємся телефоном, рахунок {team_a}:{team_b}")

    @classmethod
    def create_from_vendor(cls, vendor:str):
        if vendor.lower() == "iphone":
            return cls(vendor, "13", 12, "Китай")
        if vendor.lower() == "xiaomi":
            return cls(vendor, "Red", 13, "Китай")
        if vendor.lower() == "samsung":
            return cls(vendor, "One", 15, "Китай")
        
