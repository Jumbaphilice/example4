class MpesaAccount:
	def __init__(self,name,phone_number):
		self.name = name
		self.phone_number = phone_number
		self.balance = 0
		self.deposits=[]
		self.withdrawals=[]
		self.loan=0



				
	def deposit(self,amount):
		self.balance = self.balance + amount
		self.deposits.append(amount)
			print ("Dear {}, you have successfuly deposited Ksh{} into your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))
		
	def withdraw(self,amount):
		if self.balance>amount:
			self.withdrawals.append(amount)
			self.balance = self.balance - amount

			print ("Dear {}, you have successfully withdrawn Ksh{} from your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))
		else:
			print ("Sorry {}, you have insufficient funds to facilitate your withdrawal. Your current balance is Ksh{}.".format(self.name,self.balance))

	def check_balance(self):
		print ("Dear {}, your M-pesa balance is Ksh{}".format(self.name,self.balance))

	def my_deposits(self):
		for x in self.deposits:
			print(x)

	def my_withdrawals(self):
		for y in self.withdrawals:
			print(y)
	def give_loan(self,amount):
		if len(self.deposits)>=5 and amount <1/3*sum(self.deposits)and self.loan==0:
			self.loan=self.loan+amount
			print("hey {} you are qualified to get a loan of {}.".format(self.name,amount))
		else:
			print("hey {} you are not qualified to get a loan of {}.".format(self.name,amount))

	# def pay_loan(self,amount):
	# 	if self.loan==0:
	# 		print("you do not have existing loan")
	# 	elif amount<self.loan:
	# 	    self.loan=self.loan-amount
	# 	    print("Hi {} you have successfully paid part of your loan {} your remaining loan balance is {}.".format(self.name,amount,self.loan))
	# 	elif amount==self.loan:
	# 		self.loan=self.loan-amount
	# 		print("you have already paid your existing loan")
	# 	elif amount>self.loan:
	# 		more=amount-self.loan
	# 		self.balance=more+self.balance
	# 		self.loan=amount-self.loan

		



	
