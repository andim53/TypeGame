import spell

while True:
    print("Fire\t: 1\nWater\t: 2\nEarth\t: 3\nWind\t: 4\n")
    choice = input("Choose your spell: ")
    
    attack = "Fail"
    if choice == '1':
        attack = spell.fire()
    else:
        print("Spell not learned")
    
    print(attack + "\n\n")
    
