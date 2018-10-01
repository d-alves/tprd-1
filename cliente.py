# -*- coding: utf-8 -*-
from socket import *
from threading import Thread
from threading import Condition
from mensagem import Mensagem
from ringbuffer import RingBuffer
from envio import Envio
from envio import PreparacaoBuffer
import time


	# def insereMensagemJanelaAntigo(self, mensagem):
	# 	# to do - inserção na janela - verificar
	# 	self.mensagemAtual++
	# 	self.espacosLivres--
	# 	self.ultimoEnviado++
	# 	self.enviaMensagem(mensagem)

	# def verificaAcks(self):
	# 	entrada, saida, excecao = select.select(client_socket, [], [], TIMEOUT)
	# 	if entrada:
	# 		resposta, endereco = self.client_socket.recvfrom(1024)
		# resposta = conn.recv(1024)

	# def enviaMensagens(mensagens, tamanhoJanela):
	# 	idMensagem = 0
	# 	while(idMensagem < len(mensagens) or ultimoAck < (len(mensagens) - 1)):
	# 		while self.temEspaco and idMensagem != len(mensagens):
	# 			mensagem = mensagens[idMensagem].packMensagemParaMD5()
	# 			idMensagem++
	# 			self.insereMensagemJanelaAntigo(mensagem)

			# to do - aguardar retorno do servidor (função verificaAcks()), se não receber, reenvia
			# to do - se não houver erro, desloca janela

	# def insereMensagemJanela(self, mensagem):
	# 	self.janelaDeslizante.append(mensagem)

	# def enviaMensagens(mensagens, tamanhoJanela):
	# 	idMensagem = 0
	# 	while(idMensagem < len(mensagens) or ultimoAck < (len(mensagens) - 1)):
	# 		while(self.espacosLivres > 0 and idMensagem != len(mensagens)):
	# 			mensagem = mensagens[idMensagem].packMensagemParaMD5()
	# 			insereMensagemJanela(mensagem)

	# 			self.mensagemAtual = idMensagem
	# 			self.espacosLivres--
	# 			idMensagem++

def Main(servidor, porta, fileName, perror, socket):
	file = abreArquivo(fileName)
	linhas = criaListaLinhas(file)
	mensagens = []
	for linha in linhas:
		mensagens.append(Mensagem(linhas.index(linha), linha, perror))

	
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
	client_socket = socket(AF_INET, SOCK_DGRAM)

	nome_arquivo = raw_input("Enter a name: ")
	perror = 0.5

	Main(server_name, server_port, nome_arquivo, perror, client_socket)
	
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
