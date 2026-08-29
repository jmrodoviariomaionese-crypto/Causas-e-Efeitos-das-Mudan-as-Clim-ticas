import random

def random_negative_fact():

    negative_facts = [

        # CAUSAS

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


        # EFEITOS

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

        "As mudanças climáticas podem destruir casas, empregos e meios de subsistência, aumentando o risco de pobreza."

    ]

    return random.choice(negative_facts)


input("Pressione Enter para receber um fato sobre as mudanças climáticas: ")

print(random_negative_fact())
