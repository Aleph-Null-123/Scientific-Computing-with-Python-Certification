import copy
import random
class Hat:
  def __init__(self,**kwargs):
    self.contents = []
    self.co = []
    for key,value in kwargs.items():
      for i in range (value):
        self.contents.append(key)
        self.co.append(key)
  
  def draw(self,num_to_draw):
    self.contents = copy.deepcopy(self.co)
    if num_to_draw>len(self.co):
      return self.co
    else:
      self.drawn = []
      self.index_num = len(self.co)-1
      for i in range (num_to_draw):
        if self.index_num>0:
          self.r = random.randint(0,self.index_num)
        else:
          self.r = 0
        self.drawn.append(self.contents[self.r])
        self.index_num-= 1
        self.contents.remove(self.contents[self.r])

      return self.drawn

def experiment(**kwargs):#hat, expected_balls, num_balls_drawn, num_experiments):
  args_dict = kwargs#.items()
  m = 0
  hat = args_dict['hat']
  expected_balls = args_dict['expected_balls']
  num_balls_drawn = args_dict['num_balls_drawn']
  num_experiments = args_dict['num_experiments']

  for i in range (num_experiments):
    lot = hat.draw(num_balls_drawn)
    x = 0
    for key,value in expected_balls.items():
      if lot.count(key)>=value:
        x+=1
    if x==len(expected_balls):
      m+=1

  return m/num_experiments
