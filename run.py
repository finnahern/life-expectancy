import csv


class data_category:
    """
    Creates an instance of the data category class to store the name and
    description of the selected statistics.
    """
    def __init__(self, name, info):
        self.name = name
        self.info = info

        def get_name(self):
            return(self.name)

        def get_info(self):
            return(self.info)


with open('lifeExpect.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    def get_user_input():
        """
        Prompt the user to select which data they want sorted and displayed
        """
        # while loop to repeat request for input until valid selection is entered.
        while True:
            print("Please select the data you wish to sort by entering a number between 1 and 13.")
            # for loop to print list of data categories the user can choose from.
            for x in range(13):
                print(f"{x + 1}. {data[0][x + 3]}")

            selection = input()
            selection = int(selection)

            if validate_input(selection):
                print("Data is valid!")
                break

        return selection

    def validate_input(selection):
        """
        Check that the user input is an integer within the specified range.
        If not display an error message and continue While loop in
        get_user_input.
        """

        try:
            if selection > 13 or selection < 1:
                raise ValueError("Please enter a number between 1 and 13")

        except ValueError:
            print("Input must be a number between 1 and 13!\n")
            return False

        return True

    def sort_data(selection):
        """
        Sort the .csv file into a list of country names and life expectancy
        values. Sort these by life expectancy values and display the top five.
        """
        print(f"sort_data called, selection is: {selection}")

        # create data_list out of the countries column and the column of the selected data.
        data_list = []
        for row in data[1:]:
            row[selection + 2] = float(row[selection + 2])
            line = [row[0], row[selection + 2]]
            data_list.append(line)

        # sort data_list in descending order and make a list of the top 5.
        data_list.sort(key=lambda x: x[1], reverse=True)
        data_list_top = data_list[:5]

        # sort data_list in ascending order and make a list of the bottom 5.
        data_list_bottom = data_list[-5:]
        data_list_bottom.sort(key=lambda x: x[1])

        # print a list of the top 5 countries in the selected category.
        print(f"\nThe top five countries for {data[0][selection + 2]} in 2015 are:")
        for x in range(5):
            print(f"{(x + 1)}. {data_list_top[x][0]}    {data_list_top[x][1]}")

        # print a list of the bottom 5 countries in the selected category.
        print(f"\nThe bottom five countries for {data[0][selection + 2]} in 2015 are:")
        for x in range(5):
            print(f"{(x + 1)}. {data_list_bottom[x][0]}    {data_list_bottom[x][1]}")

    def main():
        """
        Main function to take and pass arguments to the other
        functions as required
        """

        selection = get_user_input()
        sort_data(selection)

main()
