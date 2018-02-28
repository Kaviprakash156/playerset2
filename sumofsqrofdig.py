def sum_of_squares_of_digits(value):
    return sum(int(c) ** 2 for c in str(value))
print (sum_of_squares_of_digits(12))
