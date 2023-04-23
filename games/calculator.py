from art import calculator


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Invalid input"


calculations = {"+": add, "-": sub, "*": mul, "/": div}


def print_logo():
    print(calculator)


def get_first_no():
    return float(input("Enter the first number: "))


def get_operator():
    return input("Enter any operator from the following: \n'+'\n'-'\n'*'\n'\\'\n")


def get_second_no():
    return float(input("Enter the second number: "))


def calculate(n1, op, n2):
    answer = calculations[op](n1, n2)
    print(f"The answer is {answer}.")
    return answer


def start_calculator():
    print_logo()
    continue_from_last = True
    answer = calculate(get_first_no(), get_operator(), get_second_no())
    while continue_from_last:
        user_choice = input("Type 'c' to continue from here, 's' to start fresh and any other key to end: ").lower()
        if user_choice == 'c':
            calculate(answer, get_operator(), get_second_no())
        elif user_choice == 's':
            start_calculator()
        else:
            continue_from_last = False


if __name__ == '__main__':
    start_calculator()
