import math   
AB = input("AB: ") 
AC = input("AC: ")   
AB = float(AB) 
AC = float(AC)   
BC = math.sqrt(AB**2+AC**2)   
S =(AB*AC)/2 
P = AB+AC+BC   
print("S:%.2f"%S)
print("P:%.2f"%P)
