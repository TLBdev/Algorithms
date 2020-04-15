#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  if n == 0:
    return 1
  


  
  return eating_cookies(n-1)+eating_cookies(n-2)+eating_cookies(n-3)
  
    
  


  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
    # 31, 13, 112, 121, 211, 1111
    # 32, 23, 311, 131, 113, 221, 212, 122, 1112, 1121, 1211, 2111, 11111
    
  #   if n<2:
  #   return 1
  # if n == 2:
  #   return 2
  # answer = 0
  # arr=[]
  # #initial fill
  # while sum(arr) < n:
  #   print("1",sum(arr))
  #   if sum(arr) + 3 <= n:
  #     arr.append(3)
  #     if sum(arr) == n:
  #       answer += len(arr)
  #   elif sum(arr) + 2 <= n:
  #     arr.append(2)
  #     if sum(arr) == n:
  #       answer += len(arr)
  #   elif sum(arr) + 1 <= n:
  #     arr.append(1)
  #     if sum(arr) == n:
  #       answer += len(arr)
  # print("2a",sum(arr))
  # while arr[0] == 3:
  #   arr.pop(0)    
  #   while sum(arr) < n:
  #     if sum(arr) + 2 <= n:
  #       arr.append(2)
  #       if sum(arr) == n:
  #         answer += len(arr)
  #     elif sum(arr) + 1 <= n:
  #       arr.append(1)
  #       if sum(arr) == n:
  #         answer += len(arr)
  # arr.sort(reverse = True)
  # while arr[0] == 2:
  #   arr.pop(0)
  #   while sum(arr) < n:
  #     if sum(arr) + 1 <= n:
  #       arr.append(1)
  #       if sum(arr) == n:
  #         check = 1
  #         for i in arr:
  #           if i != 1:
  #             check = 0
  #         if check == 0:
  #           answer += len(arr)
  #         else: 
  #           answer += 1
  # print(arr)
  # while arr[0] == 1 and arr[1] == 1 and arr[2] == 1:    
  #   arr.pop(0)
  #   arr.pop(0)
  #   arr.pop(0)
    
  #   arr.append(3)
  #   answer += len(arr)
  # print(arr)
  # return answer