# assuming your data is exactly as in the original question
data = '''records STUDENT_NAME| jack | STUDENT_MARKS|200| STUDENT_NAME| clark |STUDENT_MARKS|200| STUDENT_NAME| Ajkir | STUDENT_MARKS|30| STUDENT_NAME| Aqqm | STUDENT_MARKS|200| STUDENT_NAME| jone | STUDENT_MARKS|200| STUDENT_NAME| jake | STUDENT_MARKS|100|'''

data  = data.split('|')

for idx in range(1, len(data), 4):
    # every second item in the list is a name and every fourth is a mark
    name = data[idx].strip() # need to add code to check for duplicate names
    mark = int(data[idx+2].strip()) # this will crash if not a number
    print(name, mark) # use these values to add to the database
