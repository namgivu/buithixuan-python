import json

cuahang_d = {
  'tien': 12000000,  # money

  'mathang': [  # items
    {
      'ten'    : 'mi goi',
      'gia'    : '5000',
      'soluong': '48',  # aka soluong ton kho
    },
    {
      'ten'    : 'giay dep',
      'gia'    : '120000',
      'soluong': '100',  # aka soluong ton kho
    },
    {
      'ten'    : 'quan ao',
      'gia'    : '200000',
      'soluong': '70',  # aka soluong ton kho
    },

  ],

}

print('Xin chao! Moi ban mua hang.')
# print(cuahang_d['mathang'])

# mathang_de_in = [ mh for mh in cuahang_d['mathang'] ]
mathang_de_in = [
  # [ mh['ten'], mh['gia'],  ]
  {
    'ten': mh['ten'],
    'gia': mh['gia'],
  }
  for mh in cuahang_d['mathang']
]

print(mathang_de_in)

print('\n--- json dump\n')

print(json.dumps(mathang_de_in, indent=2) )

print('\n--- in tho\n')

for mh in mathang_de_in:
  print(mh)

print('\n---\n')

for mh in mathang_de_in:
  # print(mh['ten']+' '+mh['gia']+'đ')
  print(f"{mh['ten']:<8} {mh['gia']}đ")

print('\nTambiet')
