def add_time(start, duration, start_day = ''):

  num_set = ['0','1','2','3','4','5','6','7','8','9']
  day_set = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

  t_hours = 0
  t_minutes = 0
  d_hours = 0
  d_minutes = 0
  n_hours = 0
  n_minutes = 0

  time_digits = list(start)
  t_digs = 0

  AM = False
  PM = False

  if time_digits[1]==':':
    t_digs = 1
  else:
    t_digs = 2
  
  if t_digs == 1:
    t_hours = num_set.index(time_digits[0])

  elif t_digs == 2:
    temp1 = []
    temp1.append(time_digits[0])
    temp1.append(time_digits[1])
    tc1 = 1
    for digit in temp1:
      x = num_set.index(digit)
      t_hours+=x*(10**tc1)
      tc1-=1
  
  if t_digs == 1:
    temp2 = []
    temp2.append(time_digits[2])
    temp2.append(time_digits[3])
    tc2=1
    for digit in temp2:
      x = num_set.index(digit)
      t_minutes+=x*(10**tc2)
      tc2-=1
  
  if t_digs == 2:
    temp3 = []
    temp3.append(time_digits[3])
    temp3.append(time_digits[4])
    tc3=1
    for digit in temp3:
      x = num_set.index(digit)
      t_minutes+=x*(10**tc3)
      tc3-=1

  if t_digs == 1:
    if time_digits[5]=='A':
      AM=True
    else:
      PM=True
  if t_digs == 2:
    if time_digits[6]=='A':
      AM=True
    else:
      PM=True

  duration_digits = list(duration)
  d_digs = duration_digits.index(':')
  if d_digs == 1:
    d_hours = num_set.index(duration_digits[0])

  elif d_digs > 1:
    temp4 = []
    for i in range (d_digs):
      temp4.append(duration_digits[i])
    tc4 = d_digs-1
    for digit in temp4:
      x = num_set.index(digit)
      d_hours+=x*(10**tc4)
      tc4-=1
  
  if d_digs == 1:
    temp5 = []
    temp5.append(duration_digits[2])
    temp5.append(duration_digits[3])
    tc5=1
    for digit in temp5:
      x = num_set.index(digit)
      d_minutes+=x*(10**tc5)
      tc5-=1
  
  if d_digs > 1:
    temp6 = []
    temp6.append(duration_digits[d_digs+1])
    temp6.append(duration_digits[d_digs+2])
    tc6=1
    for digit in temp6:
      x = num_set.index(digit)
      d_minutes+=x*(10**tc6)
      tc6-=1
    
  DOW = (start_day.lower()).capitalize()
  if DOW in day_set:
    dow_num = day_set.index(DOW)
  
  minutes_after_12AM = 0

  if AM:
    minutes_after_12AM = (60*t_hours)+(t_minutes)
  elif PM:
    minutes_after_12AM = (60*t_hours)+(t_minutes)+720
  
  added_minutes = (60*d_hours)+d_minutes

  total_added_time = minutes_after_12AM+added_minutes

  num_days_later = total_added_time//1440

  extra_time = total_added_time%1440

  n_hours1 = extra_time//60

  n_minutes = extra_time%60
 
  time_of_day = ''

  if n_hours1>=12:
    time_of_day='PM'
  
  else:
    time_of_day='AM'

  if time_of_day=='PM':
    if n_hours1 != 12:
      n_hours = n_hours1%12
    else:
      n_hours=12
  else:
    if n_hours1==0:
      n_hours=12
    else:
      n_hours=n_hours1
  
  if DOW!='':
    temp_dow_num = num_days_later+dow_num
    if temp_dow_num>6:
      new_dow_num = temp_dow_num%7
    else:
      new_dow_num = temp_dow_num
    day_of_week = day_set[new_dow_num]

  if n_minutes<10:
    n_minutes = '0'+str(n_minutes)

  if (num_days_later>1) and (start_day!=''):
    return (str(n_hours)+":"+str(n_minutes)+" "+time_of_day+", "+day_of_week+" ("+str(num_days_later)+" days later)")
  
  elif (num_days_later==1) and (start_day!=''):
    return (str(n_hours)+":"+str(n_minutes)+" "+time_of_day+", "+day_of_week+" (next day)")

  elif (num_days_later>1) and (start_day==''):
    return (str(n_hours)+":"+str(n_minutes)+" "+time_of_day+" ("+str(num_days_later)+" days later)")

  elif (num_days_later==1) and (start_day==''):
    return (str(n_hours)+":"+str(n_minutes)+" "+time_of_day+" (next day)")

  elif (num_days_later==0) and (start_day!=''):
    return (str(n_hours)+":"+str(n_minutes)+" "+time_of_day+", "+day_of_week)

  elif (num_days_later==0) and (start_day==''):
    return (str(n_hours)+":"+str(n_minutes)+" "+time_of_day)
    #return new_time