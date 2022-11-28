import csv

product_list =[
	["Product Name:", "Price:", "Quantity:"],
	[ "Apple:       ", "12EGP:","  15"],
	[ "Banana:      ", "15EGP:","  30"],
	[ "Blueberry:   ", "30EGP:","  30"]
 ]
 
# file=open("product_file.csv","x")
file=open("product_file.csv","w")
writer=csv.writer(file)
writer.writerows(product_list)
