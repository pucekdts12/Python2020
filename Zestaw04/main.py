import argparse,ast,itertools as it

def zadanie3(args):
  nested_lists = ast.literal_eval(args.list)
  output = [ sum(l) for l in nested_lists ]
  print(output)

def zadanie4(args):
  # nie wiem o co dokłanie chodzi z tymi róznymi sposobami na stworzenie słownika
  # domyślam się że chodzi o to że można stworzyć wprost:
  d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  # albo
  # d=dict()
  # d['I']=1
  # d['V']=5 # itd.?
  r = args.roman
  


  




  

def zadanie5(args):
  input = ast.literal_eval(args.list)

  def iteracyjna(input):
    n = args.right-args.left+1
    print(input)
    for i in range(0,int(n/2))
      input[args.left+i],input[args.right-i] = input[args.right-i],input[args.left+i]
    print(input)

  def rekurencyjna(input,l,r):
    if l>=r: return
    rekurencyjna(input,l+1,r-1)
    input[l],input[r]=input[r],input[l]
    


  print("WERSJA ITERACYJNA")
  iteracyjna(input.copy()) # przekazuje kopię zeby rekurencyjna dostała oryginał
  print("WERSJA REKURENCYJNA")
  print(input)
  rekurencyjna(input,args.left,args.right)
  print(input)

  

if __name__=="__main__":
  arg_parser = argparse.ArgumentParser()
  subparsers = arg_parser.add_subparsers(help='numer zadania',dest='zadanie')

  zad3_p = subparsers.add_parser('3')
  zad3_p.add_argument("list",help="lista w formacie pythona [1,2,[3,4],...]",type=str)

  zad4_p = subparsers.add_parser('4')
  zad4_p.add_argument("roman",help="liczba w formacie rzymskim do odczytania",type=str)

  zad5_p = subparsers.add_parser('5')
  zad5_p.add_argument("list",help="lista w formacie pythona [1,2,[3,4],...]",type=str)
  zad5_p.add_argument("left",help="odkąd zacząć odwracać",type=int)
  zad5_p.add_argument("right",help="dokąd odwracać",type=int)
  
  
  args = arg_parser.parse_args()

  zadania={"3":zadanie3,"4":zadanie4,"5":zadanie5}
  zadania[args.zadanie](args)  

