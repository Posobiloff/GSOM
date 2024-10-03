class Animal:
    def __init__(self, genus, name, year_of_birth, additional_info=None):
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.additional_info = additional_info
    def get_age(self, year):
        """Calculate the age of the animal in a given year."""
        return year - self.year_of_birth
    def get_info(self):
        """Return a string with the animal's name and genus."""
        return f"{self.name} is a {self.genus}"
    def __str__(self):
        """Return a string representation of the animal."""
        info = self.get_info()
        if self.additional_info:
            info += f". Additional info: {self.additional_info}"
        return info
def find_oldest_animal(animals, current_year):
    """Find the oldest animal in the list."""
    oldest_animal = None
    max_age = -1

    for animal in animals:
        age = animal.get_age(current_year)
        if age > max_age:
            max_age = age
            oldest_animal = animal
    return oldest_animal
animals = [
    Animal(genus="elephant", name="Dumbo", year_of_birth=2000),
    Animal(genus="dog", name="Balto", year_of_birth=1925),
    Animal(genus="python", name="Kaa", year_of_birth=2010, additional_info="a large snake"),
    Animal(genus="lion", name="Simba", year_of_birth=2015),
    Animal(genus="cat", name="Whiskers", year_of_birth=2018, additional_info="loves to nap"),
]

current_year = 2023

oldest_animal = find_oldest_animal(animals, current_year)

if oldest_animal:
    print(f"The oldest animal is {oldest_animal.name}, a {oldest_animal.genus}, aged {oldest_animal.get_age(current_year)} years.")S