def square(num: int) -> int:
    return num**2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        inputNumber = int(input('Enter a number\n> '))
    except ValueError:
        print('Not a number!')
