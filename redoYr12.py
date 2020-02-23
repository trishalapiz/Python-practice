"""
Redo of Year 12 Python assessment (2016)" VERY SIMPLE PROGRAM, DOESN'T ACCOUNT FOR FULL SESSIONS
"""
#movie times, movie list and prices
movie_times = ["11am", "1:30pm", "3pm", "5pm", "7:30pm", "9pm"]
movies = ["Hunt for the Wilderpeople", "Deadpool", "Star Wars: The Force Awakens", "Captain America: Civil War", "X-Men: Apocalypse", "Me Before You", "Finding Dory", "Ghostbusters", "The Jungle Book"] #created a list of available movies the customers can watch
night_price = 10
day_price = 8

####### THINGS TO CONSIDER
# how to check if movie session is full
# get_time() is dependent on get_movie() if the "full session" is going to be incorporated
# user needs to exit at any point OR change their answers // CAN CHANGE MOVIE / TIMES BUT NOT EXIT AT ANY POINT
# assuming everyone (regardless of age) pays same price

def get_movie(): #returns chosen movie 
    print("The movies currently showing are:")
    for i in range(len(movies)):
        print(" - {} [{}]".format(movies[i], i))

    while True:
        chosen_movie = int(input("To do this, please enter a number between 0 and 8 (inclusive). Numbers at the side are there to assist you in your choice. "))
        if chosen_movie < 0 or chosen_movie > 8:
            print("Please try again.")
        else:
            return movies[chosen_movie]

def get_time(): #returns movie time
    n = int(input("Next, please choose whether you would like a daytime session (enter 1) or a nighttime session (enter 2). "))
    
    separator = ", "
    while True:
        if n < 1 or n > 2:
            print("Try aagin.")
        elif n == 1:
            day_times = movie_times[:3]
            print(separator.join(day_times))
            movie_time = int(input("Choose a movie time: (for example, 0 corresponds to {}) ".format(day_times[0])))
            return day_times[movie_time]
        elif n == 2:
            night_times = movie_times[3:]
            print(separator.join(night_times))
            movie_time = int(input("Choose a movie time: (for example, 0 corresponds to {}) ".format(night_times[0])))
            return night_times[movie_time]
        

def get_tickets(): #returns number of tickets
    
    while True:
        try:
            num_tickets = int(input("Please enter the number of tickets you wish to purchase for this session. Max number per session booking is 10. "))
            if num_tickets < 0 or num_tickets > 10:
                print("Invalid answer. Enter a number from 0 to 10. ")
            else:
                return num_tickets
        except ValueError:
            print("Enter a NUMBER between 0 and 10 (inclusive) ")


def calculate(t, n): #returns total to be paid
    day_times = movie_times[:3]
    night_times = movie_times[3:]

    if t in day_times:
        return day_price * n
    else:
        return night_price * n

    
def main(): #main simulator
    while True:
        try:
            print("Welcome to Nomad Cinemas! To book a session, please select a movie you would like to watch: ")
            print()
            movie = get_movie() #choose movie
            print()
            time = get_time() #choose time
            print()
            ask = int(input("So far, you've chosen to watch {} at {}. If you would like to make changes, press 4 to change your movie, press 5 to change your time. Otherwise, press 0. ".format(movie, time)))
            if ask == 4: #NEW MOVIE
                new_movie = get_movie()
                tickets = get_tickets() #select ticket quantity, new movie may be chosen
            elif ask == 5: #NEW TIME
                new_time = get_time()
                tickets = get_tickets() #select ticket quantity, new time may be chosen
            elif ask == 0:
                tickets = get_tickets() #select ticket quantity
            
            total = calculate(time, tickets) #calculate total of session

            print()
            print("*" * 85)
            print('                                 ', "SUMMARY:")
            if ask == 4:
                print("Movie: {}".format(new_movie))
                print("Movie time: {}".format(time))
            elif ask == 5:
                print("Movie: {}".format(movie))
                print("Movie time: {}".format(new_time))
            else:
                print("Movie: {}".format(movie))
                print("Movie time: {}".format(time))

            print("Quantity of Tickets: {}".format(tickets))
            print("Total: ${}".format(total))

            confirm = int(input("Would you like to go through with this purchase? Select 0 for YES, 1 for CANCEL. "))
            if confirm < 0 or confirm > 1:
                print("You did not follow the instruction.")
            elif confirm == 0:
                print("Thank You! Hope you enjoy your time at Nomad Cinemas!")
                break
            elif confirm == 1:
                print("Aw, that's too bad. Hope we see you next time!")
                break
        except ValueError:
            print("Please try again")

main()

