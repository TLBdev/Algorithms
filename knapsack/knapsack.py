#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  
  arr = []
  for i in items:
    arr.append([i.index, i.size, i.value, i.value/i.size])
   
  swaps_performed = 1
  max_length = len(arr)
  while swaps_performed > 0:
      swaps = 0
      max_length -= 1
      for i in range(0, max_length):
          
          if i + 1 <= max_length:
              if arr[i][3] > arr[i+1][3]:
                  smaller = arr[i+1]
                  larger = arr[i]
                  arr[i+1] = larger
                  arr[i] = smaller
                  swaps += 1
      swaps_performed = swaps
  
  answer = []
  total_value = 0
  loop_counter = len(arr) + 1
  while loop_counter > 0:
    loop_counter -= 1
    test_answer = []
    test_value = 0
    test_weight = 0
    for i in range(len(arr)):
      if arr[-(i+1)][1] + test_weight <= capacity and i != loop_counter:
        test_weight += arr[-(i+1)][1]
        test_value += arr[-(i+1)][2]
        test_answer.append(arr[-(i+1)][0])
    if test_value > total_value:
      total_value = test_value
      answer = test_answer
  for i in range(0, len(answer)):
    smallest_index = i
    for x in range(i , len(answer)):
        if answer[x] < answer[smallest_index]:
            smallest_index = x
                        
    if smallest_index > 0:
        smaller = answer[smallest_index]
        larger = answer[i]
        answer[smallest_index] = larger
        answer[i] = smaller
    
  return {'Value': total_value, 'Chosen': answer}
  #{'Value': 2640, 'Chosen': [44, 83, 104, 107, 134, 160, 239, 271, 295, 297, 308, 335, 337, 370, 373, 420, 432, 561, 566, 623, 648, 671, 693, 704, 737, 782, 795, 796, 814, 844, 866, 907, 909, 913, 935, 949, 987, 997]}
  #value: 2639, 'Chosen': [44, 83, 104, 107, 134, 160, 239, 271, 295, 297, 308, *329co15.0, 335, 337, 370, 373, 420, 432, 561, 566, 623, 648, 671, 693, *700 co11.0, 704, 737, 782, 795, 796, 814, 844, 866, 907, 909, 913, 935, 949, *(987 co13.5) 997]


  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')