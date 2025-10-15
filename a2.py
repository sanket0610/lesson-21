l1=[18,45,77,1,7,33,93]
print("LIST 1:", l1)
s=0
for i in l1:
    s=s+i
print("SUM=", s)
print("AVERAGE:",s/len(l1))
print("MAXIMUM:",max(l1))
print("MINIMUM:",min(l1))
l1.sort()
print("SORTED LIST:",l1)
l1.reverse()
print("REVERSE:",l1)