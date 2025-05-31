import data
import functions as fun
import time

print("------ Speed Typing App ------")
go_next = True

while(go_next == True):
    level = data.Starter
    paragraph = fun.select(level)
    print("""Instruction : Just write the data as it is..""")
    print(paragraph)
    start = time.time()
    user_data = input("Enter \n->")
    end = time.time()
    error = fun.errorcount(paragraph, user_data)

    delay = fun.typing_time(start, end)
    speed1 = fun.speed(start, end, user_data)
    print("\n---- Result ----\n")
    print(f"Time Taken : {delay}")
    print(f"Speed : {speed1} word per second.")
    print(f"Error Occured = {error}")

    ask = input("Do you want to continue or not [Y or N] : ")
    if ask == "N":
        go_next = False