def countingValleys(steps, path):
    # Write your code here
    c=0
    v=0
    for i in range(steps):
        if path[i]=="D" and c==0:
            c+=1
            v+=1
        elif path[i]=="D" and c!=0:
            c+=1
        elif path[i]=="U":
            c-=1
    return v
