def gradingStudents(grades):
    # Write your code here
    grades_count=len(grades)
    grade=[]
    for i in range(grades_count):
        nm= grades[i]%5
        if grades[i] < 38:
            grade+= [grades[i]]
        else:
            if nm >2:
                grade+= [grades[i] + 5-nm]
            else:
                grade+= [grades[i]]
    grades=grade
    return grades
