#Author: Andrew Apollo 

import plotter

def print_lines(filename):
    file = open(filename)
    for line in file:
        stripped = line.strip()
        print(stripped)

def word_search(filename):
    word = input("User enter a word: ")
    found = False
    word = word.lower()
    file = open(filename)
    for line in file:
        file_word = line.strip()
        if word == file_word.lower():
            print("found the word: " , file_word)
            found = True 
            break
    file.close()

    if not found:
        print("Didn't find the word!")

def longest_word(string):
    stripped = string.strip()
    if stripped == "":
        return

    longest_word = ""
    words = stripped.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    print("Longest word: " , longest_word)

def longest_words(filename):
    file = open(filename)
    for line in file:
        longest_word(line)
    file.close()

def print_names(filename):
    file = open(filename)
    next(file) #skip the header row
    for line in file:
        fields = line.split(',')
        print(fields[1] , fields[0])
    file.close()

def average(filename , column):
    with open(filename) as file:
        header = next(file)
        header_fields = header.split(",")
        name = header_fields[column]
        sum = 0 
        count = 0
        for line in file:
            fields = line.split(",")
            value = fields[column]
            if value != "":
                sum += float(fields[column])
            else:
                sum += 0
            count += 1
        
        print(name , "Average:" , (sum / count))

def plot_grades(filename , colum):
    with open(filename) as csv_file:
        header = next(csv_file).split(",")
        name = header[colum]

        plotter.init("Grades for " + name , "Students" , "Scores")

        for row in csv_file:
            fields = row.split(',')
            score = float(fields[colum])
            plotter.add_data_point(score)

        plotter.plot()

def main():
    #print_lines("data/alice.txt")
    #word_search("data/words.txt")
    #longest_word("The quick brown fox jumped over")
    #longest_words("data/alice.txt")
    #print_names("data/grades_010.csv")
    #average("data/grades_010.csv" , 2)
    plot_grades("data/grades_010.csv" , 10)
    input("Press enter to continue...")
main()