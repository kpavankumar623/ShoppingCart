
import random 
class Dealer:

	def __init__(self,id,name,contact):
		self.name = name
		self.id = id
		self.contact = contact

	def add_promotion(self,item):
		offer_per = random.randint(5,30)
		original_price = item.price
		promotion_price = original_price - (original_price/100)*offer_per
		item.add_special_price(promotion_price)

	def deactivate_promotion(self,item):
		try:
			del item.special_price
		except AttributeError:
			print("this item not in the part of promotion now.")



