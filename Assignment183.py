#       ============
#       Assignment 183
#       ============
#
#       Python:   3.8.5
#
#       Author:   Michael B. Darlow
#
#       Purpose:   The Tech Academy -- Python Course. Utilize class polymorphism (definition of methods
#                       in a child class that have the same name as methods in its parent class, essentially
#                       overriding the behavior of the original method).
#
#       Requirements:   -Each child class should have at least two of their own attributes.
#                               -The parent class should have at least one method.
#                               -Both child classes should utilize polymorphism on the parent class method.
#
#

##############
# Parent class: #
##############
class Aquatic_Creatures:
    def __init__(self, name, species, origin, pH_levels, can_swim):
        self.name = name
        self.species = species
        self.origin = origin
        self.pH_levels = pH_levels
        self.can_swim = can_swim

    def information(self):
        info = f"\nName: {self.name}\nSpecies: {self.species}\nOrigin: {self.origin}\npH Levels: {self.pH_levels}\n\
Can Swim: {self.can_swim}"
        return info

####################
# Child class instance: #
####################
class Starfish(Aquatic_Creatures):
    # Child-specific attributes:
    no_of_rays = 5
    reef_safe = False

    def information(self):
        # Reimplementation of parent information() method:
        info0 = Aquatic_Creatures.information(self)
        # Data specific to child:
        info1 = f"\nNo. of Rays: {self.no_of_rays}\nReef Safe: {self.reef_safe}\n\
Starfish don\'t swim, but instead use their 5 (or more) rays with hundreds of tube feet to \"walk\" on the ocean floor."
        # Add together:
        info_full = info0 + info1
        return info_full

####################
# Child class instance: #
####################
class Hatchetfish(Aquatic_Creatures):
    # Child-specific attributes:
    swimming_level = "Top"
    plant_friendly = True

    def information(self):
        # Reimplementation of parent information() method:
        info0 = Aquatic_Creatures.information(self)
        # Data specific to child:
        info1 = f"\nSwimming Level: {self.swimming_level}\nPlant-Friendly: {self.plant_friendly}\n\
Hatchetfish spend the vast majority of their time just below the water's surface."
        # Return the two variables:
        return info0 + info1


# Pet aquatic creatures:
Cookie = Starfish("Cookie", "Chocolate Chip Starfish", "Saltwater", "8.0", False)
Hoch = Hatchetfish("Hoch", "Silver Hatchetfish", "Freshwater", "6.5", True)


if __name__ == "__main__":
    print(Cookie.information() )
    print(Hoch.information() )





