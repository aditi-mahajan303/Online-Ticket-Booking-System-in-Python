from array import *


def seat_detail():
    print("Ticket booking for the movie: ", mov[bkmov])
    print("Please have a look at the seating plan")
    print()
    seating_plan = ["1    2    3    4    5    6    7    8    9    10",
                    "11   12   13   14   15   16   17   18   19   20",
                    "21   22   23   24   25   26   27   28   29   30",
                    "31   32   33   34   35   36   37   38   39   40",
                    "41   42   43   44   45   46   47   48   49   50",
                    "51   52   53   54   55   56   57   58   59   60"]
    for x in seating_plan:
        print(x)

    print()

    print("Silver seats:    1 - 20 (per seat-130 rupees)")
    print("Gold seats:     21 - 40 (per seat-150 rupees)")
    print("Platinum seats: 41 - 60 (per seat-175 rupees)\n")


print("Welcome to 'fabfour Online Movie Ticket' Booking..!!")

print()

# movie names

mov = {1: "Dhoom", 2: "Bahubali", 3: "Harry Potter And The Philosopher's Stone", 4: "Super 30", 5: "Crazy Stupid Love"}
print("1.", mov[1])
print("2.", mov[2])
print("3.", mov[3])
print("4.", mov[4])
print("5.", mov[5])

print()

bkmov = int(input("Enter movie number: "))

print()

# seat_detail() function call
seat_detail()

no_seat = int(input("No of seats to be booked: "))

bkseat = array('i', [])

count = 0
s_amt = 0
g_amt = 0
p_amt = 0

print("Enter seat number:")
for i in range(no_seat):
    x = int(input())

    # to check whether the entered seat is already booked

    if count > 0:
        for comp in bkseat:
            if comp == x:
                print("This seat is already booked", format(x))

                x = int(input("Enter other unoccupied seat number:\n"))

    # bkseat.append(x) links to the already created array

    bkseat.append(x)
    count = count + 1

    # to check which seats are booked.
    # s_amt is to count for Silver seats
    # g_amt is to count for Gold seats
    # p_amt is to count for Platinum seats

    if x > 0 and x <= 20:
        s_amt = s_amt + 1
    elif x >= 21 and x <= 40:
        g_amt = g_amt + 1
    elif x >= 41 and x <= 60:
        p_amt = p_amt + 1
    else:
        print("Is an invalid seat number..!!", format(x))

        x = int(input("Enter valid seat number:\n"))

        if count > 0:
            for comp in bkseat:
                if comp == x:
                    print("This seat is already booked", format(x))
                    x = int(input("Enter other unoccupied seat number:\n"))

        bkseat[i] = x
        if x > 0 and x <= 20:
            s_amt = s_amt + 1
        elif x >= 21 and x <= 40:
            g_amt = g_amt + 1
        elif x >= 41 and x <= 60:
            p_amt = p_amt + 1
        count = count + 1

print()

print("Seats booked:")
for s in bkseat:
    print(s, end="  ")

print()

print("\nSilver seats -", s_amt)
print("Gold seats -", g_amt)
print("Platinum seats -", p_amt)

print()

# to calculate the total amount

price = (s_amt * 130) + (g_amt * 150) + (p_amt * 175)
print("\nTotal amount to be paid : Rs.", price)


