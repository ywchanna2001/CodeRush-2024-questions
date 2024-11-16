# input = 3 4 5
# save the input integers in an array
wands = list(map(int, input().split()))

a = wands[0]
b = wands[1]
c = wands[2]

if(a==b==c):
    print("Equilateral Barrier")

elif (a==b and a!=c and b!=c) or (a==c and a!=b and c!=b) or (b==c and b!=a and c!=a):
    sorted_wands = sorted(wands)
    if(sorted_wands[2] < sorted_wands[0] + sorted_wands[1]):
        print("Isosceles Barrier") 
    else:
        print("Shattered Magic")
elif(a!=b and a!=c and b!=c):
    sorted_wands = sorted(wands)
    if(sorted_wands[2] < sorted_wands[0] + sorted_wands[1]):
        print("Scalene Barrier") 
    else:
        print("Shattered Magic")
