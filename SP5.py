class Animal:
    def __init__(self, genus, name, year_of_birth, additional_info=None):
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.additional_info = additional_info

    def get_info(self):
        """Return a string with the animal's name and genus."""
        return f"{self.name} is a {self.genus}"


def animals_to_write(animals, filename):
    """Write the names and genera of animals to a text file."""
    with open(filename, 'w') as file:
        for animal in animals:
            file.write(f"{animal.name}, {animal.genus}\n")
animals = [
    Animal(genus="elephant", name="Dumbo", year_of_birth=2000),
    Animal(genus="dog", name="Balto", year_of_birth=1925),
    Animal(genus="python", name="Kaa", year_of_birth=2010, additional_info="a large snake"),
    Animal(genus="lion", name="Simba", year_of_birth=2015),
    Animal(genus="cat", name="Whiskers", year_of_birth=2018, additional_info="loves to nap"),
]
animals_to_write(animals, 'animals.txt')

print("Animal names and genera have been written to 'animals.txt'.")