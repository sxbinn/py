i,k,gugu=0,0,""

for i in range(9,1,-1):
    gugu=gugu+("#  %d단  #" % i)

print(gugu)

for i in range(9,0,-1):
    gugu=""
    for k in range(9,1,-1):
        gugu=gugu+str("%2dX %2d= %2d" % (k,i,k*i))
    print(gugu)
