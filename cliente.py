# -*- coding: utf-8 -*-
from socket import *
from mensagem import Mensagem

def Main(fileName, perror):
	file = abreArquivo(fileName)
	linhas = criaListaLinhas(file)
	mensagens = []
	for linha in linhas:
		mensagens.append(Mensagem(linhas.index(linha), linha, perror))
	for mensagem in mensagens:
		print str(mensagem.tamanhoMensagem) + ' ' + str(mensagem.sec) + ' ' + str(mensagem.nsec) + ' ' + mensagem.codVerificacao

def abreArquivo(fileName):
	file = open(fileName, "r")
	return file

def criaListaLinhas(file):
	linhas = []
	for line in file:
		linhas.append(line)
		print 'oi ' + line
	return linhas

if __name__ == "__main__":
	# Name will be translated by DNS
	# AF_INET ~ IPv4
        # DGRAM ~ UDP
	server_name = "localhost"
	server_port = 12000
	# client_socket = socket(AF_INET, SOCK_DGRAM)

	nome = raw_input("Enter a name: ")
	perror = 0.5

	Main(nome, perror)
	
	# msg = raw_input("Input lowercase sentence: ")
	
	# # Src IP addr will be attached to the packet by O.S
	# # Src port can be random. Guess why?
	# client_socket.sendto(msg, (server_name, server_port))

	# # 2048 is buffer size
	# # Connectionless; no src port
	# rcv_msg, server_addr = client_socket.recvfrom(2048)
	# print "[" + str(server_addr) + "]: " + rcv_msg

	# # Closing socket
	# client_socket.close()
