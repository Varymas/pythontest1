from msvcrt import kbhit


n = float(input(""))
c=0
k=0
while n != 0:
   c += n
   k += 1
   n = n-1
print(c ,k ) 