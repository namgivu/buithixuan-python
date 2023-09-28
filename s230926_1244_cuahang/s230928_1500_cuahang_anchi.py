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
# print(json.dumps(cuahang_d, indent=2))
print('Moi ban chon mathang')
# print(cuahang_d['mathang_list'])
# print(cuahang_d['mathang_list'][0])
# print(cuahang_d['mathang_list'][1])

i = 1

with open("cuahang_d.json", "r") as f:
  cuahang_d = json.loads(f.read())

for mh in cuahang_d['mathang_list']:
  # print(mh)
  print(f"{i:<2} {mh['ten']:<9} {mh['gia']}")
  i += 1

while True:
  s = input('chon: ')
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

  json_string = json.dumps(cuahang_d)

  # Open a file in write mode
  with open("cuahang_d.json", "w") as f:
    # Write the JSON string to the file
    f.write(json_string)

db = 122
