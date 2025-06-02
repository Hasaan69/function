def square_list(start, end):
    squares = list(i * i for i in range(start, end + 1))
    even_squares = list(x for x in squares if x % 2 == 0)
    odd_squares = list(x for x in squares if x % 2 != 0)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)
square_list(1, 10)