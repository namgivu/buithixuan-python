while True:
  #age = input('Nhap tuoi: ')
  age = '55'
  print(f'{age=:<}')
  
  """
  Ticket price is:
  ■ 25$  / 1 children, which is younger than 18.
  ■ 100$ / 1 adult,    18 to 60 years old.
  ■ 50$  / 1 person,   which is older than 60.
  """
  price = -1
  
  age = int(age)
  if age < 18                    : price = 25
  if       18 <= age <= 60       : price = 100
  if                    60 < age : price = 50
    
  print(f'{price=:<}')
  print(f'Gia ve la ${price}')

  break

print('Tam biet')
