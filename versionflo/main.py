from timeclass import Time, Alarm
import time

# Function to choose time format (12h or 24h)
def choose_format():
    while True:
        format_choice = input("Choose the time format (12h/24h): ").lower().strip()
        if format_choice in ["12h", "24h"]:  # Fix the list to be correct
            return format_choice
        print("Invalid format: please choose 12h or 24h")

# Function to set the time based on user input
def set_time():
    while True:
        try:
            hour = int(input(f"Enter hour (0-{Time.max_hour} for 24h, 1-12 for 12h): "))
            minute = int(input("Enter minutes (0-59): "))
            second = int(input("Enter seconds (0-59): "))
            
            # Additional validation for valid time ranges
            if minute < 0 or minute > 59:
                print("Invalid minute! Please enter a value between 0 and 59.")
                continue
            if second < 0 or second > 59:
                print("Invalid second! Please enter a value between 0 and 59.")
                continue

            # You can also add specific checks here for the hour based on format_choice
            return hour, minute, second  # return the valid time

        except ValueError:
            print("Invalid input! Please enter valid integers for hour, minute, and second.")

# Main function to run the program
def main():
  
    # Choose time format
    format_choice = choose_format()

    # Set the time
    hour, minute, second = set_time()

    # Create a Time object with the inputted time
    time_object = Time(hour, minute, second, format_choice)

    # Print the time
    print(f"Time set: {time_object}")

# 6. Execution of the main program
if __name__ == "__main__":
    main()
