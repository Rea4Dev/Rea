# Dicionários para armazenar os conteúdos e suas respectivas contagens
conteudos_portugues = {}
conteudos_matematica = {}










# Prova1
prova1_portugues = {
    'questão1': ["Regência Verbal", "Sintaxe"],
    'questão2':[""],
    'questão3': [""],
    'questão4': [""],
    'questão5': [""],
    'questão6': [""],
    'questão7': [""],
    'questão8': [""],
    'questão9': [""],
    'questão10': [""],
    'questão11': [""],
    'questão12': [""],
    'questão13': [""],
    'questão14': [""],
    'questão15': [""],
}
prova1_matematica = {
    'questão16': [""],
    'questão17': [""],
    'questão18': [""],
    'questão19': [""],
    'questão20': [""],
    'questão21': [""],
    'questão22': [""],
    'questão23': [""],
    'questão24': [""],
    'questão25': [""],
    'questão26': [""],
    'questão27': [""],
    'questão28': [""],
    'questão29': [""],
    'questão30': [""],
}

# Prova2














for prova in [prova1_portugues]:
    for questao, conteudos in prova.items():
        for conteudo in conteudos:
            if conteudo in conteudos_portugues:
                conteudos_portugues[conteudo].append((questao, prova))
            else:
                conteudos_portugues[conteudo] = [(questao, prova)]

for prova in [prova1_matematica]:
    for questao, conteudos in prova.items():
        for conteudo in conteudos:
            if conteudo in conteudos_matematica:
                conteudos_matematica[conteudo].append((questao, prova))
            else:
                conteudos_matematica[conteudo] = [(questao, prova)]

print("Conteúdos mais cobrados em Português:")
for conteudo, questoes_provas in conteudos_portugues.items():
    n_cobrancas = len(questoes_provas)
    print(f"\n{conteudo} ({n_cobrancas} cobranças):")
    for questao, prova in questoes_provas:
        print(f"- Questão {questao} (Prova {list(prova.keys())[0]})")

print("_____________________________________________________________")

print("\nConteúdos mais cobrados em Matemática:")
for conteudo, questoes_provas in conteudos_matematica.items():
    n_cobrancas = len(questoes_provas)
    print(f"\n{conteudo} ({n_cobrancas} cobranças):")
    for questao, prova in questoes_provas:
        print(f"- Questão {questao} (Prova {list(prova.keys())[0]})")
