import json


cuahang_d = {
  'ten' : 'CircleBTX',
  'tongtien' : 0,
  'mathang_list' : [
    {
      'ten' : 'mi goi',
      'so luong' : 48,
      'gia' : 6000
    },
    {
      'ten' : 'quan ao',
      'so luong' : 24,
      'gia' : 12000
    },
    { 'ten' : 'giay dep',
      'so luong' : 36,
      'gia' : 80000
      },
    {
      'ten' : 'mi goi',
      'so luong' : 48,
      'gia' : 6000
    },
    {
      'ten' : 'quan ao',
      'so luong' : 24,
      'gia' : 12000
    },
    { 'ten' : 'giay dep',
      'so luong' : 36,
      'gia' : 80000
      },
    {
      'ten' : 'mi goi',
      'so luong' : 48,
      'gia' : 6000
    },
    {
      'ten' : 'quan ao',
      'so luong' : 24,
      'gia' : 12000
    },
    { 'ten' : 'giay dep',
      'so luong' : 36,
      'gia' : 80000
      },
    {
      'ten' : 'mi goi',
      'so luong' : 48,
      'gia' : 6000
    },
    {
      'ten' : 'quan ao',
      'so luong' : 24,
      'gia' : 12000
    },
    { 'ten' : 'giay dep',
      'so luong' : 36,
      'gia' : 80000
      },
  ]
}

# Nạp dữ liệu từ tệp JSON


try:
  # Nạp dữ liệu từ tệp JSON
  with open('cuahang_d.json', 'r', encoding='utf-8') as f:
    cuahang_d = json.load(f)
except FileNotFoundError:
  pass

print('Moi ban chon mathang')


i = 1
for mh in cuahang_d['mathang_list']:
  # print(mh)
  print(f"{i:<2} {mh['ten']:<9} {mh['gia']}")
  i += 1

while True:
  s = input('\nchon: ')
  # s = '5'
  if s == 'q':
    print('Tam biet')
    break

  i = int(s)
  mh = cuahang_d['mathang_list'][i-1]
  print(mh['ten'], mh['gia'], mh['so luong'])

  cuahang_d['tongtien'] += mh['gia']
  print(f"{cuahang_d['tongtien']=}")

  mh['so luong'] -= 1
  print(f"{mh['ten']}, soluong={mh['so luong']}")

'''
xuất cuahang_d tệp json
khi chương trình bắt đầu sẽ nạp lại tệp này
'''
# Xuất dữ liệu cuahang_d thành tệp JSON
with open('cuahang_d.json', 'w', encoding='utf-8') as f:
  json.dump(cuahang_d, f, indent=2)


db = 122
