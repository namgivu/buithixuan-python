print('Chao ban, toi la chatbot v0.1 !')

while True:
  m = input('> ').lower()  # m aka message
  
  if m == 'q':
    print('Tambiet')
    break

  elif m == 'chao':
    print('Chao ban')

  elif m == 'hi':
    print('Chao ban')
    
  elif m == 'xin chao':
    print('Chao ban')
  elif m == 'xin chao' or m == 'chao'  or m == 'hi':
    print('Chao ban')

  elif m in [
    'xin chao', 'chao', 'chao ban',
    'hi', 'hello', 
    'hola', 'bonjour', 'hallo', "kon'nichiwa",
  ]:
    print('Chao ban')
    
  else:
    print('Xinloi khong hieu')
  