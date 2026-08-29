import random

def random_negative_fact():

    negative_facts = [

        "Uma pessoa média passa seis meses da vida esperando o sinal vermelho ficar verde.",

        "Mais pessoas morrem todos os anos por causa da queda de cocos do que por ataques de tubarão.",

        "As preguiças conseguem prender a respiração por mais tempo do que os golfinhos.",

        "Bananas são consideradas frutas vermelhas, mas morangos não são.",

        "Existem mais flamingos falsos no mundo do que flamingos reais.",

        "Cerca de 26 mil ursos polares vivem atualmente na natureza, e o aquecimento global ameaça cada vez mais suas populações.",

        "O nível do mar está subindo devido ao derretimento do gelo e à expansão da água do oceano causada pelo aquecimento.",

        "O aquecimento e a acidificação dos oceanos ameaçam os recifes de coral em todo o mundo.",

        "A Grande Barreira de Corais já passou por vários eventos de branqueamento em massa devido ao aumento da temperatura dos oceanos.",

        "A Groenlândia está perdendo grandes quantidades de gelo à medida que o clima esquenta.",

        "A Antártida está perdendo gelo, contribuindo para o aumento do nível do mar.",

        "O derretimento das geleiras ameaça o fornecimento de água doce em algumas regiões."

    ]

    return random.choice(negative_facts)

input("Pressione Enter para receber um fato negativo aleatório: ")

print(random_negative_fact())
