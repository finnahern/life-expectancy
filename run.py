import csv

with open('lifeExpect.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    def get_top_five():
        """
        Sort the .csv file into a list of country names and life expectancy values.
        Sort these by life expectancy values and display the top 5.
        """

        print("Creating Life expectancy array...")
        life_expect_list = []
        for row in data[1:]:
            line = [row[0], row[3]]
            life_expect_list.append(line)

        life_expect_list.sort(key=lambda x: x[1], reverse=True)
        life_expect_list[1:6]
        print(life_expect_list)

        # line_count = 1
        # first_five = []
        # while line_count < 6:
        # first_five.append(data[line_count][3])
        # line_count += 1

        # print(first_five)

    get_top_five()

    # for row in data:
    # print(row[0])
