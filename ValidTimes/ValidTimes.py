from itertools import permutations
def solution(A,B,C,D):
    s1=str(A)
    s2=str(B)
    s3=str(C)
    s4=str(D)
    a=s1+s2+s3+s4
    op=set()
    le= [x.lower() for x in a]
    for n in range(2,len(a)):
        for y in list(permutations(le)):
            hr1=int(y[0])*10
            hr2=int(y[1])
            m1=int(y[2])*10
            m2=int(y[3])
            hrs=hr1+hr2
            mins=m1+m2
            if 60> mins >=0 and 24 > hrs >=0:
                hour=str(hrs)
                minutes=str(mins)
                time=hour+":"+minutes
                op.add(time)
    return(len(op))

print(solution(1,8,3,2))
