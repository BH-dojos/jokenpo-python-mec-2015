class Rodada:

	def __init__(self, jogador1, jogador2):
		self.jogador1 = jogador1
		self.jogador2 = jogador2

	def empatou(self):
		return self.jogador1 == self.jogador2

	def vencedor (self):

		dicionario = {
			"Pedra":{
				"Tesoura" : "Pedra",
				"Papel" : "Papel",
				"Pedra": None
			},
			"Tesoura": {
				"Pedra": "Pedra",
				"Papel": "Tesoura",
				"Tesoura": None
			},
			"Papel": {
				"Pedra": "Papel",
				"Tesoura": "Tesoura",
				"Papel": None
			}
		}

		return dicionario[self.jogador1][self.jogador2]


def main():
	print "digite a entrada: "

if __name__ == '__main__':
	main()