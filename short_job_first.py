TROCA_CONTEXTO = 2


class Processo():
    def __init__(self, dados):
        dados = dados.split(' ')
        self.tempo_chegada = int(dados[0])
        self.tempo_execucao = int(dados[1])
        self.prioridade = int(dados[2])
        self.concluido = False
        self.id = dados[3]

    def __str__(self):
        str1 = "Tempo chegada: " + str(self.tempo_chegada) + "\n"
        str2 = "Tempo execucao: " + str(self.tempo_execucao) + "\n"
        str3 = "Prioridade: " + str(self.prioridade) + "\n"
        str4 = "Concluido: " + str(self.concluido) + "\n"
        str5 = "Id: " + self.id
        return str1 + str2 + str3 + str4 + str5


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

    tempo_atual = 1
    saida = ""
    while len(filter(lambda x: x.concluido is False, lista_de_processos)) > 0:
        apenas_processos_nao_concluidos = filter(lambda x: x.concluido is False, lista_de_processos)
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
            while processo_escolhido.tempo_execucao > 0:
                saida += processo_escolhido.id
                processo_escolhido.tempo_execucao -= 1
                tempo_atual += 1

                if processo_escolhido.tempo_execucao == 0:
                    processo_escolhido.concluido = True
                    saida += "TC"
                    tempo_atual += TROCA_CONTEXTO
                    break
    print saida
