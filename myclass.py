class myclass:
    def __init__(self):
        self.my_fav = {'Paris': 500, 'NYC': 600}
    
    def get_extra_cost(self, dist):
        return self.my_fav.get(dist, 0)
    
    def valid_this(self, dist):
        return isinstance(dist,str)

class passagner:
    def __init__(self, num):
        self.num = num
    
    def valid_number(self):
        print("this working here")
        return isinstance(self.num,int) and self.num > 0

    def for_here_discount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num <= 10:
            return 0.2
        else:
            return 0.0

class Plane:
    def __init__(self, dist, num, duration):
        self.myclass = myclass()
        self.passanger = passagner(num)
        self.total_time = total_time(duration)
        self.dist = dist
        self.seats = 200

    def sum(self):
        if not self.myclass.valid_this(self.dist) or not self.passanger.validNumber() or not self.total_time.is_valid_total_time():
            return -1

        number_total = self.costBas
        number_total += self.myclass.get_extra_cost(self.dist)
        number_total += self.total_time.get_fee()
        number_total -= self.total_time.get_best_promo_ever()

        discount = self.passanger.forHereDiscount()
        number_total = number_total - (number_total * discount)
        
        return max(int(number_total), 0)

class total_time:
    def __init__(self, duration):
        self.duration = duration

    def is_valid_total_time(self):
        return isinstance(self.duration,int) and self.duration > 0

    def get_fee(self):
        return 200 if self.duration < 7 else 0

    def get_best_promo_ever(self):
        return 200 if self.duration> 30 else 0
    
    def get_weekend(self):
        return 100 if self.duration > 7 else 0

class vacation:
    cost_base = 1000

    def __init__(self, dist, num, duration):
        self.myclass = myclass()
        self.passagner = passagner(num)
        self.total_time = total_time(duration)
        self.dist = dist

    def sum(self):
        #sum the cost of the vacation package here
        if not self.myclass.valid_this(self.dist) or not self.passagner.valid_number() or not self.total_time.is_valid_total_time():
            return -1
        
        #sum the total cost
        number_total = self.cost_base
        number_total += self.myclass.get_extra_cost(self.dist)
        number_total += self.total_time.get_fee()
        number_total -= self.total_time.get_best_promo_ever()

        discount = self.passagner.for_here_discount()
        number_total = number_total - (number_total * discount)
        
        return max(int(number_total), 0)

#this is main function
def main():
    #this are the inputs
    dist = "Paris"
    num = 5
    duration = 10


    #this are the outputs
    calculator = vacation(dist, num, duration)
    cost = calculator.sum()

    #this will do some printing
    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")

#main event function
if __name__ == "__main__":
    main()