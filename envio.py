# -*- coding: utf-8 -*-
import sys
from socket import *
from threading import Thread
from threading import Condition
from mensagem import Mensagem
from ringbuffer import RingBuffer
import time

class Envio:

	def __init__(self, host, port, tamanhoJanela):
		self.host = host
		self.port = port
		self.tamanhoJanela = tamanhoJanela
		self.ultimoEnviado = -1
		self.ultimoRecebido = -1
		self.reenviados = 0
		self.buffer = RingBuffer(self.tamanhoJanela)
		self.socketCliente = iniciaSocketCliente()
		self.condition = Condition()
		self.enviando = True

	def iniciaSocketCliente():
		try:
			socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			socketCliente.setblocking(0)
		except socket.error:
			sys.exit()
	
		return socketCliente

	def getBuffer(self):
		return self.buffer

	def getTamanhoJanela(self):
		return self.tamanhoJanela

	def getUltimoEnviado(self):
		return self.ultimoEnviado

	def setUltimoEnviado(self, ultimoEnviado):
		self.ultimoEnviado = ultimoEnviado

	def getUltimoRecebido(self):
		return self.ultimoRecebido

	def setUltimoRecebido(self, ultimoRecebido):
		self.ultimoRecebido = ultimoRecebido

	def getTotalReenviados(self):
		return self.reenviados

	def sumTotalReenviados(self):
		self.reenviados++

	def getSocket(self):
		return self.socketCliente

	def getCondition(self):
		return self.condition

	def enviaMensagem(self, mensagem):
		time.sleep(1)
		self.socketCliente.sendto(mensagem, (self.host, self.port))

	def getEnviando(self):
		return self.enviando

	def setEnviando(self, enviando):
		self.enviando = enviando
	
class PreparacaoBuffer(thread):

	def __init__(self, mensagens, envio):
		Thread.__init__(self)
		self.mensagens = mensagens
		self.condition = envio.getCondition()
		self.buffer = envio.getBuffer()
		self.envio = envio

	def run(self):
		i = -1
		while True:
			while True:
				self.condition.acquire()
				while True:
					i++
					if not mensagens[i].getAdicionadaBuffer():
						break;
				if self.buffer.hasSpace():
					self.buffer.insere(mensagens[i])
					mensagens[i].setAdicionadaBuffer(True)
				else:
					break
			if self.buffer.isEmpty():
				break;

			self.condition.notify()
			self.condition.release()

		self.transmissor.setEnviando(False)
		self.condition.notify()
		self.condition.release()
			

class GerenciamentoEnvios(Thread):

	def __init__(self, mensagens, envio, tout):
		Thread.__init__(self)
		self.condition = transmissor.getCondition() #remover?
		self.buffer = envio.getBuffer() #remover?
		self.socketCliente = envio.getSocket() #remover?
		self.envio = envio
		self.mensagens = mensagens

	def run(self):
		numQuadro = 0
		socket = [self.socketCliente]
		primeiroEnvio = True
		noAck = True
		enviarMensagem = False
		ACKsRecebidos = RingBuffer(2 * self.envio.getTamanhoJanela())
		mensagensEnviadas = RingBuffer(self.envio.getTamanhoJanela())
		i = -1

		while True:
			self.condition.acquire()
			while True:
				if not self.buffer.hasSpace():
					if primeiroEnvio:
						if noAck:
							i++
							self.envio.enviaMensagem(self.mensagens[i])
							ent, sai, exc = select.select(socket, [], [], tout)

							if ent: #recebeu resposta
								resposta, endereco = self.sock.recvfrom(1024)
# 								MD5Mensagem = resposta[:32]
# 								quadro = int(resposta[32:40])
# 								if not self.transmissor.confereMD5Mensagem(resposta[32:40], MD5Mensagem):
# 									print "MD5 não confere"
# 									continue

# 								print "Conexão iniciada"
# 								tempoInicio = time.time()
# 								NACK = False
# #							"Caso não tenha recebido resposta, temporização dispara"
# 							else:
# 								print "Expirou timeout"
# 								continue
						
# 						"Recebe dados lidos do buffer"		
# 						dados = self.filaCircular.get()
						
# 						"Envia a primeira janela de dados"
# 						for i in xrange(self.transmissor.getTamanhoJanela()):
# 							numQuadro += 1
# 							print "Enviando", numQuadro
# 							mensagem = self.transmissor.colocaCabecalho(dados[i], numQuadro)
# 							if not dados[i] == '':
# 								self.transmissor.enviaMensagem(mensagem)
# 							mensagensEnviadas.insere(mensagem)
# 							self.transmissor.setLFS(numQuadro)
#							primeiroEnvio = False
					else:
						# naoPrimeiroEnvio()


# 	"Coloca o cabeçalho na mensagem"
# 	def colocaCabecalho(self, mensagem, numQuadro):
# 		quadro = "{0:0>8}".format(numQuadro)
# 		checksumMD5 = str(self.geraMD5Mensagem(quadro + mensagem))		
# 		mensagem = checksumMD5 + quadro + mensagem
		
# 		return mensagem
	
# 	"Gera MD5 para arquivo de entrada"
# 	def geraMD5(self, arquivo):
# 		return hashlib.md5(open(arquivo).read()).hexdigest()
	
# 	"Gera MD5 para a mensagem enviada"
# 	def geraMD5Mensagem(self, mensagem):
# 		return hashlib.md5(mensagem).hexdigest()
	
# 	"Confere se o MD5 da mensagem é o mesmo informado no cabeçalho"
# 	def confereMD5Mensagem(self, mensagem, MD5):
# 		return str(hashlib.md5(mensagem).hexdigest()) == MD5