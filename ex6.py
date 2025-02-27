class Movie:
    def __init__(self, name, genre, duration, rating, price):
        self.name = name
        self.genre = genre
        self.duration = duration
        self.rating = rating
        self.price = price

    def display(self):
        print(f"Movie: {self.name}")
        print(f"Genre: {self.genre}")
        print(f"Duration: {self.duration} minutes")
        print(f"Rating: {self.rating}/10")
        print(f"Ticket Price: ${self.price}")

class Show:
    def __init__(self, movie, showtime, seats):
        self.movie = movie
        self.showtime = showtime
        self.seats = seats

    def display_show(self):
        self.movie.display()
        print(f"Showtime: {self.showtime}")
        print(f"Available Seats: {self.seats}")

    def book_ticket(self, num_tickets):
        if num_tickets <= self.seats:
            self.seats -= num_tickets
            print(f"{num_tickets} tickets successfully booked for {self.movie.name} at {self.showtime}.")
            return True
        else:
            print("Not enough seats available!")
            return False

    def cancel_ticket(self, num_tickets):
        self.seats += num_tickets
        print(f"{num_tickets} tickets have been canceled for {self.movie.name} at {self.showtime}.")

class BookingSystem:
    def __init__(self):
        self.movies = []
        self.shows = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_show(self, show):
        self.shows.append(show)

    def display_movies(self):
        print("Available Movies:")
        for i, movie in enumerate(self.movies, start=1):
            print(f"{i}. {movie.name}")

    def choose_movie(self):
        self.display_movies()
        choice = int(input("Enter the movie number you want to see: ")) - 1
        if 0 <= choice < len(self.movies):
            return self.movies[choice]
        else:
            print("Invalid choice.")
            return None

    def display_shows(self, movie):
        print(f"\nAvailable Shows for {movie.name}:")
        for i, show in enumerate(self.shows, start=1):
            if show.movie == movie:
                show.display_show()
                print("-------------")

    def choose_show(self, movie):
        self.display_shows(movie)
        show_choice = int(input("Enter the show number you want to book: ")) - 1
        if 0 <= show_choice < len(self.shows):
            selected_show = self.shows[show_choice]
            if selected_show.movie == movie:
                return selected_show
        print("Invalid choice.")
        return None

    def book_tickets(self, show):
        num_tickets = int(input("Enter number of tickets to book: "))
        if show.book_ticket(num_tickets):
            print(f"Booking successful! You have booked {num_tickets} tickets.")
        else:
            print("Booking failed.")

    def cancel_tickets(self, show):
        num_tickets = int(input("Enter number of tickets to cancel: "))
        show.cancel_ticket(num_tickets)
        print(f"{num_tickets} tickets have been canceled.")

    def show_menu(self):
        while True:
            print("\nMovie Ticket Booking System")
            print("1. View Movies")
            print("2. Book Tickets")
            print("3. Cancel Tickets")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.display_movies()
            elif choice == '2':
                movie = self.choose_movie()
                if movie:
                    show = self.choose_show(movie)
                    if show:
                        self.book_tickets(show)
            elif choice == '3':
                movie = self.choose_movie()
                if movie:
                    show = self.choose_show(movie)
                    if show:
                        self.cancel_tickets(show)
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Sample Movies
    movie1 = Movie("Avengers: Endgame", "Action/Sci-Fi", 181, 8.4, 15)
    movie2 = Movie("The Lion King", "Animation/Adventure", 118, 8.5, 12)
    movie3 = Movie("Joker", "Crime/Drama", 122, 8.5, 10)

    # Sample Shows
    show1 = Show(movie1, "12:00 PM", 50)
    show2 = Show(movie1, "3:00 PM", 30)
    show3 = Show(movie2, "1:00 PM", 40)
    show4 = Show(movie2, "4:00 PM", 60)
    show5 = Show(movie3, "2:00 PM", 70)
    show6 = Show(movie3, "5:00 PM", 25)

    # Booking System Initialization
    booking_system = BookingSystem()
    booking_system.add_movie(movie1)
    booking_system.add_movie(movie2)
    booking_system.add_movie(movie3)
    booking_system.add_show(show1)
    booking_system.add_show(show2)
    booking_system.add_show(show3)
    booking_system.add_show(show4)
    booking_system.add_show(show5)
    booking_system.add_show(show6)

    # Start Menu
    booking_system.show_menu()
