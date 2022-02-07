class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.balance = 0
  
  def __str__(self):
    self.stp = ''
    self.foobar = (30 - len(self.category))//2
    self.stp+=('*'*self.foobar+self.category+'*'*self.foobar+'\n')
    self.total = 0
    for item in self.ledger:
      og_amount = item['amount']
      og_desc = item['description']
      if og_desc == '':
        og_desc = ' '
      new_desc = ''
      new_amount = ''
      self.total+= og_amount
      if len(og_desc)>23:
        temp = list(og_desc)
        temp2 = temp[0:23]
        new_desc = ''.join(temp2)
      else:
        new_desc = og_desc
      
      if len(str(og_amount))>7:
        temp = list(str(og_amount))
        temp2 = temp[0:7]
        new_amount = ''.join(temp2)
      else:
        new_amount = str(og_amount)
      
      if '.' not in list(new_amount):
        new_amount+='.00'

      foobarbaz = 30 - len(str(new_amount)) - len(new_desc)
      self.stp+=(new_desc+' '*foobarbaz+str(new_amount)+'\n')
    
    self.stp+=('Total: '+str(self.total))
    return self.stp
        

  def deposit(self, d_amount, d_description=''):
    self.d_amount = d_amount
    self.d_description = d_description
    self.ledger.append({'amount':self.d_amount, 'description': self.d_description})

  def withdraw(self,w_amount,w_description = ''):
    self.w_amount = w_amount
    self.w_description = w_description
    if self.check_funds(self.w_amount):
      self.ledger.append({'amount':(self.w_amount)*(0-1), 'description': self.w_description})
      return True
    else:
      return False
  
  def get_balance(self):
    self.balance = 0
    for thing in self.ledger:
      self.balance+=thing['amount']
    return self.balance
  

  def transfer(self, t_amount, category2):
    self.t_amount = t_amount
    self.category2 = category2
    if self.check_funds(self.t_amount):
      self.withdraw(self.t_amount, "Transfer to "+self.category2.category)
      self.category2.deposit(self.t_amount,"Transfer from "+self.category)
      return True
    else:
      return False

  def check_funds(self,c_amount):
    self.get_balance()
    self.c_amount = c_amount
    if self.c_amount<=self.balance:
      return True
    else:
      return False


def create_spend_chart(categories):
  spent_num = []
  total_spent = 0
  percent_spent = []
  for category in categories:
    c_spent = 0
    for item in category.ledger:
      if item['amount']<0:
        c_spent-=item['amount']
      else:
        continue
    spent_num.append(c_spent)
  
  for item in spent_num:
    total_spent+=item
  for item in spent_num:
    p=(item/total_spent)*100
    p/=10
    p//=1
    p*=10
    percent_spent.append(p)
  
  hundred = []
  ninety = []
  eighty = []
  seventy = []
  sixty = []
  fifty = []
  forty = []
  thirty = []
  twenty = []
  ten = []
  zero = []

  for num in percent_spent:
    if num>=100:
      hundred.append('o  ')
    else:
      hundred.append('   ')
  for num in percent_spent:
    if num>=90:
      ninety.append('o  ')
    else:
      ninety.append('   ')
  for num in percent_spent:
    if num>=80:
      eighty.append('o  ')
    else:
      eighty.append('   ')
  for num in percent_spent:
    if num>=70:
      seventy.append('o  ')
    else:
      seventy.append('   ')
  for num in percent_spent:
    if num>=60:
      sixty.append('o  ')
    else:
      sixty.append('   ')
  for num in percent_spent:
    if num>=50:
      fifty.append('o  ')
    else:
      fifty.append('   ')
  for num in percent_spent:
    if num>=40:
      forty.append('o  ')
    else:
      forty.append('   ')
  for num in percent_spent:
    if num>=30:
      thirty.append('o  ')
    else:
      thirty.append('   ')
  for num in percent_spent:
    if num>=20:
      twenty.append('o  ')
    else:
      twenty.append('   ')
  for num in percent_spent:
    if num>=10:
      ten.append('o  ')
    else:
      ten.append('   ')
  for num in percent_spent:
    if num>=0:
      zero.append('o  ')
    else:
      zero.append('   ')
  
  hundred = ''.join(hundred)
  ninety = ''.join(ninety)
  eighty = ''.join(eighty)
  seventy = ''.join(seventy)
  sixty = ''.join(sixty)
  fifty = ''.join(fifty)
  forty = ''.join(forty)
  thirty = ''.join(thirty)
  twenty = ''.join(twenty)
  ten = ''.join(ten)
  zero = ''.join(zero)
  
  longest_len = 0

  for category in categories:
    if len(category.category)>longest_len:
      longest_len = len(category.category)
    else:
      continue
  
  categories2 = []
  
  for category in categories:
    categories2.append(category.category+(' '*(longest_len-len(category.category))))

  legend = ''
  for i in range (longest_len):
    legend = legend+"\n     "
    for category in categories2:
      legend = legend+(category[i])+'  '


  return ("Percentage spent by category\n100| "+hundred+"\n 90| "+ninety+"\n 80| "+eighty+"\n 70| "+seventy+"\n 60| "+sixty+"\n 50| "+fifty
  +"\n 40| "+forty+"\n 30| "+thirty+"\n 20| "+twenty+"\n 10| " +ten +"\n  0| " +zero+ "\n    "+'---'*(len(categories))+'-'+legend)
