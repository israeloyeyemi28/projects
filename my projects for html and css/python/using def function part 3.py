# after defining function4 
#it seems the return statement wiuld define what its going to do like return 3*x 
#meabwhile in line 8 f has ben called as 4 sk 3*4 = 12
def function4(x):
    print(x)
    print("still in the code")
    return 3*x
f = function4(4)
print(f)
    