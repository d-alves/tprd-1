# -*- coding: utf-8 -*-
import hashlib
import time
import random

class Mensagem:
	
	def __init__(self, seqNum, textoMensagem, perror):
		self.seqNum = seqNum
		self.textoMensagem = textoMensagem
		self.tamanhoMensagem = self.defineTamanhoMsg()
		self.tick = self.defineTimestamp()
		self.sec = self.defineSec()
		self.nsec = self.defineNsec()
		self.codVerificacao = self.geraMD5Mensagem(perror)

	def __init__(self, seqNum, textoMensagem):
		self.seqNum = seqNum
		self.textoMensagem = textoMensagem
		self.tamanhoMensagem = self.defineTamanhoMsg()
		self.tick = self.defineTimestamp()
		self.sec = self.defineSec()
		self.nsec = self.defineNsec()

	def defineTamanhoMsg(self):
		return len(self.textoMensagem)

	def defineTimestamp(self):
		return time.time()

	def defineSec(self):
		return int(self.tick)

	def defineNsec(self):
		return self.tick - int(self.tick)

	def geraMD5Mensagem(self, perror):
		numRandom = geraNumeroAleatorio()

		if(numRandom < perror):
			concatCampos = str(self.seqNum) + str(self.sec) + str(self.nsec) + str(-1) + self.textoMensagem
		else:
			concatCampos = str(self.seqNum) + str(self.sec) + str(self.nsec) + str(self.tamanhoMensagem) + self.textoMensagem
		
		return hashlib.md5(concatCampos.encode('utf-8')).hexdigest()[:16]

	def geraNumeroAleatorio(self):
		return random.uniform(0, 1)

	def packMensagemParaMD5(self):
		formato = '!2QIH' + str(tamanhoMensagem) + 's' + str(len(self.codVerificacao)) + 's'
		return struct.pack(formato, self.seqNum, self.sec, self.nseq, self.tamanhoMensagem, self.textoMensagem, self.codVerificacao)

	def verificaMD5(self)