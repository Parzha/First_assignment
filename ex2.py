
def mosalaschecker(a1,a2,a3):
    if a1<(a2+a3) and a2<(a1+a2) and a3<(a1+a2):
        return 1
    else:
        return 0

loop_flag=1
while(loop_flag):
    x,y,z = [int(x) for x in input("azlae mosalas vared konid:").split()]
    if x>0 and y>0 and z>0:
        loop_flag=0
    else:
        print("invalid measures try again")


flag=mosalaschecker(x,y,z)

if (flag==1):
    print("acceptable triangle")
else:
    print("can't be a triangle")

