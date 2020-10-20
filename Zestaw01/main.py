import argparse
import sys


def zadanie1(args):
  num=args.num
  cur=num
  while cur > 0:
    print( f"{' '*((num-cur)//2)}{'*'*cur}" )
    cur-=2


def zadanie2(args):
  print([ i for i in range(0,30) if i%3!=0 ])
      

def zadanie3(args):
  end_number = args.end_number
  seg_len = len(str(end_number))+1
  ruler = f"|{'.'*seg_len}" * end_number + "|"
  labels = '0'+''.join( [ f"{i:>{seg_len+1}}"for i in range(1,end_number+1) ] )
  print(ruler)
  print(labels)
  

def zadanie4(args):
  a,b=args.a,args.b
  field = f"{'+---'*b+'+'}\n{'|   '*b+'|'}\n" * a + f"{'+---'*b+'+'}\n"
  print(field)

def zadanie5(args):
  set1,set2 = set(args.set1),set(args.set2)
  print("SET1:",set1)
  print("SET2:",set2)
  print("ILOCZYN:",set1.intersection(set2))
  print("SUMA:",set1.union(set2))
  

arg_parser = argparse.ArgumentParser()
subparsers = arg_parser.add_subparsers(help='numer zadania',dest='zadanie',required=True)

zad1_p = subparsers.add_parser('1')
zad1_p.add_argument("num",type=int,help="dlugosc podstawy piramidy")

zad2_p = subparsers.add_parser('2')

zad3_p = subparsers.add_parser('3')
zad3_p.add_argument("end_number",help="liczba do jakiej rysowac miarke",type=int)


zad4_p = subparsers.add_parser('4')
zad4_p.add_argument("a",help='bok a prostokata',type=int)
zad4_p.add_argument("b",help='bok a prostokata',type=int)

zad5_p = subparsers.add_parser('5')
zad5_p.add_argument("-set1",nargs="+",type=int,help="wartości pierwszej listy",required=True)
zad5_p.add_argument("-set2",nargs="+",type=int,help="wartości drugiej listy",required=True)

args = arg_parser.parse_args()

zadania={"1":zadanie1,"2":zadanie2,"3":zadanie3,"4":zadanie4,"5":zadanie5}
zadania[args.zadanie](args)