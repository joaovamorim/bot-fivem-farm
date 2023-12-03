
# Muni G36
print('--- Farm total = Cápsulas + Pólvoras ---')
farm_total = int(input('Farm total: '))


if farm_total <= 9999:
    farm = farm_total - (farm_total * 50 / 100) # 50%
    print('Farm 50%: {}'.format(farm))
elif farm_total <= 14999:
    farm = farm_total - (farm_total * 45 / 100) # 55%
    print('Farm 55%: {}'.format(farm))
elif farm_total <= 19999:
    farm = farm_total - (farm_total * 40 / 100) # 60%
    print('Farm 60%: {}'.format(farm))
elif farm_total <= 24999:
    farm = farm_total - (farm_total * 35 / 100) # 65%
    print('Farm 65%: {}'.format(farm))
elif farm_total >= 25000:
    farm = farm_total - (farm_total * 30 / 100) # 70%
    print('Farm 70%: {}'.format(farm))

print('''
[1] G36
[2] M4A1
''')
opcao = int(input('Qual sua opção? '))
if opcao == 1:
    muni_g36 = farm / 24 # 12 x 2
    print('Total de Muni G36: {}'.format(muni_g36))
elif opcao == 2:
    muni_m4a1 = farm / 16 # 8 x 2
    print('Total de Muni M4A1: {}'.format(muni_m4a1))
