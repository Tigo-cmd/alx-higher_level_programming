#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    result = 0
    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        match op:
            case "+":
                result = add(a, b)
                print("{} + {} = {}".format(a, b, result))
                exit(0)
            case "-":
                result = sub(a, b)
                print("{} - {} = {}".format(a, b, result))
                exit(0)
            case "*":
                result = mul(a, b)
                print("{} * {} = {}".format(a, b, result))
                exit(0)
            case "/":
                result = div(a, b)
                print("{} / {} = {}".format(a, b, result))
                exit(0)
            case default:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
