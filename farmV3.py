import discord
from discord.ext import commands
from discord import app_commands

# Codigo com falha!

id_do_servidor = 459881865390719001

class CustomClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
        print(f'Entramos como {self.user}.')

aclient = CustomClient()
tree = app_commands.CommandTree(aclient)


@tree.command(guild=discord.Object(id=id_do_servidor), name='farm', description='Vamos Calcular.')
async def farm(interaction):
    await interaction.send('--- Farm total = Cápsulas + Pólvoras ---')
    farm_total = await get_user_input(interaction, 'Qual a quantidade total de Farm que você quer calcular?')
    farm = farm_total - (farm_total * 50 / 100)  # 50%
    await interaction.send(f'Farm 50%: {farm:.2f}')

    while True:
        await interaction.send('Escolha uma das opções:\n[1] G36\n[2] Advanced\n[3] M4\n[4] AK-47\n[5] Thompson\n[6] MTAR21\n[7] Machine')
        opcao = await get_user_input(interaction, 'Qual sua opção?')
        farm_calculo = await get_user_input(interaction, 'Quanto do farm você quer trocar?')

        if opcao == 1:
            muni_g36 = farm_calculo / 12
            await interaction.send(f'Total de Muni G36: {muni_g36:.2f}')
        elif opcao == 2:
            muni_advanced = farm_calculo / 11
            await interaction.send(f'Total de Muni Advanced: {muni_advanced:.2f}')
        elif opcao == 3:
            muni_m4 = farm_calculo / 10
            await interaction.send(f'Total de Muni M4: {muni_m4:.2f}')
        elif opcao == 4:
            muni_ak47 = farm_calculo / 9
            await interaction.send(f'Total de Muni AK-47: {muni_ak47:.2f}')
        elif opcao == 5:
            muni_thompson = farm_calculo / 8
            await interaction.send(f'Total de Muni Thompson: {muni_thompson:.2f}')
        elif opcao == 6:
            muni_mtar21 = farm_calculo / 7
            await interaction.send(f'Total de Muni MTAR21: {muni_mtar21:.2f}')
        elif opcao == 7:
            muni_machine = farm_calculo / 6
            await interaction.send(f'Total de Muni Machine: {muni_machine:.2f}')
        else:
            await interaction.send(f'Erro, Você escolheu uma opção inválida. Reinicie o comando se deseja continuar.')
            await interaction.send(f'Obrigado!!')
            break   

        continuar = await get_user_input(interaction, 'Deseja fazer outro cálculo? (S/N): ')
        if continuar.lower() != 's':
            await interaction.send(f'Obrigado!!')
            break  # Sai do loop se a resposta não for 's'

async def get_user_input(ctx, message):
    await ctx.send(message)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    response = await tree.wait_for('message', check=check)
    try:
        return int(response.content)
    except ValueError:
        return response.content

aclient.run('')
