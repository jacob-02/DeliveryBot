import sheet

read = sheet.read("Sheet1!A1:D10")


def find(consumer):
    for i in read:
        for j in i:
            if j == consumer:
                return i[1]

'''
def write():
    a =(sheet.read("Sheet1!C1"))
    a = int(a[0][0])
    k = 0
    while k <= 5:
        consumer_column = "Sheet1!A" + str(a) + ":A" + str(a + 1)
        food_column = "Sheet1!B" + str(a) + ":B" + str(a + 1)

        consumer1 = input("Enter you name ")
        food = input("Enter the food that you need to order ")

        sheet.write(consumer1, food)

        a += 1
        k += 1

write()
'''