def hi(name, gender):
  # print('Hi ' + name + '!')
  xung_ho = 'Ms' if gender == 'f' else 'Mr'
  print(f'Hi {xung_ho} {name}!')
  print('Bye')
  print()

hi(name='Mum', gender='f')
hi(name='Dad', gender='m')
