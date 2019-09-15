class Item:

	def __init__(self,id,name,quantity,price):
		self.id = id
		self.name=name
		self.quantity = quantity
		self.price = price 

	def update_item(self, name = None, quantity = None, price= None):
	
		if name != None:
			self.name = name 
		if quantity != None:
			self.quantity = quantity
		if price != None:
			self.price = price 

	def add_special_price(self,special_price):
		self.special_price = special_price

	def __str__(self):
		try:
			return '{} - {}\n quantity {} ,price {}\n special_price {}'.format(self.name,self.id,self.quantity,self.price,self.special_price)
		except AttributeError:
			return '{} - {}\n quantity {} ,price {}'.format(self.name,self.id,self.quantity,self.price)