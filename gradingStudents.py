def gradingStudents(grades):
    for i in range(0,len(grades)):
        nf=(grades[i]//5)+5
        if grades[i] < 38 :
            pass
        else:
            if nf-grades[i] < 3:
                return nf
            else:
                return grades[i]
