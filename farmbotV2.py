
# Codigo inutilizavel

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # Ativar a intenção de mensagen

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name= 'farm', help= 'Vamos calcular.')
async def farm(ctx):
    await ctx.send('--- Farm total = Cápsulas + Pólvoras ---')
    farm_total = await get_user_input(ctx, 'Qual a quantidade total de Farm que você quer calcular?')

    if farm_total <= 9999:
        farm = farm_total - (farm_total * 50 / 100)  # 50%
        await ctx.send(f'Farm 50%: {farm}')
    elif farm_total <= 14999:
        farm = farm_total - (farm_total * 45 / 100)  # 55%
        await ctx.send(f'Farm 55%: {farm}')
    elif farm_total <= 19999:
        farm = farm_total - (farm_total * 40 / 100)  # 60%
        await ctx.send(f'Farm 60%: {farm}')
    elif farm_total <= 24999:
        farm = farm_total - (farm_total * 35 / 100)  # 65%
        await ctx.send(f'Farm 65%: {farm}')
    elif farm_total >= 25000:
        farm = farm_total - (farm_total * 30 / 100)  # 70%
        await ctx.send(f'Farm 70%: {farm}')

    while True:
        await ctx.send('''
	        [1] G36
	    [2] M4A1
        ''')
        opcao = await get_user_input(ctx, 'Digite sua Número de sua opção. ')
        farm_calculo = await get_user_input(ctx, 'Quanto do farm você quer trocar? ')

        if opcao == 1:
            muni_g36 = farm_calculo / 12
            await ctx.send(f'Total de Muni G36: {muni_g36:.2f}')
        elif opcao == 2:
            muni_m4a1 = farm_calculo / 10
            await ctx.send(f'Total de Muni M4A1: {muni_m4a1:.2f}')

        continuar = await get_user_input(ctx, 'Deseja fazer outro cálculo? (s/n): ')
        if continuar.lower() != 's':
            await ctx.send(f'Obrigado!')
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
