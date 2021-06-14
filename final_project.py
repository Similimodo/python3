from json import dumps, loads

#This is the final project. It is a product inventory python programming

#This class block  uses the __init special method to intialize name and price

class Product:

	def __init__(self, name, price):
		self.name = name
		self.price = price

#This function inside this product class below uses the to_dict to convert the product objects into dictionaries
	def to_dict(self):
		return {"name" : self.name, "price" : self.price}

#This function sums up the price of the whole product
def total_product_price(products):
	total = 0.0
	for i in products:
		total += i.price
	print("Your products have a total value of : $" + str(total) + "\n\n" )
#This function is used to load products that was stored in the products.json 
def load_products():
	try:
		products_file = open("products.json" , "r+")
	except FileNotFoundError:
		return []
	products_json = products_file.read()
	products_data = loads(products_json)

	products = []
	for i in products_data:
		products.append(Product(i["name"],i["price"]))
	products_file.close()
	return products

#This function below is the add product function to create a product object and append it to the product list
def add_product(name, price):
	new_product = Product(name,price)
	products.append(new_product)

#This function below creates the list of the added product
def list_products(products):
	for p in products:
		print("Product ({}): Price: ${} \n\n".format(p.name, p.price)) 

#This function is used to save our products so that when the program quits and loads back the previously stored products can be loaded back without loosing any data
def save_product(products):
	products_save_list = []
	for i in products:
		products_save_list.append(i.to_dict())

	products_file = open("products.json", "w+")
	products_file.write(dumps(products_save_list))
	products_file.close()


#This array stores any product the user adds 

products = load_products()

#This while loop gives the user the ability to add a product to the list of program and if they type quit then it breaks the program

while True:
	print("Type 'add' to add a product!")
	print("Type 'quit' to quit the program")
	print("Type 'list' to list all the products")
	print("Type 'total' to list the total value of your products")

	command = input("type a command: ")

	if command == "quit":
		save_product(products)
		break
		
	if command == "add":
		product_name = input("Enter the name of your new product: ")
		try:
			product_price = float(input("Enter the price of your new product: "))
		except ValueError:
			print("Please enter a valid price which is a number not string!")
			continue
		add_product(product_name, product_price)

	if command == "list":
		list_products(products)
	if command == "total":
		total_product_price(products)
