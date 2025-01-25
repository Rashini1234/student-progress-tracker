print ("\nPart 01")

# Function to get credit input from the user
def get_credit(data):    
    while True:
        try:
            # Prompt user for credit input (pass, fail, defer)
            credit = int(input(f'Please enter your credit at {data}: '))
            # Check if the credit within the valid range
            if credit not in range(0, 121, 20):
                print('Out of range')
            else:
                return credit

        except ValueError:
            print('Integer required')

# initialize counts and empty list to store results
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
outcome_list = []
            
# Function to calculate results based on credits
def cal(pass_value, defer_value, fail_value):
    global progress_count, trailer_count, retriever_count, exclude_count
    # Calculate the total credit points
    total = pass_value + defer_value + fail_value
    
    # Check and categorize results
    if total != 120:
        print('Total incorrect')
        
    elif pass_value == 120 and defer_value == 0 and fail_value == 0:
        print ('Progress')
        progress_count += 1
        # Append outcome details to the outcome_list
        outcome_list.append("Progress")
        outcome_list.append(pass_value)
        outcome_list.append(defer_value)
        outcome_list.append(fail_value)
        
    elif pass_value == 100 and defer_value in range(20, -1, -20) and fail_value in range(0, 21, 20):
        print('Progress (module trailer)')
        trailer_count += 1
        outcome_list.append("Progress (module trailer)")
        outcome_list.append(pass_value)
        outcome_list.append(defer_value)
        outcome_list.append(fail_value)
       
    elif pass_value in range (80,-1,-20) and defer_value in range (120,-1,-20) and fail_value in range (60,-1,-20):
        print ('Do not progress - module retriever')
        retriever_count += 1
        outcome_list.append("Do not progress - module retriever")
        outcome_list.append(pass_value)
        outcome_list.append(defer_value)
        outcome_list.append(fail_value)
       
    elif pass_value in range (40,-1,-20) and defer_value in range (40,-1,-20) and fail_value in range (80,121,20):
        print('Exclude')
        exclude_count += 1
        outcome_list.append("Exclude")
        outcome_list.append(pass_value)
        outcome_list.append(defer_value)
        outcome_list.append(fail_value)
    else:
        print('Invalid input. Try another')

# Loop to get input from staff or students
while True:
    staff_student = input("Staff or Student: ")
    # Input for staff
    if staff_student.lower() == "staff":
        # Loop for staff input
        while True:
            pass_value = get_credit("pass")
            defer_value = get_credit("defer")
            fail_value = get_credit("fail")
            cal(pass_value, defer_value, fail_value)
            # Ask for more entries or exit
            more_entries = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            while more_entries.lower() not in ["y", "q"]:
                more_entries = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")

            if more_entries.lower() == "q":
                break
        break
    
    # Input for students
    elif staff_student.lower() == "student":
        pass_value = get_credit("pass value")
        defer_value = get_credit("defer value")
        fail_value = get_credit("fail value")
        cal(pass_value, defer_value, fail_value)
        break
    else:
        print("Invalid input.")

# Histogram part for staff results        
if staff_student.lower() == "staff":
    # Import graphics module and create a histogram
    from graphics import *
    max_count = max(progress_count, trailer_count, retriever_count, exclude_count)

    # Drawing the histogram
    def draw_histogram():
        win = GraphWin("Histogram", 600, 600)

        heading = Text(Point(200, 30), 'Histogram Results')
        heading.setSize(20)
        heading.setStyle("bold")
        heading.setTextColor("grey")
        heading.draw(win)

        x_axis = Line(Point(40, 500), Point(550, 500))
        x_axis.setOutline("grey")
        x_axis.draw(win)

        progress_bar = Rectangle(Point(50, 500), Point(150, 500 - (420 / max_count) * progress_count))
        progress_bar.setOutline("grey")
        progress_bar.setFill("darkolivegreen1")
        progress_bar.draw(win)

        trailer_bar = Rectangle(Point(170, 500), Point(270, 500 - (420 / max_count) * trailer_count))
        trailer_bar.setOutline("grey")
        trailer_bar.setFill("green")
        trailer_bar.draw(win)

        retriever_bar = Rectangle(Point(290, 500), Point(390, 500 - (420 / max_count) * retriever_count))
        retriever_bar.setOutline("grey")
        retriever_bar.setFill("lightgoldenrod3")
        retriever_bar.draw(win)

        exclude_bar = Rectangle(Point(410, 500), Point(510, 500 - (420 / max_count) * exclude_count))
        exclude_bar.setOutline("grey")
        exclude_bar.setFill("orange")
        exclude_bar.draw(win)

        progress_num = Text(Point(100, 500 - ((420 / max_count) * progress_count) - 20), str(progress_count))
        progress_num.setFill("grey")
        progress_num.draw(win)
        trailer_num = Text(Point(220, 500 - ((420 / max_count) * trailer_count) - 20), str(trailer_count))
        trailer_num.setFill("grey")
        trailer_num.draw(win)
        
        retriever_num = Text(Point(340, 500 - ((420 / max_count) * retriever_count) - 20), str(retriever_count))
        retriever_num.draw(win)
        retriever_num.setFill("grey")
        exclude_num = Text(Point(460, 500 - ((420 / max_count) * exclude_count) - 20), str(exclude_count))
        exclude_num.setFill("grey")
        exclude_num.draw(win)

        progress_text = Text(Point(100, 500 + 10), "Progress")
        progress_text.setFill("grey")
        progress_text.setStyle("bold")
        progress_text.draw(win)

        trailer_text = Text(Point(220, 500 + 10), "Trailer")
        trailer_text.setFill("grey")
        trailer_text.setStyle("bold")
        trailer_text.draw(win)

        retriever_text = Text(Point(340, 500 + 10), "Retriever")
        retriever_text.setFill("grey")
        retriever_text.setStyle("bold")
        retriever_text.draw(win)

        exclude_text = Text(Point(460, 500 + 10), "Excluded")
        exclude_text.setFill("grey")
        exclude_text.setStyle("bold")
        exclude_text.draw(win)

        total_outcome = progress_count + trailer_count + retriever_count + exclude_count
        total_text = Text(Point(150, 540), f"{total_outcome} outcomes in total")
        total_text.setFill("grey")
        total_text.setStyle("bold")
        total_text.draw(win)

        win.getMouse()
        win.close()

    # Function call to draw the histogram
    draw_histogram()

    print("\nPart 02")

    # Display the results in the list
    for i in range (0,len(outcome_list),4):
        print(outcome_list[i],"-", outcome_list[i+1],",", outcome_list[i+2],",", outcome_list[i+3])

    print("\nPart 03")

    # Write results to a text file   
    f = open('outcome.txt', 'w')            
    for i in range (0,len(outcome_list),4):
        f.write(str(outcome_list[i])+" - "+str(outcome_list[i+1])+" , "+str(outcome_list[i+2])+" , "+ str(outcome_list[i+3]))
        f.write("\n")
    f.close()
    # Read and display results from the text file
    f = open('outcome.txt', 'r')
    for line in f:
        print(line.strip())


        



