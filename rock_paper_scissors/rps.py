#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = ['rock', 'paper', "scissors"]
  
  if n < 1: 
    return [[]]
  if n == 1: 
    return[[plays[0]], [plays[1]], [plays[2]]]
  amt = 3
  for i in range(n - 1):
      amt *= 3
  answer = [[] for i in range(amt) ]
  chunk = len(answer) // 3
  last_hit = 0
  while len(answer[-1]) < n:
    for i in range(0 , chunk * 3 ):
      if i < chunk:
        answer[last_hit].append(plays[0])
        last_hit += 1
      elif i < chunk + chunk:
        answer[last_hit].append(plays[1])
        last_hit += 1
      elif i < chunk + chunk + chunk:
        answer[last_hit].append(plays[2])
        last_hit += 1
      
      if last_hit == len(answer):
        
        chunk = chunk // 3
        last_hit = 0
  return answer
  
  
  
  
  
  # full_loops = 0
  # last_index_hit = 0
  # while len(answer[-1]) < n:
  #   for i in range(last_index_hit ,(n-full_loops) ** 3 + 1):
  #     if last_index_hit > n ** 3 + 1:
  #       full_loops += 1
  #     if i < ((n ** 3) / 3):
  #       answer[i].append(plays[0])
  #     elif i < ((n ** 3) / 3) + ((n ** 3) / 3):
  #       answer[i].append(plays[1])
  #     elif i <= n ** 3 + 2:
  #       answer[i].append(plays[2])
  #     last_index_hit += 1
  
  # return answer

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
    # 1
    # [['rock'], 
    # ['paper'], 
    # ['scissors']]
    # 2
    # [
    # ['rock', 'rock'], 
    # ['rock', 'paper'], 
    # ['rock', 'scissors'], 
    # ['paper', 'rock'], 
    # ['paper', 'paper'], 
    # ['paper', 'scissors'], 
    # ['scissors', 'rock'], 
    # ['scissors', 'paper'], 
    # ['scissors', 'scissors']
    # ]
    # 3
    # [['rock', 'rock', 'rock'], 
    # ['rock', 'rock', 'paper'], 
    # ['rock', 'rock', 'scissors'], 
    # ['rock', 'paper', 'rock'], 
    # ['rock', 'paper', 'paper'], 
    # ['rock', 'paper', 'scissors'], 
    # ['rock', 'scissors', 'rock'], 
    # ['rock', 'scissors', 'paper'], 
    # ['rock', 'scissors', 'scissors'], 
    # ['paper', 'rock', 'rock'], 
    # ['paper', 'rock', 'paper'], 
    # ['paper', 'rock', 'scissors'], 
    # ['paper', 'paper', 'rock'], 
    # ['paper', 'paper', 'paper'], 
    # ['paper', 'paper', 'scissors'], 
    # ['paper', 'scissors', 'rock'], 
    # ['paper', 'scissors', 'paper'], 
    # ['paper', 'scissors', 'scissors'], 
    # ['scissors', 'rock', 'rock'], 
    # ['scissors', 'rock', 'paper'], 
    # ['scissors', 'rock', 'scissors'], 
    # ['scissors', 'paper', 'rock'], 
    # ['scissors', 'paper', 'paper'], 
    # ['scissors', 'paper', 'scissors'], 
    # ['scissors', 'scissors', 'rock'], 
    # ['scissors', 'scissors', 'paper'], 
    # ['scissors', 'scissors', 'scissors']]