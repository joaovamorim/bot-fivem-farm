
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # Ativar a intenção de mensagen

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name= 'farm', help= 'Vamos calcular.')
async def farm(ctx):
    await ctx.send('--- Farm total = Cápsulas + Pólvoras ---')
    farm_total = await get_user_input(ctx, 'Qual a quantidade total de Farm que você quer calcular?')
    farm = farm_total - (farm_total * 50 / 100)  # 50%
    await ctx.send(f'Farm 50%: {farm:.2f}')
    

    while True:
        await ctx.send('Escolha uma das opções:\n[1] G36\n[2] Advanced\n[3] M4\n[4] AK-47\n[5] Thompson\n[6] MTAR21\n[7] Machine')
        opcao = await get_user_input(ctx, 'Qual sua opção?')
        farm_calculo = await get_user_input(ctx, 'Quanto do farm você quer trocar?')

        if opcao == 1:
            muni_g36 = farm_calculo / 12
            await ctx.send(f'Total de Muni G36: {muni_g36:.2f}')
        elif opcao == 2:
            muni_advanced = farm_calculo / 11
            await ctx.send(f'Total de Muni Advanced: {muni_advanced:.2f}')
        elif opcao == 3:
            muni_m4 = farm_calculo / 10
            await ctx.send(f'Total de Muni M4: {muni_m4:.2f}')
        elif opcao == 4:
            muni_ak47 = farm_calculo / 9
            await ctx.send(f'Total de Muni AK-47: {muni_ak47:.2f}')
        elif opcao == 5:
            muni_thoompson = farm_calculo / 8
            await ctx.send(f'Total de Muni Thompson: {muni_thoompson:.2f}')
        elif opcao == 6:
            muni_mtar21 = farm_calculo / 7
            await ctx.send(f'Total de Muni MTAR21: {muni_mtar21:.2f}')
        elif opcao == 7:
            muni_machine = farm_calculo / 6
            await ctx.send(f'Total de Muni Machine: {muni_machine:.2f}')
        else:
            await ctx.send(f'Erro, Você escolheu uma opção inválida. Reinicie o comando se deseja continuar.')
            await ctx.send(f'Obrigado!!')
            break   

        continuar = await get_user_input(ctx, 'Deseja fazer outro cálculo? (S/N): ')
        if continuar.lower() != 's':
            await ctx.send(f'Obrigado!!')
            break  # Sai do loop se a resposta não for 's'

async def get_user_input(ctx, message):
    await ctx.send(message)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    response = await bot.wait_for('message', check=check)
    try:
        return int(response.content)
    except ValueError:
        return response.content

bot.run('')
