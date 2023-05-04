import functions

def check(data):
    # if data[1] == '+':
    #     return functions.sum(data[0], data[2])
    # elif data[1] == '-':
    #     return functions.minus(data[0], data[2])
    # elif data[1] == '*':
    #     return functions.mult(data[0], data[2])
    # elif data[1] == '/':
    #     return functions.dev(data[0], data[2])
    # else:
    #     print("wrong equetion sing!")
    match data[1]:
        case '+':
            return functions.sum(data[0], data[2])
        case '-':
            return functions.minus(data[0], data[2])
        case '*':
            return functions.mult(data[0], data[2])
        case '/':
            return functions.dev(data[0], data[2])
        case _:
            print("wrong equetion sing!")

        