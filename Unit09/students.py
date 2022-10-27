#Author: Andrew Apollo

#Class Activty 9.2.2
def make_student(id, name):
    return [id, name, 0, 0.0]

#Class Activty 9.2.3
def add_student(population, id, name):
    for index in range(len(population)):
        student = population[index]
        if student[0] == id:
            population.pop(index)
            break
    new_student = make_student(id , name)
    population += [new_student]

#Class Activty 9.2.4
def get_student(population , id):
    for student in population:
        if student[0] == id:
            return student
    return None

#Class Activty 9.2.5
def add_credits(population, id, credits):
    student = get_student(population, id)
    if student is not None:
        student[2] += credits

def get_credits(population, id):
    student = get_student(population, id)
    if student is not None:
        return student[2]
    else:
        return None

#Class activty 9.2.10
def add_student_2(population, id_key, name):
    population[id_key] = name

def get_student_2(population, id_key):
    if id_key in population:
        return population[id_key]
    else:
        return None

def main():

    #Class Activty 9.2.2
    '''
    print(make_student("OE2010" , "Papa Emeritus "))
    print(make_student("IF2012" , "Papa Emeritus II"))
    print(make_student("ME2015" , "Papa Emeritus III"))
    print(make_student("PQ2018" , "Cardinal Copia"))
    print(make_student("HM2021" , "Papa Emeritus IV"))
    

    #Class Activty 9.2.3 / 9.2.4
   
    population = [] 
    add_student(population ,"OE2010" , "Papa Emeritus " )
    add_student(population ,"OE2010" , "Tobias Forge" )
    add_student(population ,"IF2012" , "Papa Emeritus II")
    add_student(population ,"IF2012" , "Martin Persner")
    add_student(population ,"ME2015" , "Papa Emeritus III")
    add_student(population ,"PQ2018" , "Cardinal Copia")
    add_student(population ,"HM2021" , "Papa Emeritus IV")
    print(population)
    #9.2.4
    papaI = get_student(population , "OE2010" )
    print(papaI)
    print(get_student(population , "not_real"))
    #9.2.5
    add_credits(population, "OE2010", 4 )
    print(papaI)
    print(get_credits(population, "OE2010"))
    '''
#Class Activty 9.2.9
    population = {}
    add_student_2(population ,"I" , "Papa Emeritus " )
    add_student_2(population ,"F" , "Tobias Forge" )
    add_student_2(population ,"2" , "Papa Emeritus II")
    add_student_2(population ,"P" , "Martin Persner")
    add_student_2(population ,"3" , "Papa Emeritus III")
    add_student_2(population ,"C" , "Cardinal Copia")
    add_student_2(population ,"4" , "Papa Emeritus IV")
    print(population)
    print(get_student_2(population, "F"))
    print(get_student_2(population, "Z"))
main()