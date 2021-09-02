import numpy as np
np.set_printoptions(precision=16, floatmode='fixed')
def calculate(inputlist:list):
  calculations = {}
  try:
    # 1 - Validate de Input array
    wklist = np.array(inputlist)
    if len(wklist) != 9:
        raise ValueError('List must contain nine numbers.') # problema 2 no esta interpretando el raise error, proque?
    # 2 reshape
    mat3x3 = wklist.reshape(3,3)
    # 3 set de iterables
    dcresult = {}
    titer = [0, 1, None] # controls the Axis if required
    dmthe = {
        "mean" : "mean",
        "var" : "variance",
        "std" : "standard deviation",
        "max" : "max",
        "min" : "min",
        "sum" : "sum",
        }
    # 4 - Automatic routine
    # all functions have the same structure to the call 
    for m in dmthe.keys():
        tmprs = []
        for i in titer:
            concat = ''
            concat = 'mat3x3.' + str(m) + '( axis = ' + str(i) + ')'
            X = eval(concat)
            tmprs.append(X) 
        dcresult[str(dmthe[m])]=tmprs
    # set the return
    calculations = dcresult
    dcresult = {}
  except Exception as e:
    print (e)
  finally:
    return calculations