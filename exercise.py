def divide_fizzbuzz(7, 19):
    three = "Fizz"
    five = "Buzz"
    for num in range(1, 101):
        string_x = ""
        if num % 3 == 0:
            string_x += three
            print(string_x)
        if num % 5 == 0:
            string_x += five
            print(string_x)
        if string_x == "":
            print(num)

if __name__ == '__main__':
    # divide_fizzbuzz()

    for i in range(1, 101):
        fizz = 'Fizz' if i % 3 == 0 else ''
        buzz = 'Buzz' if i % 5 == 0 else ''
        print(f'{fizz}{buzz}' or i)
