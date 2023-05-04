def get_input():
    number_a = input("Enter number: ")
    equation = input("Enter equation: ")
    number_b = input("Enter number: ")
    # numbers = []
    # numbers.insert(0, number_a)
    # numbers.insert(1, equation)
    # numbers.insert(2, number_b)
    numbers = number_a + ' ' + equation + ' ' + number_b
    return numbers

def send_info(a):
    print(f'Your result: {a}')

