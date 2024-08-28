#!/usr/bin/python3
#
#
########################################################################
#                          FONTE DO SCRIPT:                            #
#   Curso: Zabbix 7.0 Academy: Zabbix Server from basic to advanced    #
#   Date: 10/02/2024                                                   #
#   Auto: Magno cerqueira                                              #
#   Email: magnopeem@gmail.com                                         #
#   trilha: Zabbix 7.0 Expert                                          #  
#   URL: https://go.hotmart.com/Q91374935B                             # 
#                                                                      # 
########################################################################
#
#
##### PACOTE NECESSARIO PARA O FUNCIONAMENTO DO SCRIPT #################
# Debian e Derivados (Ubuntu, Debian):
# apt-get install python3 python3-dev
#
##### 
#
# Red Hat e Derivados (CentOS, Fedora, RHEL):
# yum install python3 python3-dev
#
#####
#
#
# Importa os modulos que serão utilizados no script
#
import json
#
# Define uma função para ler as linhas do arquivo sem comentários
def ler_arquivo_sem_comentarios(nome_arquivo):
    linhas_sem_comentarios = []  # Inicializa uma lista vazia para armazenar as linhas sem comentários
    with open(nome_arquivo, 'r') as arquivo:  # Abre o arquivo especificado em modo de leitura
        for linha in arquivo:  # Itera sobre cada linha do arquivo
            linha = linha.strip()  # Remove espaços em branco extras do início e do fim da linha
            if linha and not linha.startswith('#'):  # Verifica se a linha não está vazia e não é um comentário
                linhas_sem_comentarios.append(linha)  # Adiciona a linha à lista de linhas sem comentários
    return linhas_sem_comentarios  # Retorna a lista de linhas sem comentários
#
# Define uma função para separar as chaves e valores das linhas
def separar_chave_valor(linhas):
    chave_valor = {}  # Inicializa um dicionário vazio para armazenar as chaves e valores
    for linha in linhas:  # Itera sobre cada linha da lista de linhas sem comentários
        partes = linha.split('=', 1)  # Divide a linha na primeira ocorrência de '='
        if len(partes) == 2:  # Verifica se a linha contém exatamente duas partes após a divisão
            chave = partes[0].strip()  # Remove espaços em branco extras do início e do fim da chave
            valor = partes[1].strip().strip('"')  # Remove espaços em branco extras e aspas do valor
            chave_valor[chave] = valor  # Adiciona a chave e o valor ao dicionário
    return chave_valor  # Retorna o dicionário com as chaves e valores
#
if __name__ == "__main__":
    #
    # Mudar o Nome e local aonde esta a configuração do ser zabbix server 
    nome_arquivo = "/etc/zabbix/zabbix_server.conf"  # Nome do arquivo de configuração do Zabbix Server
    #
    #
    linhas_sem_comentarios = ler_arquivo_sem_comentarios(nome_arquivo)  # Chama a função para ler as linhas do arquivo
    chave_valor = separar_chave_valor(linhas_sem_comentarios)  # Chama a função para separar as chaves e valores
    # Imprime as chaves e valores separados em formato JSON
    print(json.dumps([chave_valor], indent=4))
#
########################################################################
#                          FONTE DO SCRIPT:                            #
#   Curso: Zabbix 7.0 Academy: Zabbix Server from basic to advanced    #
#   Date: 10/02/2024                                                   #
#   Auto: Magno cerqueira                                              #
#   Email: magnopeem@gmail.com                                         #
#   trilha: Zabbix 7.0 Expert                                          #  
#   URL: https://go.hotmart.com/Q91374935B                             # 
#                                                                      # 
########################################################################
