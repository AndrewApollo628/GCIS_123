'''
Author: Andrew Apollo 

This program will
    - Print an avengers bio
    - Print the roster of the avengers
    - find a specific avenger 
    - find out who the team leader is 
    - Print the team members with all bio's 

'''
class Avenger:
    '''
    This class will
        - initalize an avengers bio 
    ''' 

    __slots__ = ["name", "abilities", "weapons"]

    def __init__(self, name):
        '''
        This function will
        - initalize an avengers bio 
        '''
        self.name = name
        self.abilities = []
        self.weapons = []

class Team: 
    '''
    This class will
        - initalize the avengers team
    ''' 

    __slots__ = ["roster", "leader"]

    def __init__(self):
        '''
        This function will
        - initalize the avengers roster
        '''
        self.roster = set()
        self.leader = []

AVENGERS = Team()

def print_avenger_bio(avenger):
    '''
    This function will
        - Check to see if the avenger is the leader
        - print the bio of the leader if true
        - print out the avenger bio if not leader

    Paramaters
        - avenger: avenger being passed in
    '''
    
    name = avenger.name
    abilities = avenger.abilities
    weapons = avenger.weapons
    
    for i in AVENGERS.leader: #Checks to see if the Avenger is the leader 
        if name  == i:
            print("Leader Bio:")
            print(name, " Leader")
        else:
            print("Avenger Bio:")
            print(name)

    print("Abilities:")
    for ab in abilities:
        print(ab)
    if len(weapons) != 0:
        print("Weapons:")
        for we in weapons:
            print(we)
    

def find_avenger(avenger, team):
    '''
    This function will
        - see if teh avenger is in the team 
        - if avenger is in the team they are found and bio will print
        - if not found they are not in the team

    Paramaters
        - avenger: avenger being passed in
        - team: team of avengers  
    '''
    if avenger in team:
        print("Avenger found!!!")
        print_avenger_bio(avenger)
    else:
        print("Avenger not found")

def print_team(team):
    '''
    This function will 
        - print the roster of the team 
        - will check to see which one is the leader and indicate that 

    Paramaters:
        - team: team of avengers being passed in
    '''
    team = team.roster
    print("Roster:")
    for an_avenger in team:
        for i in AVENGERS.leader:
            if an_avenger.name == i:
                print(an_avenger.name , " Leader")
            else:
                print(an_avenger.name)
        
def print_team_with_bio(team):
    '''
    This function will 
        - print the roster of the team with their bios 

    Paramaters:
        - team: team of avengers being passed in
    '''
    team = team.roster
    print("Roster:")
    for an_avenger in team:
        print_avenger_bio(an_avenger)
        print()

def main():

    Iron_man = Avenger("Iron Man (Tony Stark)")
    Iron_man.abilities.append("Technical Genious")
    Iron_man.weapons.append("Mark VII Armor Suit")
    AVENGERS.leader.append("Iron Man (Tony Stark)")
    AVENGERS.roster.add(Iron_man)

    Thor = Avenger("Thor")
    Thor.abilities.append("Extreme super strength.")
    Thor.abilities.append("Can control lightning.")
    Thor.weapons.append("Mjolnir")
    AVENGERS.roster.add(Thor)

    Hulk = Avenger("Hulk (Bruce Banner)")
    Hulk.abilities.append("Extreme super strength")
    Hulk.abilities.append("Super healing.")
    Hulk.abilities.append("Genious (when Bruce Banner)")
    AVENGERS.roster.add(Hulk)

    Cap = Avenger("Captain America (Steve Rogers)")
    Cap.abilities.append("Super Strength.")
    Cap.abilities.append("Super reflexes.")
    Cap.weapons.append("Vibranium Shield")
    AVENGERS.roster.add(Cap)

    #print avenger bio test (non leader)
    print_avenger_bio(Hulk)
    print()

    #print avenger bio test (Leader)
    print_avenger_bio(Iron_man)
    print()

    #find avenger test
    find_avenger(Cap, AVENGERS.roster)
    print()

    #Print team test 
    print_team(AVENGERS)
    print()

    #print team with bio test 
    print_team_with_bio(AVENGERS)
    print()
    
main()