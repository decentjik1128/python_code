from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

#deque
deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)
deque_list.appendleft(10)
print(deque_list)

import time
start_time = time.clock()
deque_list = deque()
#Stack
for i in range(10000):
    for i in range(10000):
        deque_list.append(i)
        deque_list.pop()
print(time.clock()-start_time,'seconds')
