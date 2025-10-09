def fizzbuzz_val(n, x, y):
    return "Fizz" * (str(n)[0] == str(x)) + "Buzz" * (n % 10 == y) or n
print(fizzbuzz_val(123456, 3, 5))
print(fizzbuzz_val(345, 3, 5))
print(fizzbuzz_val(12345, 3, 5))
print(fizzbuzz_val(3456, 3, 5))