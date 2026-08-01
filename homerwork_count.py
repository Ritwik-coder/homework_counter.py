total_homework = 4
Original_count = total_homework

print(f"You have {Original_count} homework assignments to finish today\n")

completed_count = 0
task_num = 1

while task_num <= total_homework:
    if task_num == 1: next_task = "Math homework"
    elif task_num == 2: next_task = "Science homework"
    elif task_num == 3: next_task = "History homework"
    else: next_task = "English homework"

    answer = input(f"Have you finished {next_task}? (yes/no) ")

    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Great job! :)")
    else:
        print("Okay, finish it and check again.")

    print("Homework assignments remaining:", total_homework - completed_count)
    print()
print("=========== ALL HOMEWORK COMPLETE ===========")
print("Great job! You have completed all your homework assignments for today!\n")

print ("Now lets saffely peek at a infinite loop...")

test_value = 0
safety_counter = 0
while  test_value >= 0:
    print("This condition never changes, so this loop will run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("Safety counter has reached 3, breaking the loop to prevent an infinite loop.")
        break
print("\n=========== HOMEWORK COMPLETETION SUMMARY ===========")
print("Total homework assignments: ", Original_count)
print("Total homework assignments completed: ", completed_count)
print("Total homework assignments remaining: ", Original_count - completed_count)
print("==========================================================")