file = open("filename.bin", "rb")
# Lendo dados do arquivo binário
data = file.read()
file.close()
# Gravando dados no arquivo binário
file = open("filename.bin", "wb")
file.write(data)
file.close()