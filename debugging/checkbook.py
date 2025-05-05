class Checkbook:
	def __init__(self):
		"""
		Description de la fonction :
			Initialise un nouveau chéquier avec un solde initial de 0,00 $.

		Paramètres :
			Aucun

		Retour :
			Aucun
		"""
		self.balance = 0.0

	def deposit(self, amount):
		"""
		Description de la fonction :
			Ajoute le montant spécifié au solde et affiche le nouveau solde.

		Paramètres :
			amount (float) : Montant à déposer. Doit être un nombre positif.

		Retour :
			Aucun
		"""
		self.balance += amount
		print("Deposited ${:.2f}".format(amount))
		print("Current Balance: ${:.2f}".format(self.balance))

	def withdraw(self, amount):
		"""
		Description de la fonction :
			Retire le montant spécifié du solde si les fonds sont suffisants.

		Paramètres :
			amount (float) : Montant à retirer. Doit être un nombre positif.

		Retour :
			Aucun
		"""
		if amount > self.balance:
			print("Insufficient funds to complete the withdrawal.")
		else:
			self.balance -= amount
			print("Withdrew ${:.2f}".format(amount))
			print("Current Balance: ${:.2f}".format(self.balance))

	def get_balance(self):
		"""
		Description de la fonction :
			Affiche le solde actuel du chéquier.

		Paramètres :
			Aucun

		Retour :
			Aucun
		"""
		print("Current Balance: ${:.2f}".format(self.balance))

def main():
	"""
	Description de la fonction :
		Fonction principale de l'application. Permet à l'utilisateur de déposer,
		retirer, consulter le solde ou quitter le programme.

	Paramètres :
		Aucun

	Retour :
		Aucun
	"""
	cb = Checkbook()
	print("Bienvenue dans l'application Chéquier.")
	print("Commandes disponibles : deposit, withdraw, balance, exit\n")

	while True:
		action = input("Que souhaitez-vous faire ? (deposit, withdraw, balance, exit) : ").strip().lower()

		if action == 'exit':
			print("Au revoir !")
			break

		elif action == 'deposit':
			try:
				amount = float(input("Entrez le montant à déposer : $"))
				if amount < 0:
					print("Vous ne pouvez pas déposer un montant négatif.")
				else:
					cb.deposit(amount)
			except ValueError:
				print("Entrée invalide. Veuillez entrer une valeur numérique.")

		elif action == 'withdraw':
			try:
				amount = float(input("Entrez le montant à retirer : $"))
				if amount < 0:
					print("Vous ne pouvez pas retirer un montant négatif.")
				else:
					cb.withdraw(amount)
			except ValueError:
				print("Entrée invalide. Veuillez entrer une valeur numérique.")

		elif action == 'balance':
			cb.get_balance()

		else:
			print("Commande invalide. Veuillez réessayer (deposit, withdraw, balance, exit).")

if __name__ == "__main__":
	main()
