# hnchs82
# 09/2021
# python 3.X + numpy
# built to the first data analisys exercise
import numpy as np
# np.set_printoptions(precision=15, floatmode='fixed')
def calculate(inputlist):
  calculations = {}
  tmp = []
  # try:
  # hchs82: discording the solution but i remove the try block because the program does not pass the test routine
  # https://forum.freecodecamp.org/t/assertionerror-valueerror-not-raised-by-calculate/433244
  # 1 - Validate de Input array
  wklist = np.array(inputlist)
  # print (len(inputlist))
  # print ('cantidad elementos', len(inputlist))
  if len(wklist) != 9:
      raise ValueError('List must contain nine numbers.')
      # raise Exception('List must contain nine numbers.')
  # 2 reshape 3x3 to literal mat3x3
  mat3x3 = wklist.reshape(3,3)
  # 3 set de iterables
  dcresult = {}
  titer = [0, 1, None] # controls the Axis if required
  dmthe = {
      "mean" : "mean",
      "var"  : "variance",
      "std"  : "standard deviation",
      "max"  : "max",
      "min"  : "min",
      "sum"  : "sum",
      }
  # 4 - Automatic routine
  # all functions have the same structure to the call, i will iterate
  for m in dmthe.keys():
      tmprs = []
      for i in titer:
          tmp = []
          concat = ''
          concat = 'mat3x3.' + str(m) + '( axis = ' + str(i) + ').tolist()'
          # print (concat) # probar a mano
          tmp = eval(concat)
          # print(tmp[0])
          tmprs.append(tmp)
      dcresult[str(dmthe[m])]=tmprs
  # set the return
  calculations = dcresult
  return calculations
  # except Exception as e:
  #   # print (str(e))
  #   # print(e)
  #   pass
  # finally:
  #   dcresult = {}
  #   tmp = []
  #   tmprs = []
  #   wklist = []
  #   titer = []