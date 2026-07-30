class Talaba:
    def __init__(self, ism, baholar):
        self.ism = ism
        self.baholar = baholar

    def __str__(self):
        bal = self.baholar.values()
        return f"{self.ism} - {len(bal)} ta fan , o'rtacha baho {sum(bal)/len(bal)} "

    def __len__(self):
        return len(self.baholar.values())

    def __setattr__(self, name, value):
        try:
            if name == "baholar":
                if not isinstance(value, dict):
                    raise TypeError("Baholar lug'at (dict) ko'rinishida bo'lishi kerak!")

                for fan, baho in value.items():
                    if not (1 <= baho <= 100):
                        raise ValueError(f"{fan} fani bahosi 1 va 100 oralig'ida bo'lishi kerak!")

            super().__setattr__(name, value)

        except ValueError as e:
            print(e)

        except TypeError as t:
            print(t)

    def __getattr__(self, name):
        return f"Bu attribute mavjud emas: {name}"


Ali = Talaba(
    "Ali",
    {
        "Fizika": 110,
        "Matematika": 84
    }
)

print(Ali.age)