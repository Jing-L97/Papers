# -*- coding: utf-8 -*-
"""
notes on efficient computing

@author: Jing Liu
"""


'''
Profile in python 
'''
import time

start = time.time()
a = 5+3
end = time.time()


'''
cProfile module: in milliseconds
'''
import cProfile
def f():
    print('helo')


cProfile.run()



'''
line profiler: CPU running
'''

################################################

'''
Efficient data structure

lists and tuples
list: dynamic arrays    not cached: mutable at the ocst of memory cost
tuples: static arrays -> immutable, cached by python runtime

tuple: not changed; lightweight at the cost of immutability

can be mixed types: force all the data to be same type

blist; array: non-numerical situations
    
'''
my_list = [9,1,2,3,4,45]

# linear search O(n)
def linear_search(elem,array):
    for i, item in enumerate(array):
        if item ==elem:
            return i 
    return -1 



'''
improve by sorting; custom objects
Tim-Sort   O(n); O(nlogn) sort

bisect: simplify the 

1.add ele in a list
2.find the closest


compare 2 datasets
-> pick the right data structure and ;ook for it
'''
        
import bisect
import random

def find_closest(numbers,my_val):
    i = bisect.bisect_left(numbers,my_val)
    j = 0
    
    return i
        
        
''' 
Resourcecaching： garbage collection

list vs tuples （1-20: not free the mem but reserved for futrue use)
list O(n): resize appreation
List need to track all the ele every time when    
'''        
            
numbers = [9,1,2,3,4,45]      
numbers[2] = 9
numbers.append()
        
'''
list
append: each time create a new list, memory copy
only the number of elements needed are allocated
''' 
        
        
'''
tuple: fixed
   add one ele
concatenate new tupke and concatenate
new location in memory for the added element
'''        
        
###########################################################################

'''
sets v.s. dict
set: unique collection of keys
o(n): based on arbituary index; also list like search 
o(1) for search table hash table

larger footprint in memory
speed depends on hash func    
'''
        
'''
dict: advanced: O(1): hash func
key -> hash key -> value
hash table: compares to other objects; effective indexing;
mask = no of reserved bucket -1 

insertion: 
    probing
    insert key-value in case of empty bucket/return similar if there is already one/find new index in case ofdifferent values
    laod factor
    pertub: used in python 
    e.g. 
        1.reserve memory sequence
        2.defeine the mask
        3.calculate the hash and index
        !!! collision problem: replace before the new jar
    
deletion:
    null: sentinal marker
    special: signify empty
    
    
resicing:
    fit the new table: recomputing the indices
    quirte expensive; only do this when the hash table is small
    
    8->32->128->512->2048
    
'''        


###########################################################################       
        
'''
generators and iterators

other lang: for(){}
iterators: in for loops, comprehensions, generators; an object can be iterated on
    protocal: _iter_
    iterablr: list, tuple,string
    need to track internal state
    
generators: save memory by dealing only current item
    return an object which can iterate over as one value 
    return: terminate
    yield: recod the generated tokens
    
    itertools
    
    prepare the code to run on multiple CPUs or computures
'''
        
my_lst = [1,2,3,45,6,7]
my_iter = iter(my_lst)
print(next(my_iter))


###########################################################################       

'''
vectors and matrices

numpy for rescue

vector: buiilt from component, operations onlists
        vpython: easier for operations
        
matrices: 
    1. nested lists
    
    importance: optimized using matrices
    problem to notice: 
        a.memory fragmentation
    - lists store pointers instead of data 
    - python ByteCode not optimized
    resulting in multiple look-ups
        b.performance degradation
    force the CPUs to be segmented
        
    2.numpy: flexible multi-dimensional array
        arange: allows the creation of number's list
        shape: return the shape of the matrix
        reshape: renewed dimensions
        size: total number of ele
        dtype: provide type of ele
        itemsize: sizre of each array
    
    how numpy solve the problems above
        faster mand gives memory locality

other: numexpr: run vector expressions and on multiple CPU cores

-reducing time to take data to CPU
reducing the work of CPU

tuning performance down to the external libraries is essential

must generalize optimizations for other computers
'''

import numpy as np

py_array = [1,2,3,4,55,6,7]
np_array = np.array([1,2,3,4,55,6,7])



########################################################################### 
'''
compiling to C

balance code adaptability and team velocity
profiling helps to understand bigger picture

AOT compiler
Cython: compiling to C-like annotated python types into compiled extension module
        used in ipython
        
ShedSkin: automatic
Pythran

JIT ocmpiler
Numba: for numpy code
    provide a decorator to a func
Pypy
-> reduce instructions on CPUs
'''



########################################################################### 

'''
concurrency: optimize execution time during waiting by combining the entire execution
    I/O wait: use this time so that we don't need to wait for the kernal to do so
    context switch: perform low-level operations associated with I/O requests
    event loop: list of functions until ends
                non-blocking
                -callbacks: called on task completion
                -future: returns a promise of future result instead of the actual result
    coroutines: asyncrounously


Useful libraries
Gevent: async used future paradigm 
Tornado: callback paradigm
Asyncio: till python 3.7
 
co-routine decorator 
help to solve I/O bound problem by allowing to run multiple I/O functions

'''

async def my_ciroutine():
    return 'hello'

# need to schedule
loop = asyncio.get_event 
r = loop.run_until_complete(c)




########################################################################### 

'''
useful func
1.map: a func to be pause in
2.zip: take iterables and make iterator do so e.g. zip(*iterables)
3.super: allow multiple inheritances
4.hash: return the hash value fo an object if it has one  hash(object)
5.format: returns a formattedvalue
6.enumerate: iterable and start: give different index of 
7.memoryview(object): 
    bufferprotocal: sccess the internal data of an object
8.pow(X,Y,Z): modules of suppression
9.repre: printable representations, takes object as input
10.strip: remove beginning and ending white spaces
11.dir: return attributes of the parameters 
12.clear  
'''



########################################################################### 

'''
multiprocessing: parallel processing
ckasses concerning in the multiple processing
1.process
    forked 
    start(): after it it's idle
    join（）: start running the rest 
2.lock: no other similar code is processed until it has been locked
3.queue
4.pool
'''

import multiprocessing as mp

print(mp.cpu_count())

########################################################################### 

'''
FIFO: queue need to be pickled ato sent and unpickled to consume; not sttavkle
    consume shared data
    -use put to insert data


data parallalism; use pool class

'''

########################################################################### 

'''
cluaters and job queues

cluster: collections of computers working together to solve a common task
    -easy scaling: dynamic scaling (cost efficiency)
    -> latency of machines
    ->algorithms implementation and their synchronizations

Library: parallel python
    task->compiler->server
'''