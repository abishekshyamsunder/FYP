from z3 import *
import sys
def getTestCase(variables, relations, parameters, type):
  i = 0
  s = Solver()
  constraint = True
  while i < len(variables):
    variable = Real(variables[i])
    if relations[i] == 'equal to':
      constraint = And(constraint, variable == parameters[i])
    if relations[i] == 'greater':
      constraint = And(constraint, variable > parameters[i])
    elif relations[i] == 'lesser':
      constraint = And(constraint, variable < parameters[i])
      constraint = And(constraint, variable > 0)
    elif relations[i] == 'greater or equal to' or relations[i] == 'atleast':
      constraint = And(constraint, variable >= parameters[i])
    elif relations[i] == 'lesser or equal to' or relations[i] == 'atmost':
      constraint = And(constraint, variable <= parameters[i])
    i += 1
  if type:
    s.add(constraint)
  else:
    s.add(Not(constraint))
  if not s.check() == sat:
    raise("Unsolvable")
  return str(s.model())

def main():
  relations = sys.argv[1]
  variables = sys.argv[2]
  parameters = sys.argv[3]

  v = []
  r = []
  p = []
  v.append(variables[:-1])
  r.append(relations[1:-1])
  p.append(parameters[:-1])
  if(sys.argv[4]=="temp.temp" or sys.argv[4]=="temp1.temp"):
    x = getTestCase(v, r, p, True)
  else:
    x = getTestCase(v, r, p, False)
  f = open(sys.argv[4],"a")
  f.write(str(x+"\n"))
  f.close()

if __name__== "__main__":
  main()