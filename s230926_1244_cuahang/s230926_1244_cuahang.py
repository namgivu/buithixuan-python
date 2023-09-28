import json

cuahang_d = {
  'ten'      : 'CircleBTX',
  'tongtien' : 0,

  'mathang_list': [
    {
      'ten'     : 'migoi',
      'soluong' : 48,
      'gia'     : 6000,
    },

    {
      'ten'     : 'quanao',
      'soluong' : 24,
      'gia'     : 120000,
    },

    {
      'ten': 'giaydep',
      'soluong' : 36,
      'gia'     : 80000,
    },
  ],
}

print(cuahang_d)
print()
print(json.dumps(cuahang_d, indent=2))
print()
print('Moi ban chon mathang')


db=122