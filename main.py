"""
    Author: Matthew Vallance 001225832, Deanna White 001208356, Varnika Mogali 001279858, Kayleigh Harmsworth 001218868, Deeya Patel 001230057
    Purpose: Main file for running this project
    Date: 15/11/23
"""
import task_1
import task_2
import task_3
import task_4

program_running = True
print('Welcome to Group 51s COMP1828 project')  # Word this better
# While loop for a menu system for all tasks
while program_running:
    print('Chose an option from the following (input 1,2,3,4,5 for selecting an option):\n'
          '1. Task 1 - This returns the time it takes to get between two user-inputted stations and the route they would need to take.\n'
          '2. Task 2 - This returns the number of stops between two user-inputted stations and the route they would need to take.\n'
          '3. Task 3 - Revised task_2 using the Bellman Ford Algorithm\n'
          '4. Task 4 - Check feasibility of closing connections between two stations\n'
          '5. Exit program')
    # Make sure user selects a valid option, if not, user to reenter until valid option is selected
    option_selected = False
    while not option_selected:
        option_chosen = int(input('Select option: '))
        if option_chosen in [1, 2, 3, 4, 5]:
            option_selected = True
        else:
            print('Invalid option selected.')

    # Run correct code dependant on option selected
    if option_chosen == 1:
        task_1.run_task_1()
    elif option_chosen == 2:
        task_2.run_task_2()
        option_selected = False
    elif option_chosen == 3:
        task_3.run_task_3()
        option_selected = False
    elif option_chosen == 4:
        task_4.run_task_4()
        option_selected = False
    elif option_chosen == 5:
        program_running = False
