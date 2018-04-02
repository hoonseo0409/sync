import struct
import numpy as np


#mmap_mode

f=open("filename.bin","ab")
#f=file('filename.bin', 'a')
mydata=np.random.randint(low=1,high=65535,size=10,dtype='uint16')
print(mydata)
#mydata.astype('uint16').tofile('filename.bin')
np.save(f, mydata)
f.close()


tmp=np.fromfile('filename.bin', dtype='uint16')
print (tmp)