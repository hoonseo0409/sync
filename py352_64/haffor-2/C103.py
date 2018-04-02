import struct
import numpy as np


#mmap_mode
#b'\x93NUMPY\x01\x00v\x00{\'descr\': \'<u2\', \'fortran_order\': False, \'shape\': (10,), }

mydata=np.random.randint(low=1,high=65535,size=10,dtype='uint16')
print(mydata)

f=open("filename.bin","ab")
#f=file('filename.bin', 'a')

#mydata.astype('uint16').tofile('filename.bin')
np.save(f, mydata)

f.close()


#tmp=np.fromfile('filename.bin', dtype='uint16')
#tmp=open('filename.bin', 'rb')

#tmp = np.memmap('filename.bin', dtype='uint16', mode='r', shape=(11))
tmp = np.memmap('filename.bin', dtype='uint16', mode='r')
print (len(tmp))