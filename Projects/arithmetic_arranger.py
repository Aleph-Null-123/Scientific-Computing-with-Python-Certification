import re

def arithmetic_arranger(problems,display_answers=False):
  num_set = ['0','1','2','3','4','5','6','7','8','9']
  op_set = ['+','-']
  first_nums = []
  second_nums = []
  operators = []
  answers = []
  if len(problems)>5:
    return 'Error: Too many problems.'  
  for problem in problems:
    p = list(problem)
    if '*' in p or '/' in p:
      return "Error: Operator must be '+' or '-'."
  for problem in problems:
    prblem = problem.replace(" ","")
    p=list(prblem)
    for i in p:
      if str(i) not in num_set and str(i) not in op_set:
        return 'Error: Numbers must only contain digits.'
  for problem in problems:
    x = re.split('\s',problem)
    if len(x[0])>4 or len(x[2])>4:
      return 'Error: Numbers cannot be more than four digits.'        
  for problem in problems:
    addition = False
    subtraction = False
    num1 = 0
    num2 = 0
    x = re.split("\s", problem)
    if x[1]=='+':
      addition = True
      subtraction = False
      operators.append("+")
    if x[1]=='-':
      addition = False
      subtraction = True
      operators.append("-")
    n1 = list(x[0])
    count1=0
    for digit in n1:
      index = num_set.index(digit)
      dex = len(n1) - (count1+1)
      num1+= (index*(10**dex))
      #print(digit,index,dex)
      count1+=1
    n2 = list(x[2])
    count2=0
    for digit in n2:
      index = num_set.index(digit)
      dex = len(n2) - (count2+1)
      num2+= (index*(10**dex))
      #print(digit,index,dex)
      count2+=1    
    if addition:
      answer = num1+num2
    if subtraction:
      answer = num1-num2

    first_nums.append(num1)
    second_nums.append(num2) 
    #print(num1,num2)
    #print(n1,n2) 
    answers.append(answer)

  larger_numbers = []
  smaller_numbers = []
  line1ns = []
  for problem in problems:
    num1=0
    num2=0
    x = re.split("\s", problem)
    n1 = list(x[0])
    count1=0
    for digit in n1:
      index = num_set.index(digit)
      dex = len(n1) - (count1+1)
      num1+= (index*(10**dex))
      #print(digit,index,dex)
      count1+=1
    n2 = list(x[2])
    count2=0
    for digit in n2:
      index = num_set.index(digit)
      dex = len(n2) - (count2+1)
      num2+= (index*(10**dex))
      #print(digit,index,dex)
      count2+=1

    if num1>num2:
      larger_number = num1
      smaller_number = num2
  
    else:
      larger_number = num2
      smaller_number = num1
    if num2>num1:
        line1ns.append(2+(len(str(larger_number))-len(str(smaller_number))))
    else:
        line1ns.append(2)
    larger_numbers.append(larger_number)
    smaller_numbers.append(smaller_number)

  line1list = []
  for i in range (len(problems)):
    x = str((' '*(line1ns[i]))+str(first_nums[i]))
    if i!=0:
      line1list.append(' '*4)
    line1list.append(x)
  line1 = ''.join(line1list)
  line1 = ''.join(line1)
  
  line2list = []

  for i in range (len(problems)):
    numspacel2 = 0
    if first_nums[i]<second_nums[i]:
      numspacel2 = 1
    else:
      numspacel2 = (1+(len(str(first_nums[i]))-(len(str(second_nums[i])))))

    x = str(operators[i]+(" "*numspacel2)+str(second_nums[i]))

    if i!=0:
      line2list.append(' '*4)
    line2list.append(x)
  line2 = ''.join(line2list)
  line2 = ''.join(line2)

  line3list = []

  for i in range (len(problems)):
    x = str("-"*(len(str(larger_numbers[i]))+2))
    if i!=0:
      line3list.append(' '*4)
    line3list.append(x)
  line3 = ''.join(line3list)
  line3 = ''.join(line3)
  line4list = []

  for i in range(len(problems)):
    ans = str(answers[i])
    ns = ((len(str(larger_numbers[i]))+2)) - len(ans)
    x = str(' '*ns+ans)
    if i!=0:
      line4list.append(' '*4)
    line4list.append(x)
  line4 = ''.join(line4list)
  line4 = ''.join(line4)
  #print(first_nums,second_nums,operators,answers,larger_numbers,smaller_numbers,line1ns)
  if display_answers:
    arranged_problems = (line1+'\n'+line2+'\n'+line3+'\n'+line4)
    return arranged_problems
  else:
    arranged_problems = (line1+'\n'+line2+'\n'+line3)
    return arranged_problems