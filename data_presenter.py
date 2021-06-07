open_file = open('CupcakeInvoices.csv')

# for row in open_file:
#     print(row)

for row in open_file:
    row = row.strip()
    values = row.split(',')
    print(values[2])

open_file.seek(0)

for row in open_file:
    row = row.strip()
    values = row.split(',')
    total = float(values[3]) * float(values[4])
    print(round(total, 2))

open_file.seek(0)
thesum = 0
for row in open_file:
    row = row.strip()
    values = row.split(',')
    thesum += float(values[3]) * float(values[4])
print(round(thesum, 2))

open_file.close()

