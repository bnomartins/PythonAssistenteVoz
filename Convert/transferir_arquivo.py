import os
# Listar arquivos
arquivos = os.listdir()
print(arquivos)
print('-'*50)

# Caminho do arquivo
caminho = os.getcwd()
print(caminho)
print('-'*50)

# Renomear arquivo
os.rename('teste2.xls', 'teste2.xls')
print('Arquivo renomeado')
# transferir arquivo
os.rename('teste2.xls', 'video/teste2.xls')
print("Arquivo transferido")
