import csv

with open('lifeExpect.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    def get_top_five():
        """
        Sort the .csv file into a list of country names and life expectancy
        values. Sort these by life expectancy values and display the top 5.
        """

        print("Creating Life expectancy array...")
        life_expect_list = []
        for row in data[1:]:
            line = [row[0], row[3]]
            life_expect_list.append(line)

        life_expect_list.sort(key=lambda x: x[1], reverse=True)
        life_expect_list = life_expect_list[:5]

        print("The top five countries for life expectancy in 2015 are:")
        for x in range(5):
            print(f"{(x + 1)}. {life_expect_list[x][0]}    {life_expect_list[x][1]}")

    get_top_five()
