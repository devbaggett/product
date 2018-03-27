# Assignment title
print "\n----------Assignment: Product----------\n"

# instantiate class: "Project" with attributes
class Product(object):
	# this method to run every time a new object is instantiated
	def __init__(self, price, item_name, weight, brand, tax_rate):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "For Sale"
		self.tax_rate = tax_rate

	# method for selling item that changes status once sold
	def sell(self):
		self.status = "Sold"
		return self

	# method for adding tax to price
	def addTax(self):
		self.price = self.price * (1 + self.tax_rate)
		return self

	# method for returning item based on certain criteria
	def item_return(self, reason):
		self.reason = reason
		if self.reason == "Defective":
			self.status = "Defective"
			self.price = 0
		elif self.reason == "Unopened":
			self.status = "For Sale"
		elif self.reason == "Opened":
			self.status = "Used"
			self.price = self.price - (self.price * .20)
		return self

	# displays info about item in console
	def displayInfo(self):
		print "Price: ${}".format(self.price)
		print "Item Name: {}".format(self.item_name)
		print "Weight: {}lb".format(self.weight)
		print "Brand: {}".format(self.brand)
		print "Status: {}".format(self.status)
		print "Tax rate: {}%".format(self.tax_rate * 100)
		return self

# instantiate Product objects
product1 = Product(1, "Widgit", 5, "Acme Co", .15)
product2 = Product(1, "Widgit", 5, "Acme Co", .12)
product3 = Product(1, "Widgit", 5, "Acme Co", .15)

# product separator
print "\n-----Product1-----"
# displays sell() and add() methods for product1
product1.sell().addTax().displayInfo()

print "\n-----Product2-----"
# displays that the item was returned "open"
product2.item_return("Opened").displayInfo()

print "\n-----Product3-----"
# displays that the item is for sale
product3.displayInfo()

# bottom separator
print ""