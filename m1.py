class Kitob:
    def __init__(self,nomi, muallif, sahifalar):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifalar = sahifalar

    def __str__(self):
        return f"Nomi: {self.nomi}\nMuallifi: ({self.muallif})\nSahifalar soni: {self.sahifalar}\n\n"

    def __repr__(self):
        return f"{self.nomi} ({self.sahifalar} sahifa)"

    def __len__(self):
        return self.sahifalar

    def __eq__(self, other):
        if not isinstance(self, Kitob):
            return NotImplemented
        return self.sahifalar == other.sahifalar

    def __lt__(self, other):
        if not isinstance(other, Kitob):
            return NotImplemented
        return self.sahifalar < other.sahifalar

    def __gt__(self, other):
        if not isinstance(other, Kitob):
            return NotImplemented
        
        return self.sahifalar > other.sahifalar
    

k1 = Kitob("Xamsa", "Alisher Navoiy", 600)
k2 = Kitob("Animal Farm", "Jorj Ourell", 450)
k3 = Kitob("O'tgan kunlar", "O'tkir hoshimov", 500)

print(k1==k2)
# print(k1)
print(len(k1))

print(k1>k2)
print(k1<k2)

kitoblar = [k1, k2, k3]

saralangan = sorted(kitoblar, key=lambda kitob: kitob.sahifalar)

print(saralangan)



    