def fizz_buzz_logic(number):
    """
    Returns:
    - "FizzBuzz" if number divisible by 3 and 5
    - "Fizz" if divisible by 3
    - "Buzz" if divisible by 5
    - number itself otherwise
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def run_fizz_buzz():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        result = fizz_buzz_logic(i)
        print(result)

        if result == "FizzBuzz":
            fizzbuzz_count += 1
        elif result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1

    print("\nCounts:")
    print("Fizz count:", fizz_count)
    print("Buzz count:", buzz_count)
    print("FizzBuzz count:", fizzbuzz_count)


# Run the program
run_fizz_buzz()
