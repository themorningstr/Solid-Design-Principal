#SRP or SOC :- 



class Journel:
    def __init__(self):
        self.entries = []
        self.count = 0


    def add_entries(self, text):
        self.count += 1
        self.entries.append(f"{self.count}:{text}")
    
    def delete_entries(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close

    # def load(self, filename):
    #     pass

    # def load_from_wed(self):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journel, filename):
        pass


J = Journel()
J.add_entries("Vishwas")
J.add_entries("Ramm")
J.add_entries("Vishwas")

print(J)