import struct
import numpy as np



f=open("filename.bin","wb")
mydata=np.random.randint(low=1,high=65535,size=10,dtype='uint16')
print(mydata)
mydata.astype('uint16').tofile('filename.bin')



tmp=np.fromfile('filename.bin', dtype='uint16')
print (tmp)