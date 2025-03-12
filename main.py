from math import log
# A to the power of x equals' B
# solve for x
def main():
    print(solve_for_ex(4,1024))

def solve_for_ex(a,b):
  # orginal method to solve problem
  """
    ex = 0
    for i in range(0,b):
        if b == a ** i:
            return i
    return ex
  """
  return round(log(b,a))
    
main()
