import random
import itertools as it
import argparse

"""
ZADANIE 11.1

Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania. Przydatne są m.in. następujące rodzaje danych:
(a) różne liczby int od 0 do N-1 w kolejności losowej,
(b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
(c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
(d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
(e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N). 
"""


def genA(N,k):
  return random.sample(range(0,N),k=N)

def genB(N,k):
  a = list(range(N))
  for v in it.islice(it.cycle(a),0,N*4): # 
    i = random.randrange(0,N)
    if abs(v-i)<k:
      a[v],a[i] = a[i],a[v]
  return a

def genC(N,k):
  return list(reversed(genB(N,k)))

def genD(N,k): # gauss
  return [random.gauss(0,1) for _ in range(N)]

def genE(N,k):
  S = [ random.randint(0,10000) for _ in range(k)]
  return random.sample(list(it.islice(it.cycle(S),0,N)),k=N)


"""
ZADANIE 11.6
Napisać iteracyjną wersję funkcji quicksort().   
"""
def partition(array,L,H):
  i = L
  PIVOT = array[H]
  for j in range(L,H):
    if array[j]<PIVOT:
      array[i],array[j] = array[j],array[i]
      i+=1
  array[i],array[H] = array[H],array[i]
  return i

def quick_iter(array,N):
  S = [] # stack
  mid = 0
  returned = False
  S.append((0,N-1))
  while S:
    top = S[-1]
    if returned:
      child = S.pop()
      if not S: break

      top = S[-1]

      if top[1]==child[1]: continue

      S.append((child[1]+2,top[1]))
      returned = False
      continue

    if top[0]>=top[1]:
      returned = True
      continue

    mid = partition(array,top[0],top[1])
    S.append((top[0],mid-1))

  return array


generator = {'A':genA,'B':genB,'C':genC,'D':genD,'E':genE}
gen_help ="""A - int numbers from 0 to N-1 in random order  
B - int numbers from 0 to N-1 in almost ordered K far from original position
C - B reversed
D - N float numbers gauss
E - N repeated int numbers from k length set
"""

from argparse import RawTextHelpFormatter

arg_parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter)
arg_parser.add_argument("gen",help=gen_help,type=str,choices=['A','B','C','D','E'])
arg_parser.add_argument("-N",type=int,help="[default = 10]",default=10)
arg_parser.add_argument("-K",help="set length [default = 3]",type=int,default=3)
arg_parser.add_argument("-save",help="save input/output to files [default = F]",type=str,default='F')


args = arg_parser.parse_args()

array = generator[args.gen](args.N,args.K)
if args.save=='T':
  f = open('array_in.txt','w')
  f.write(repr(array))
  f.close()
  quick_iter(array,len(array))
  f = open('array_out.txt','w')
  f.write(repr(array))
  f.close()
  print('Done.')

else:
  print("Before:",array)
  quick_iter(array,len(array))
  print(" After:",array)