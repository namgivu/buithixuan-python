"""
chatbot v0

Chao ban, toi la chatbot v0!
> 

---
> Ban khoe khong?
Khoe, con ban?

> (con lai )
Xin loi, toi khong hieu
"""

print('Chao ban, toi la chatbot v0!')
user_chat_message = input('> ')
print('Xin loi, toi khong hieu')

while True: 
  user_chat_message = input('> ')
  print(user_chat_message)
  if user_chat_message == 'nnn':
    print('Tao hieu')
  else:
    print('Xin loi, toi khong hieu')
  