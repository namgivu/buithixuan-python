namsinh = input('Nhap namsinh: ')
print(f'{namsinh=}')

import datetime
namhientai = datetime.datetime.now().year
print(f'{namhientai=}')

tuoi = namhientai - int(namsinh)
print(f'{tuoi=}')
