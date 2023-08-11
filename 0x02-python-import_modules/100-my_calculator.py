#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    result = 0
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        match op:
            case "+":
                result = add(a, b)
                print("{} + {} = {}".format(a, b, result))
            case "-":
                result = sub(a, b)
                print("{} - {} = {}".format(a, b, result))
            case "*":
                result = mul(a, b)
                print("{} * {} = {}".format(a, b, result))
            case "/":
                result = div(a, b)
                print("{} / {} = {}".format(a, b, result))
            case default:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)


