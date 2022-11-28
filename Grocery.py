print("                                  Welcome to ITI Grocery\n")
x=int(input("Enter 1 for shopping process\n"))
while x==1:
	
	import csv 		 
	print("                                  Welcome to ITI Grocery\n")
	print("For Customer mode press 1")
	print("For Owner mode press 2")
	print("To Exit press 0")
	n=input("Enter your mode\n")
	if n=='0' :
		x=0
		print("                                End of Processs")
	bill=0	
	if n=='1': 
		z=int(input("Please Enter 1 again for shopping process\n"))
		while z==1:
				with open ("product_file.csv")as file3:
					for lines in file3:
						product_list=lines.strip()
						print(product_list)
				
				k=str(input("Enter Product name:\n"))
				m=int(input("Choose no.of products:\n"))
				s=int(input("Enter the previous Price\n"))
				price=int(m*s)
				bill+=price
				
				y=input("Do you want to continue?yes/no\n")	

				
				if y=='yes':
					# while True:
						k=str(input("Enter Product name:\n"))
						m=int(input("Choose quantity of products:\n"))
						s=int(input("Enter the previous Price:\n"))
						bill=int(m*s)
						y=input("Do you want to continue?yes/no\n")	
						if y=='no':
							print('''**********************Bill**********************\n''')
							print("products:",k)
							print("product price:",s)
							print("product quantity:",m)
							print("Bill:",bill)
							print("\n")
							print("                                End of Processs")
							z=0
				elif y=='no':
					print('''**********************Bill**********************\n''')
					print("products:",k)
					print("product price:",s)
					print("product quantity:",m)
					print("Bill:",bill)
					print("                                End of Processs")
					z=0
			
		
			
	if n=='2':
		p=input("Enter the owner Password:\n") #pass=123
		if p=='123':
			print("Products& Price")
			print("To show Products & Prices Press1")
			print("To change cost Press2")	
			print("To add new Products Press3")
			x=input("Enter Owner Mode")
			if x=='1':
				with open ("csv_1.csv")as file3:
					for lines in file3:
						product_list=lines.strip()
						print(product_list)
				
			# if x=='2':
				# file3=open("test.csv","r")
				
				# a=input("Enter the old Price:(Product:Old Price)")
				# b=input("Enter the new Price:(Product:New Price)")
				# file3.replace(a,b)
			
			if x=='3':
				with open ("product_file.csv")as file3:
					product_file=csv.reader(file3)
					# for row in productfile:
						# print(row)
				
					product_file=[]
					word_1=str(input("Enter what you want to add:(Product:) "))
					word_2=int(input("Enter what you want to add:(Price:) "))
					word_3=int(input("Enter what you want to add:(Quantity:)")) 
					h=[word_1,word_2,word_3]
					product_file.append(h)
					print(product_file)
					
						
						
				
		else:
			print("End of Process")