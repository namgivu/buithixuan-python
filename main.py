while True:
  n = input('Nhap so: ')
  
  import re
  m = re.findall('[a-zA-Z]+', n)
  if m:
    print('Hay nhap lai')
  else:
    print(n)
    break
