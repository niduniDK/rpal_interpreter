import sys
import AST.parser as parser
import Standardizer.standardizer as standardizer
import CSE.CSE as CSE

def main():
    args = sys.argv
    print_ast = False
    print_st = False

    if len(args) == 3:
        if args[1] == "-ast":
            print_ast = True
            filename = args[2]
        elif args[1] == "-st":
            print_st = True
            filename = args[2]
        else:
            print(f"Unknown option: {args[1]}")
            sys.exit(1)
    elif len(args) == 2:
        filename = args[1]
    else:
        print("Usage: python myrpal.py [-ast] filename")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Parse content
            if print_ast:
                parser.print_ast(content)
            elif print_st:
                standardizer.print_st(content)
            CSE.evaluate(content)
    except FileNotFoundError:
        print(f"Cannot open file: {filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()
