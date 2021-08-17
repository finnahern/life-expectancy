# Life Expectancy statistics 

[Link to the live project deployed on Heroku](https://life-expectancy-ms3.herokuapp.com/)

 A simple command line Python application which reads a given .csv file containing data such as life expectancy, GPD, infection and immunisation rates for various diseases and other statistics for 167 countries in 2015. The program parses the file and displays the top and bottom five countries in the selected category to the user. Although only one is used, the program will in theory work with any .csv file in the correct format.

The repository includes two .csv files: lifeExpect.csv, which contains all of the data to be sorted, and lifeExpectCategories.csv, which describes each of the categories in more detail.

![Flowchart of the program logic](assets/images/flowchart.PNG)
Flowchart of the program's logic

## Features

- ### Retrieves user input

    The first screen the user is greeted with when they run the program for the first time is a list of each of the thirteen columns of the .csv file which prompts them to select a category of data they wish to sort.

![Screenshot of the get_user_input function](assets/images/screencap1.PNG)

The first version of the code for this output was a separate print statement for each line which was cumbersome and inelegant. I later refactored the code to use a for loop to pull the strings from the .csv line and print each line.

![Screenshot of the for loop to print the list of options](assets/images/screencap2.PNG)

- ### Reads .csv files

    The program features a .csv reader to parse the two .csv files and extract specific elements in order to sort them. This part of the program creates two variables, data and data_categories, which are lists containing the contents of each .csv file. Other parts of the program will reference specific indices of these lists to retrieve data from them as required.

![Screenshot of the .csv reader code](assets/images/screencap3.PNG)

- ### Validates user input

    
Once the user has entered a number to select which category they wish to sort, the validate_input function is called, using the user input as an argument. The function checks that the user input is an integer between 1 and 13 and if it isn't it repeats the while loop which asks the user for input again.

![Screenshot of the validate_input function](assets/images/screencap4.PNG)

- ### Object oriented programming

    After the user input has been successfully validated, the define_object function is called which creates an instance of the Data_category class, defined at the beginning of the program. The class has two properties, name and info.

    Name is the name of the category selected by the user, pulled from the data list using the user input from earlier to locate the correct index. Info is the string from the second .csv file which explains the selected category in more detail. 

![Screenshot of the define_object function](assets/images/screencap5.PNG)

The function prints out the name and info properties of the new instance to help the user understand the data that will be shown below. The output from the object is highlighted in yellow in the screenshot below.

![Screenshot of the define_object function](assets/images/screencap6.PNG)

- ### Data sorting algorithm

    The sort_data function creates a new list, data_list, which is made up of the column of country names and column selected by the user. This new list is then sorted by the second column and all but the top five items are removed to create the top and bottom five in the selected category, which is then displayed to the user.

![Screenshot of the sorting algorithm](assets/images/screencap7.PNG)

- ### Restart application

    Finally, the user is prompted to enter Y or N to indicate if they wish to sort another data set. Entering an upper or lower case Y will call the main function, restarting the program, likewise an upper or lower case N will exit the restart function, ending the program. Any other input will call the restart function again

## Testing

I have manually tested a number of aspects of the program, particularly the elements that require a user input to ensure all input is validated and invalid input is handled appropriately. Manual testing was undertaken both in the deployed Heroku terminal and the one in the Gitpod IDE.

### Bugs identified and fixed

A number of bugs were identified and fixed throughout developement, including:

- The sort function was returning unexpected results, only sorting the first two digits of a given number and ignoring decimal points. This would result in the output showing 9.9 as higher than 20.4. This was because all the elements in the lists that were being taken from the .csv files were strings. Once I converted the elements in the second column of the data_list variable to floats they were sorted correctly.

- An indentation error was preventing the Data_category class from initalising properly. The get_name and get_info functions were within the scope of the __ init__ function. This was a good reminder of the importance of indentation in Python.

- The validate_input function was not working correctly as the try statement was trying the compare the user input, which was a string, to 1 and 13. The input needed to be converted to an int as part of the try statement and then again in the scope of the main function before being passed to the other functions.

### Unresolved issues

There are a number of errors and inconsistencies in the data used in the lifeExpect.csv file. Examples include the fact that India appears to have had 90,387 cases of Measles per 1,000 population which would appear to be a bit high. According to the [Times of India](https://timesofindia.indiatimes.com/india/measles-cases-in-india-dropped-by-43-in-a-year-who/articleshow/60471312.cms), the country had 30,168 total cases of Measles in 2015. I decided that tracking down and correcting all of the issues with the data would be too time consuming and not relevant to the objective of creating a program that sorts .csv files.

### Validator testing

The code was validated using the [Pep8](http://pep8online.com/) validator. The only errors returned were a number of "line too long" errors, mostly in relation to comments and print statements that don't interfere with the program logic.

### Improvements to make

Future iteration on the project could add a secondary sort criteria. Right now ties between the elements in the sorted category are sorted alphabetically.

## Deployment

The project was deployed using Code Institute's Python terminal template and Heroku.

### Steps for deployment

- Create a new Heroku app
- Set the buildpacks to Python and NodeJS, in that order
- Link the Heroku app to the Github repository
- Click deploy

## Credits

### Acknowledgements

Spencer Barriball for his invaluable feedback and advice and providing the .csv file

### Data sources

https://www.kaggle.com/kumarajarshi/life-expectancy-who

### Technology used

- Python
- [Git](https://git-scm.com/) - Version control.
- [Github](https://github.com/) - Used to host repository and live site.
- [Gitpod IDE](https://gitpod.io/) - Development enviornment used to build site.
- [Pep8 validator](http://pep8online.com/) - Used to validate code and check for errors.

### Resources

- [W3Schools](https://www.w3schools.com/)