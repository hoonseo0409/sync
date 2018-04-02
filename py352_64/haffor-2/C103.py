import struct
import numpy as np
import io


#mmap_mode
#b'\x93NUMPY\x01\x00v\x00{\'descr\': \'<u2\', \'fortran_order\': False, \'shape\': (10,), }

def makeandsavenp():
    mydata=np.random.randint(low=1,high=65535,size=10,dtype='uint16')
    #print(mydata)

    f=open("hexDec.bin","ab")
    #f=file('filename.bin', 'a')

    #mydata.astype('uint16').tofile('filename.bin')
    np.save(f, mydata)

    f.close()


#tmp=np.fromfile('filename.bin', dtype='uint16')
tmp=open('hexDec.bin', 'rb')

#tmp = np.memmap('filename.bin', dtype='uint16', mode='r', shape=(11))

for i in range(10):
    makeandsavenp()

#tmp = np.memmap('hexDec.bin', dtype='uint16', mode='r')
tmp2=np.load(tmp)
print (tmp2)


"""
def sort_large_file(n: int, source: open, sink: open, file_opener=open) -> None:
    '''
        approach:
            break the source into files of size n
            sort each of these files
            merge these onto the sink
    '''

    # store sorted chunks into files of size n
    mergers = []
    while True:
        text = list(source.read(n))
        if not len(text):
            break;
        text.sort()
        merge_me = file_opener()
        merge_me.write(''.join(text))
        mergers.append(merge_me)
        merge_me.seek(0)

    # merge onto sink
    stack_tops = [f.read(1) for f in mergers]
    while stack_tops:
        c = min(stack_tops)
        sink.write(c)
        i = stack_tops.index(c)
        t = mergers[i].read(1)
        if t:
            stack_tops[i] = t
        else:
            del stack_tops[i]
            mergers[i].close()
            del mergers[i]  # __del__ method of file_opener should delete the file


def main():
    '''
        test case
        sort 6,7,8,9,2,5,3,4,1 with several memory sizes
    '''

    # load test case into a file like object
    input_file_too_large_for_memory = io.StringIO('678925341')

    # generate the expected output
    t = list(input_file_too_large_for_memory.read())
    t.sort()
    expect = ''.join(t)
    print('expect', expect)

    # attempt to sort with several memory sizes
    for memory_size in range(1, 12):
        input_file_too_large_for_memory.seek(0)
        output_file_too_large_for_memory = io.StringIO()
        sort_large_file(memory_size, input_file_too_large_for_memory, output_file_too_large_for_memory, io.StringIO)
        output_file_too_large_for_memory.seek(0)
        assert (output_file_too_large_for_memory.read() == expect)
        print('memory size {} passed'.format(memory_size))


if __name__ == '__main__':
    example = main
    example()

"""