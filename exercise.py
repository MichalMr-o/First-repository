def flex_fizz_buzz(num1: int = 3, num2: int = 5, range_from: int = 1, range_to: int = 101):
    for i in range(range_from, range_to):
        fizz = 'Fizz' if i % num1 == 0 else ''
        buzz = 'Buzz' if i % num2 == 0 else ''
        print(f'{fizz}{buzz}' or i)


if __name__ == '__main__':
    flex_fizz_buzz(5, 7, 101, 201)
