aa=[]
bb=[]
value=0

for i in range(0,600):
    aa.append(value)
    value+=3

for i in range(0,600):
    bb.append(aa[599-i])

print("bb[0]에는 %d이, bb[199]에는 %d이 입력됩니다." % (bb[0],bb[199]))
