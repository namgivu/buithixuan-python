import random 

sobimat = random.randint(0,10)
print(f'{sobimat=}')

solan = 0
while True:
  sodoan = input(f'\nMoi ban doan lan {solan+1}/4 : ')
  print(f'{sodoan=}')
  
  sobimat = int(sobimat)
  sodoan  = int(sodoan)
  
  if sobimat == sodoan:
    print('Doan dung roi! Tam biet.')
    break
    
  else:
    print('Chua dung')
    
    # goiy nhohon/lonhon
    if sobimat < sodoan:           print('So ban lonhon')
    if           sodoan < sobimat: print('So ban nhohon')

  # solan = solan + 1
  solan  += 1
  if solan == 4:
    print('Da het 4 lan doan. Tam biet')
    break
    