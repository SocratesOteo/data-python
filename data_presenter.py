
open_file=open("CupcakeInvoices.csv")

for line in open_file:
    line = line.strip()
    line = line.split(",")
    print(line)
    #cupcake_time = float(line[2])
    quantity = float(line[3])
    price = float(line[4])
    total = quantity * price
    
print(round(total))

