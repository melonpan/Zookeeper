duration, food_cost, flight_cost, hotel_cost = int(input()), int(input()), int(input()), int(input())

food_cost *= duration
flight_cost *= 2
hotel_cost = hotel_cost * (duration - 1)
total_cost = food_cost + flight_cost + hotel_cost

print(total_cost)
