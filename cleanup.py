import os
import shutil
lis=[]
i=1
destinationdir='C:\Users\User\Desktop\Cleanup'
while os.path.exists(destinationdir):
    destinationdir+=str(i)
    i+=1
os.makedirs(destinationdir)

lis=os.listdir('C:\Users\User\Desktop')
for x in lis:
    print x
    if x==__file__:
        continue
    shutil.move(x,destinationdir)
