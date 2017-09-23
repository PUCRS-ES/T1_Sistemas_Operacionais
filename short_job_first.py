TROCA_CONTEXTO = 2
tempo_atual = 1


class Processo():
    def __init__(self, dados):
        dados = dados.split(' ')
        self.tempo_chegada = int(dados[0])
        self.tempo_execucao = int(dados[1])
        self.prioridade = int(dados[2])
        self.concluido = None
        self.inicio_da_execucao = None
        self.id = dados[3]

    def __str__(self):
        str1 = "Tempo chegada: " + str(self.tempo_chegada) + "\n"
        str2 = "Tempo execucao: " + str(self.tempo_execucao) + "\n"
        str3 = "Prioridade: " + str(self.prioridade) + "\n"
        str4 = "Concluido: " + str(self.concluido) + "\n"
        str5 = "Id: " + self.id + "\n"
        str6 = "Inicio da execucao: " + str(self.inicio_da_execuca) + "\n"
        return str1 + str2 + str3 + str4 + str5 + str6

    def tempo_resposta(self):
        print "Tempo de resposta: " + str(self.inicio_da_execucao - self.tempo_chegada) + "\n"

    def tempo_turn_around(self):
        print "Tempo de turn around: " + str(self.concluido - self.tempo_chegada) + "\n"

    def tempo_espera(self):
        print "Tempo de espera: " + str(tempo_atual - self.tempo_execucao - self.tempo_chegada)


with open("arquivos_para_teste/trab-so1-teste1.txt", "r") as file:
    entrada = file.read().split('\n')
    numero_processos = int(entrada[0])
    tamanho_fatia_tempo = int(entrada[1])

    print numero_processos
    print tamanho_fatia_tempo
    lista_de_processos = []
    for i in range(0, numero_processos):
        print entrada[i + 2]
        lista_de_processos.append(Processo(entrada[i + 2] + " " + str(i + 1)))

    saida = ""
    while len(filter(lambda x: x.concluido is None, lista_de_processos)) > 0:
        apenas_processos_nao_concluidos = filter(lambda x: x.concluido is None, lista_de_processos)
        apenas_processos_iniciados = filter(
            lambda x: x.tempo_chegada <= tempo_atual,
            apenas_processos_nao_concluidos
        )
        processos_ordenados_por_tempo_necessario = sorted(
            apenas_processos_iniciados,
            key=lambda x: x.tempo_execucao
        )
        processos_com_menor_tempo = filter(
            lambda x: x.tempo_execucao == processos_ordenados_por_tempo_necessario[0].tempo_execucao,
            processos_ordenados_por_tempo_necessario
        )
        processos_com_menor_tempo_e_maior_prioridade = sorted(
            processos_com_menor_tempo,
            key=lambda x: x.prioridade
        )

        if len(processos_com_menor_tempo_e_maior_prioridade) == 0:
            saida += "-"
            tempo_atual += 1
        else:
            processo_escolhido = processos_com_menor_tempo_e_maior_prioridade[0]
            if processo_escolhido.inicio_da_execucao is None:
                processo_escolhido.inicio_da_execucao = tempo_atual

            for i in range(0, processo_escolhido.tempo_execucao):
                saida += processo_escolhido.id
                tempo_atual += 1
            processo_escolhido.concluido = tempo_atual
            saida += "TC"
            tempo_atual += TROCA_CONTEXTO

    print saida
