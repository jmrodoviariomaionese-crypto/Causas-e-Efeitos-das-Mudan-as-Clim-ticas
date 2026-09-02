import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

# =========================
# CONFIGURAÇÃO
# =========================

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("O token do Discord não foi encontrado no arquivo .env!")

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Prefixo dos comandos
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# =========================
# FATOS
# =========================

negative_facts = [
    "A queima de carvão, petróleo e gás libera gases de efeito estufa que aquecem o planeta.",
    "A maior parte da eletricidade do mundo ainda depende de combustíveis fósseis.",
    "A fabricação de cimento, aço, plástico e outros produtos libera grandes quantidades de gases de efeito estufa.",
    "Cerca de 12 milhões de hectares de florestas são destruídos todos os anos.",
    "O desmatamento libera o carbono armazenado nas árvores e reduz a capacidade das florestas de absorver CO₂.",
    "Carros, caminhões, navios e aviões movidos a combustíveis fósseis são grandes fontes de emissões.",
    "A produção de alimentos libera CO₂, metano e outros gases de efeito estufa.",
    "A criação de gado contribui para as mudanças climáticas principalmente por causa das emissões de metano.",
    "Prédios residenciais e comerciais consomem mais de metade da eletricidade mundial.",
    "O consumo excessivo de roupas, eletrônicos, plástico e outros produtos aumenta as emissões de gases de efeito estufa.",
    "A última década foi a mais quente já registrada.",
    "Ondas de calor estão se tornando mais frequentes e intensas em muitas regiões.",
    "Temperaturas mais altas aumentam os riscos de doenças relacionadas ao calor.",
    "O calor e as condições mais secas podem aumentar o risco de incêndios florestais.",
    "O Ártico está aquecendo muito mais rapidamente do que a média global.",
    "O aquecimento global pode tornar algumas tempestades e chuvas extremas mais intensas.",
    "O aumento das temperaturas pode agravar períodos de seca em várias regiões.",
    "A falta de água pode prejudicar plantações, animais e ecossistemas.",
    "O oceano absorve a maior parte do excesso de calor causado pelo aquecimento global.",
    "A água do oceano se expande quando esquenta, contribuindo para o aumento do nível do mar.",
    "O derretimento de geleiras e mantos de gelo também contribui para o aumento do nível do mar.",
    "O aumento do nível do mar ameaça comunidades que vivem em áreas costeiras e ilhas.",
    "O oceano absorve CO₂, mas isso aumenta sua acidez e ameaça muitos organismos marinhos.",
    "O aquecimento dos oceanos pode causar o branqueamento dos recifes de coral.",
    "As mudanças climáticas estão alterando os habitats de muitas espécies.",
    "Cerca de 1 milhão de espécies estão ameaçadas de extinção devido a diversos fatores, incluindo as mudanças climáticas.",
    "Mudanças climáticas e eventos extremos podem reduzir a produção de alimentos.",
    "Secas, enchentes e ondas de calor podem prejudicar a agricultura e a criação de animais.",
    "As mudanças climáticas podem aumentar riscos para a saúde, incluindo doenças, calor extremo e desnutrição.",
    "Eventos relacionados ao clima deslocaram, em média, cerca de 23 milhões de pessoas por ano entre 2010 e 2019.",
    "As mudanças climáticas podem destruir casas, empregos e meios de subsistência, aumentando o risco de pobreza.",
    "As concentrações de gases de efeito estufa estão em níveis muito altos na história recente.",
    "As pessoas estão enfrentando as mudanças climáticas de diversas maneiras.",
    "Cada aumento no aquecimento global é importante.",
    "Enfrentamos um grande desafio, mas já conhecemos muitas soluções.",
    "Podemos pagar a conta agora ou pagar caro no futuro.",
    "O mundo está se aquecendo rapidamente."
]


# =========================
# SOLUÇÕES
# =========================

solutions_list = [
    "Usar energia solar e eólica pode reduzir a dependência de combustíveis fósseis.",
    "Economizar eletricidade ajuda a reduzir as emissões de gases de efeito estufa.",
    "Usar transporte público, bicicletas ou caminhar pode diminuir as emissões dos veículos.",
    "Usar carros elétricos pode reduzir as emissões provenientes do transporte.",
    "Proteger as florestas ajuda a preservar o carbono armazenado nas árvores.",
    "Plantar e cuidar de árvores pode ajudar a remover CO₂ da atmosfera.",
    "Reduzir o desperdício de alimentos diminui as emissões relacionadas à produção e ao descarte de comida.",
    "Reciclar e reutilizar materiais pode reduzir a necessidade de produzir novos produtos.",
    "Consumir menos produtos desnecessários pode diminuir o impacto ambiental.",
    "Usar aparelhos e lâmpadas mais eficientes pode reduzir o consumo de energia.",
    "Melhorar o isolamento dos edifícios pode diminuir a energia necessária para aquecimento e resfriamento.",
    "Investir em energias renováveis pode ajudar a substituir carvão, petróleo e gás.",
    "Reduzir o desmatamento é uma das formas de proteger os ecossistemas e reduzir emissões.",
    "Agricultura sustentável pode ajudar a reduzir o impacto ambiental da produção de alimentos.",
    "Reduzir o uso excessivo de plástico pode diminuir a poluição e o consumo de recursos.",
    "Proteger os oceanos e os recifes de coral ajuda a preservar importantes ecossistemas.",
    "Criar cidades com mais áreas verdes pode ajudar a reduzir o calor urbano.",
    "A educação climática pode ajudar as pessoas a entenderem e adotarem ações sustentáveis.",
    "Governos podem criar políticas para reduzir emissões e incentivar tecnologias limpas.",
    "Empresas podem reduzir suas emissões usando energia renovável e processos mais eficientes.",
    "Cada pequena ação pode contribuir para a redução das emissões quando milhões de pessoas participam.",
    "Investir em tecnologias limpas pode ajudar a combater as mudanças climáticas.",
    "Reduzir o consumo de combustíveis fósseis é essencial para diminuir as emissões de gases de efeito estufa.",
    "Podemos enfrentar as mudanças climáticas combinando ações individuais, políticas públicas e inovação tecnológica."
]


# =========================
# EVENTOS
# =========================

@bot.event
async def on_ready():
    print("=" * 40)
    print(f"Bot conectado como: {bot.user}")
    print(f"ID: {bot.user.id}")
    print("=" * 40)


# =========================
# COMANDOS
# =========================

@bot.command()
async def fato(ctx):
    """Envia um fato aleatório sobre mudanças climáticas."""

    fato_aleatorio = random.choice(negative_facts)

    embed = discord.Embed(
        title="🌍 Fato sobre o clima",
        description=fato_aleatorio
    )

    await ctx.send(embed=embed)


@bot.command()
async def solucao(ctx):
    """Envia uma solução aleatória para ajudar o planeta."""

    solucao_aleatoria = random.choice(solutions_list)

    embed = discord.Embed(
        title="🌱 Solução",
        description=solucao_aleatoria
    )

    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    """Mostra a latência do bot."""

    latencia = round(bot.latency * 1000)

    await ctx.send(f"🏓 Pong! `{latencia}ms`")


@bot.command()
async def ajuda(ctx):
    """Mostra os comandos disponíveis."""

    embed = discord.Embed(
        title="🤖 Comandos do bot",
        description="Aqui estão os comandos disponíveis:"
    )

    embed.add_field(
        name="🌍 !fato",
        value="Mostra um fato aleatório sobre mudanças climáticas.",
        inline=False
    )

    embed.add_field(
        name="🌱 !solucao",
        value="Mostra uma solução para ajudar o planeta.",
        inline=False
    )

    embed.add_field(
        name="🏓 !ping",
        value="Mostra a latência do bot.",
        inline=False
    )

    embed.add_field(
        name="❓ !ajuda",
        value="Mostra esta mensagem.",
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def oi(ctx):
   await ctx.sent("opa cara :) o que voce precisa hoje?")

# =========================
# INICIAR BOT
# =========================

bot.run(TOKEN)
