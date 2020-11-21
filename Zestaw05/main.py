import functools,argparse

def zadanie1(args):
  class Bug:
    count=0
    def __init__(self):
      Bug.count+=1
      self.id = Bug.count

    def __str__(self):
      return f'{self.id} of {self.count}'

    def __del__(self):
      print(f'Koniec:: {self.id} of {Bug.count}')
      Bug.count-=1

  bugs=[]
  for i in range(args.n):
    bugs.append(Bug())
    print(bugs[-1])


def pamiec(func):
  fib_dict = {}
  @functools.wraps(func)
  def wrapper(*args,**kwargs):
    if args not in fib_dict:
      fib_dict[args] = func(*args,**kwargs)
    return fib_dict[args]
  return wrapper


@pamiec
def fibonnaci(n):
  return n if 0 <= n < 2 else fibonnaci(n-1)+fibonnaci(n-2)


if __name__=="__main__":
  arg_parser = argparse.ArgumentParser()
  subparsers = arg_parser.add_subparsers(help='numer zadania',dest='zadanie')

  zad1_p = subparsers.add_parser('1')
  zad1_p.add_argument("-n",help="liczba bugów do stworzenia",type=int,default=100)

  zad2_p = subparsers.add_parser('2')
  zad2_p.add_argument("n",help="Fn",type=int)

  
  
  args = arg_parser.parse_args()

  zadania={"1":zadanie1,"2":lambda a:print(fibonnaci(args.n))}
  zadania[args.zadanie](args)  