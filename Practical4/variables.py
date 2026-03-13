a=5080000
b=5330000
c=5550000
d=b-a
e=c-b
if d>e:
    print("d is larger")
else:
    print("e is larger")
#d=280000 e=220000 so d is larger
#decelerating
X=True 
Y=False
W=X or Y
print(W)
# X=True, Y=True  → W=True
# X=True, Y=False → W=True
# X=False, Y=True → W=True
# X=False, Y=False → W=False