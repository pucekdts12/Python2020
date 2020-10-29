import argparse
import pprint as pp
import ast
import re
from collections import Counter

"""
  zakładam że w każdej liście jest maks 1 zagnieżdżenie tzn.: [1,[2,[3]]] a nie [1,[2],[3],[4]]
  czyli na każdym poziomie jest tylko jeden podpoziom
"""

def zadanie1(args): # wrapper żeby timer dokładnie sprawdzał samo wyszukanie oraz dodanie
  nested_lists=ast.literal_eval(args.list)
  print("Przed",nested_lists)
  #_zadanie1(nested_lists)
  _zadanie1_oneline(nested_lists)
  print("Po",nested_lists)

def _zadanie1(nested_lists):
  current = iter(nested_lists)
  last = nested_lists
  try:
    while True:
      tmp = next(current)
      if type(tmp)==list:
        current = iter(tmp)
        last = tmp
  except:
    #print("Before add ",nested_lists)
    last += [last[-1]+1]
    #print("After add ",nested_lists)

def _zadanie1_oneline(nested_lists):  
  #depth = lambda l: (depth( next( (i for i in l if type(i)==list),False) ) or l+['dummy']) if l!=False else l
  depth = lambda l: ((depth( next( (i for i in l if type(i)==list),False) )==False and l.append(l[-1]+1)) or l) if l!=False else False
  depth(nested_lists)

def zadanie1_checkTimes(args):
  from timeit import Timer

  t1 = Timer(lambda: _zadanie1([1,2,[3,4,[5,6],5],3,4]))
  t2 = Timer(lambda: _zadanie1_oneline([1,2,[3,4,[5,6],5],3,4]))
  print("Sprawdzanie na [1,2,[3,4,[5,6],5],3,4]")
  print("Kilka linii:",t1.timeit(number=1))
  print("Jedna linia",t2.timeit(number=1))


#def zadanie2(year):
def zadanie2(args):
  return ((args.year%4==0 and args.year%100!=0) or args.year%400==0)

#def zadanie3(text,ignore_case = True):
def zadanie3(args):
  #używam wyraźeń regularnych bo jestem leniwy :)
  print(f"Statistics for: {args.text}\n{pp.pformat(dict(Counter(args.text)))}")
  print("Number of words:",len(re.findall("\w+",args.text)))  

#def zadanie4(x,y,z,n):
def zadanie4(args):
  #print([ [i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k)!=n])
  print([ [i,j,k] for i in range(0,args.x+1) for j in range(0,args.y+1) for k in range(0,args.z+1) if (i+j+k)!=args.n])

#def zadanie5(N):
def zadanie5(args):
  print(f"{args.N} as bin {bin(args.N)[2:]}")
  #print("Gap:",max( len(i) for i in bin(args.N).replace('0b','').split('1'))) # jeśli nie muszą być 1 s każdej strony
  print( "Largest gap: ",max(map(lambda i:len(i),re.findall("1(0+)1",bin(args.N)[2:])),default=0) ) # jeśli MUSZA


arg_parser = argparse.ArgumentParser()
subparsers = arg_parser.add_subparsers(help='numer zadania',dest='zadanie')

zad1_p = subparsers.add_parser('1')
zad1_p.add_argument("list",help="lista w formacie pythona [1,2,[3,4],...]",type=str)

zad2_p = subparsers.add_parser('2')
zad2_p.add_argument("year",help="rok do sprwdzenia",type=int)

zad3_p = subparsers.add_parser('3')
zad3_p.add_argument("text",help="tekst to sparsowania",type=str)


zad4_p = subparsers.add_parser('4')
zad4_p.add_argument("x",help='',type=int)
zad4_p.add_argument("y",help='',type=int)
zad4_p.add_argument("z",help='',type=int)
zad4_p.add_argument("n",help='',type=int)

zad5_p = subparsers.add_parser('5')
zad5_p.add_argument("N",help='',type=int)

zad5_p = subparsers.add_parser('timer')

args = arg_parser.parse_args()

zadania={"1":zadanie1,"2":lambda a:print(zadanie2(a)),"3":zadanie3,"4":zadanie4,"5":zadanie5,"timer":zadanie1_checkTimes}
zadania[args.zadanie](args)
