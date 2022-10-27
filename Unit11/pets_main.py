#Author: Andrew Apollo

import pets

def main():

    #Class activity 11.1.3
    pet = pets.Pet("Black Lab", "Willie (Bone Bone)", 80.0, "Brown", 3)
    print("Name:", pet.get_name(), ", Weight:", pet.get_weight())

    #Class activity 11.1.4
    pet.feed(1800)
    print("Name:", pet.get_name(), ", Weight:", pet.get_weight())

    #Class activity 11.1.5
    pet.walk(1.5)
    print("Name:", pet.get_name(), ", Weight:", pet.get_weight())

main()