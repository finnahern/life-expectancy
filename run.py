import csv

with open('lifeExpect.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    def get_user_input():
        """
        Prompt the user to select which data they want sorted and displayed
        """

        while True:
            print("Please select the data you wish to sort by entering a number between 1 and 5.")
            print("1. Life Expectancy")
            print("2. Adult Mortality")
            print("3. Infant Mortality")
            print("4. GDP")
            print("5. Schooling\n")

            selection = input()

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
            input_int = int(selection)
            if input_int > 5 or input_int < 1:
                raise ValueError("Please enter a number between 1 and 5")

        except ValueError:
            print("Input must be a number between 1 and 5!\n")
            return False

        return True

    def sort_data(selection):
        """
        Sort the .csv file into a list of country names and life expectancy
        values. Sort these by life expectancy values and display the top five.
        """
        print(f"sort_data called, selection is: {selection}")
        #Refactor to include all columns with a for loop
        data_category = ""
        data_col = 0
        if selection == 1:
            data_category = "life expectancy"
            data_col = 3
        elif selection == 2:
            data_category = "adult mortality"
            data_col = 4
        elif selection == 3:
            data_category = "infant mortality"
            data_col = 5
        elif selection == 4:
            data_category = "GDP"
            data_col = 12
        elif selection == 5:
            data_category = "average years of schooling"
            data_col = 15

        print(f"data_col is: {data_col}")
        print(f"data_category is: {data_category}")

        data_list = []
        for row in data[1:]:
            line = [row[0], row[data_col]]
            data_list.append(line)

        data_list.sort(key=lambda x: x[1], reverse=True)
        data_list = data_list[:5]

        print("The top five countries for life expectancy in 2015 are:")
        for x in range(5):
            print(f"{(x + 1)}. {data_list[x][0]}    {data_list[x][1]}")

    def main():
        """
        Main function to take and pass arguments to the other
        functions as required
        """

        selection = get_user_input()
        sort_data(selection)

main()
