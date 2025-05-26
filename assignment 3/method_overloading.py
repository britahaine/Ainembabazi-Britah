
class Booking:
    def calculate_cost(self, nights, rate, discount=1):
        total = nights * rate*discount
        print(total)

booking = Booking()
booking.calculate_cost(1,80,3)
booking.calculate_cost(2, 20) 