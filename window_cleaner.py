import time

class House():
    '''Class representing a house which take windows and condition as integers
    tp be used in window cleaning simulation'''

    condition_dict = {1:"Clean", 2:"Dirty", 3:"Very Dirty", 4:"stinking"}

    dirtyness_sleep = {"Clean": 5, "Dirty": 6, "Very Dirty": 7, "stinking": 9}

    def __init__(self, windows, condition):
        self.windows = windows
        self.condition = House.condition_dict[condition]
        
    def clean_windows(self):
        cleaning_time = House.dirtyness_sleep[self.condition] + self.windows
        print(f"It will take {cleaning_time}"
              f" seconds, to clean {self.windows} windows which are {self.condition}")
        time.sleep(cleaning_time)
        print("Cleaned")

    def __str__(self) -> str:
        if self.condition is not None:
            return(f"{self.windows}, {self.condition}")
        else:
            return("You windows are clean")
        
def checking(message):
     for x in message:
        time.sleep(1)
        print(x, end="", flush=True)
     
def main():     
    while True:
        windows = int(input("How many windows in your house"))#
        if windows > 50:
            print("Number of windows must be under 50, sorry")
            continue
        else:
            break

    while True:
        try:
            dirtyness = int(input("Ok, can you tell me the dirtyness on a scale of 1 - 4: "))
            if 1 <= dirtyness <= 4:
                break  # Exit the loop if the input is within the valid range
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


    house = House(windows, dirtyness)
    print(f"Ok they are {house.condition}...checking time to clean...")
    checking("checking.. ")
    house.clean_windows()
    print("Thanks for using this simulator now closing....")
    time.sleep(5)

if __name__ == "__main__":
    main()
          
     





