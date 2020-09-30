def find_Index (word, file_name):  #function takes in the identifying word and the file that contain the resume as an argument
    with open(file_name) as f:     
        for i, line in enumerate (f, 1):
            if word in line: 
                return i        #the function returns the index of the line in which the identifying word has occured 

def hide_Entire_Line (i, file_name):
    lines = open(file_name).read().splitlines() #open file, 
    lines[i] = '***********'
    open('out.txt', "w").write('\n'.join(lines))

hide_Entire_Line(find_Index("Name", "sample.txt"), "sample.txt")
