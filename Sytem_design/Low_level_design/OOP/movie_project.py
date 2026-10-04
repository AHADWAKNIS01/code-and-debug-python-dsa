class Movie:
    def __init__(self,movie_name,total_seats,ticket_price):
        self.movie_name=movie_name
        self.total_seats=total_seats
        self.ticket_price=ticket_price
        self.booked_seats=0

    def show_status(self):
        self.seats_available=self.total_seats-self.booked_seats
        print(f"Movies name= {self.movie_name} ")
        print(f"seats available= {self.seats_available}")
        print(f"Total booked seats are ={self.booked_seats}")
    

    

    def book_ticket(self,num_tickets):
        self.seats_available=self.total_seats-self.booked_seats
        if self.seats_available>=num_tickets:
            print("the your seat has been booked")
            print(f"the total price is ={self.ticket_price*num_tickets}")
            
            self.booked_seats+=num_tickets
        else:
            print("Sorry, not enough seats available")


s1=Movie("krish",100,400)
s1.show_status()
s1.book_ticket(10)
s1.show_status()




