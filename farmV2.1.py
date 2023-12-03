
print('--- Farm total = Cápsulas + Pólvoras ---')
farm_total = int(input('Quantidade total de FARM?'))

farm = farm_total - (farm_total * 50 / 100)  # 50%

while True:
    print(f'Escolha uma das opções.\n[1] G36\n[2] Advanced\n[3] M4\n[4] AK-47\n[5] Thompson\n[6] MTAR21\n[7] Machine')
    opcao = int(input('Qual sua opção?'))

    print(f'Farm 50%: {farm}')
    farm_calculo = int(input('Quanto do farm você quer trocar?'))
    if opcao == 1:
        muni_g36 = farm_calculo / 12
        print(f'Total de Muni G36: {muni_g36:.2f}')
    elif opcao == 2:
        muni_advanced = farm_calculo / 11
        print(f'Total de Muni Advanced: {muni_advanced:.2f}')
    elif opcao == 3:
        muni_m4 = farm_calculo / 10
        print(f'Total de Muni M4: {muni_m4:.2f}')
    elif opcao == 4:
        muni_ak47 = farm_calculo / 9
        print(f'Total de Muni AK-47: {muni_ak47:.2f}')
    elif opcao == 5:
        muni_thoompson = farm_calculo / 8
        print(f'Total de Muni Thompson: {muni_thoompson:.2f}')
    elif opcao == 6:
        muni_mtar21 = farm_calculo / 7
        print(f'Total de Muni MTAR21: {muni_mtar21:.2f}')
    elif opcao == 7:
        muni_machine = farm_calculo / 6
        print(f'Total de Muni Machine: {muni_machine:.2f}')
    else:
        print(f'Erro, tente novamente! Você escolheu uma opção inválida.')
        print(f'Obrigado!!')
        break

    continuar = input('Deseja fazer outro cálculo? (S/N)')
    if continuar.lower() != 's':
        print(f'Obrigado!!')
        break
