class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self,species,name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.__animals += 1

    def get_info(self, species):
        zoo_name = self.name
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        if species == "fish":
            result += f"Fish in {self.name}: {', '.join(self.fish)}\n"
        if species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {self.__animals}"
        return result

    def get_total(self):
        return f'Total animals{self.__animals}'

zoo_name = input()

zoo = Zoo(zoo_name)

n = int(input())

for _ in range(n):
    species,name = input().split(" ")
    zoo.add_animal(species,name)

species = input()

print(zoo.get_info(species))
