from cart import Item
from dealer import Dealer
import random

pencel = Item(101,"pencel",100,10)
pen = Item(102,"pen",100,10)
redpencel = Item(103,"redpencil",87,120)

dealer = Dealer(1,"apsara","bengaluru")

dealer.add_promotion(redpencel)
print(redpencel)

old_price = redpencel.price
redpencel.update_item(price=130)

if old_price < redpencel.price:
	dealer.deactivate_promotion(redpencel)
elif old_price > redpencel.price:
	decrease = old_price - redpencel.price
	percentage = (decrease / redpencel.price) *100
	print(percentage)
	if percentage > 30:
		dealer.deactivate_promotion(redpencel)

print(redpencel)