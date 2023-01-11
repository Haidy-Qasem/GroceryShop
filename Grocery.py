import csv
from csv import DictWriter
import pandas as pd


while True:
	
	 		 
	print("                                  Welcome to ITI Grocery\n")
	print("For Customer mode press 1\nFor Owner mode press 2\nTo Exit press 0")
	n=input("Enter your mode\n")
	if n== '0' :
		x=0
		print("                                End of Processs")
		break
	elif n=='1': 
		bill=0	
		z=input("Please Enter 1 again for shopping process\n")
		if z=='1':
			final_data = pd.DataFrame({
			'Product_Name':["Apple","Banana","Orange"],
			' Product Price':["20","35","22"],
			' Quantity':["50","30","20"]})
			final_data.to_csv('file.csv')
			print(final_data)
			k=str(input("Enter Product name:\n"))
			m=int(input("Choose no.of products:\n"))
			s=int(input("Enter the previous Price\n"))
			price=int(m*s)
			bill+=price
				
			print("***********************************************************Bill***********************************************************\n")
			print("products:",k)
			print("product price:",s)
			print("product quantity:",m)
			print("Bill:",bill)
			print("                                End of Processs")
			y=input("Do you want to continue?yes/no\n")			
			if y=='yes':
				while True:
					k=str(input("Enter Product name:\n"))
					m=int(input("Choose quantity of products:\n"))
					s=int(input("Enter the previous Price:\n"))
					bill=int(m*s)
					y=input("Do you want to continue?yes/no\n")	
					if y=='no':
						break
		
	elif n=='2' :
		p=input("Enter the owner Password:\n") #pass=123
		if p=='123':
			print("*****************************************************Products & Price*****************************************************")
			while True:
				print("To Show Products & Prices Press1\nTo Add new Products Press2")
				x=input("Enter Owner Mode")
				if x=='1':
					final_data = pd.DataFrame({
					'Product_Name':["Apple","Banana","Orange"],
					' Product_Price':["20","35","22"],
					' Quantity':["50","30","20"]})
					final_data.to_csv('file.csv')
					print(final_data)
				
				if x=='2':
					New_Data=input("Enter what you want to add:(Product:Price:Quantity)")
					file3 = open('file.csv', 'w')
					with open('file.csv', 'a') as f_object:
						final_data = pd.DataFrame({
						'Product_Name':["Apple","Banana","Orange"],
						' Product_Price':["20","35","22"],
						' Quantity':["50","30","20"]})
						final_data.to_csv('file.csv')
						f= csv.writer(object)
						f.writerow(New_Data)
						object.close()
		
		else:
			print("Wrong Password\nPlease Re-Enter your Password")
	else:
		print("Wrong Choice")
