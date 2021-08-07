import csv

with open('lifeExpect.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    first_five = []

    def get_top_five():

        line_count = 1
        while line_count < 6:
            first_five.append(data[line_count][3])
            line_count += 1

        print(first_five)

    get_top_five()

    # for row in data:
    # print(row[0])
