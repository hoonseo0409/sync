import struct
import numpy as np



f=open("filename.bin","wb")
mydata=np.random.randint(low=1,high=65535,size=10,dtype='uint16')
print(mydata)
mydata.astype('int16').tofile('filename.bin')

"""
myfmt='f'*len(mydata)
#  You can use 'd' for double and < or > to force endinness
bin=struct.pack(myfmt,*mydata)
print(bin)
f.write(bin)
f.close()
"""

tmp=np.fromfile('filename.bin', dtype='uint16')
print (tmp)