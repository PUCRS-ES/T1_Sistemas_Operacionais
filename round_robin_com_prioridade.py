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


with open("arquivos_para_teste/trab-so1-teste3.txt", "r") as file:
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
    processo_anterior = None
    while len(filter(lambda x: x.concluido is False, lista_de_processos)) > 0:
        apenas_processos_nao_concluidos = filter(lambda x: x.concluido is False, lista_de_processos)
        apenas_processos_iniciados = filter(
            lambda x: x.tempo_chegada <= tempo_atual,
            apenas_processos_nao_concluidos
        )
        processos_ordenados_por_prioridade = sorted(
            apenas_processos_iniciados,
            key=lambda x: x.prioridade
        )

        if len(processos_ordenados_por_prioridade) == 0:
            saida += "-"
        else:
            apenas_processos_com_prioridade_maxima = filter(
                lambda x: x.prioridade <= processos_ordenados_por_prioridade[0].prioridade,
                processos_ordenados_por_prioridade
            )

            if processo_anterior in apenas_processos_com_prioridade_maxima:
                apenas_processos_com_prioridade_maxima.remove(processo_anterior)

            for processo in apenas_processos_com_prioridade_maxima:
                for i in range(0, tamanho_fatia_tempo):
                    # Pega o processo com a maior prioridade no momento
                    processo_atual = processo

                    # Se o processo atual for diferente do instante anterior, registra a troca
                    # de contexto e marca que perdeu 2 seg trocando de contexto
                    # if processo_anterior is not None and processo_atual.id != processo_anterior.id:
                    #     saida += "TC"
                    #     tempo_atual += TROCA_CONTEXTO

                    # Registra qual processo realizou trabaho, desconta seu tempo, e aumenta
                    # o tempo decorrido
                    saida += processo_atual.id
                    processo_atual.tempo_execucao -= 1
                    tempo_atual += 1

                    # Se o processo fez todo o trabalho, marca como concluido e muda de contexto
                    if processo_atual.tempo_execucao == 0:
                        processo_atual.concluido = True
                        saida += "TC"
                        tempo_atual += TROCA_CONTEXTO

                processo_anterior = processo_atual
                saida += "TC"
                tempo_atual += TROCA_CONTEXTO

    print saida
