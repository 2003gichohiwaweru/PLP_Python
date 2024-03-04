lista =  input("Enter the intergers seoarated by commas: ")
interger_list = [int(x) for x in lista.split()]

sum_interger = sum(interger_list)

print("The sum of the interger is : ", sum_interger)
