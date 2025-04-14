# parse table for rpal grammar
parse_table = {
    'E': {
          'let':['let D in E', 'let'],
          'fn':['fn Vb+ in E', 'lambda'],
          'not': ['Ew', ''],
          '+': ['Ew', ''],
          '-': ['Ew', ''],
          '<IDENTIFIER>': ['Ew', ''],
          '<INTEGER>': ['Ew', ''],
          '<STRING>': ['Ew', ''],
          'true': ['Ew', ''],
          'false': ['Ew', ''],
          'nil': ['Ew', ''],
          '(': ['Ew', ''],
          'dummy': ['Ew', '']
        },
    'Ew': {
        'not': ['TX', ''],
        '+': ['TX', ''],
        '-': ['TX', ''],
        '<IDENTIFIER>': ['TX', ''],
        '<INTEGER>': ['TX', ''],
        '<STRING>': ['TX', ''],
        'true': ['TX', ''],
        'false': ['TX', ''],
        'nil': ['TX', ''],
        '(': ['TX', ''],
        'dummy': ['TX', '']
    },
    'X': {
        'where': ['where Dr', 'where'],
        ')': ['', '']
    },
    'T': {
        'not': ['Ta Y', ''],
        '+': ['Ta Y', ''],
        '-': ['Ta Y', ''],
        '<IDENTIFIER>': ['Ta Y', ''],
        '<INTEGER>': ['Ta Y', ''],
        '<STRING>': ['Ta Y', ''],
        'true': ['Ta Y', ''],
        'false': ['Ta Y', ''],
        'nil': ['Ta Y', ''],
        '(': ['Ta Y', ''],
        'dummy': ['Ta Y', '']
    },
    'Y': {
        ',': ['(, Ta)+', 'tau'],
        'where': ['', '']
    },
    'Ta': {
        'not': ['Tc Z', ''],
        '+': ['Tc Z', ''],
        '-': ['Tc Z', ''],
        '<IDENTIFIER>': ['Tc Z', ''],
        '<INTEGER>': ['Tc Z', ''],
        '<STRING>': ['Tc Z', ''],
        'true': ['Tc Z', ''],
        'false': ['Tc Z', ''],
        'nil': ['Tc Z', ''],
        '(': ['Tc Z', ''],
        'dummy': ['Tc Z', '']
    },
    'Z': {
        'aug': ['aug Tc', 'aug'],
        'where': ['', '']
    },
    'Tc': {
        'not': ['B G', ''],
        '+': ['B G', ''],
        '-': ['B G', ''],
        '<IDENTIFIER>': ['B G', ''],
        '<INTEGER>': ['B G', ''],
        '<STRING>': ['B G', ''],
        'true': ['B G', ''],
        'false': ['B G', ''],
        'nil': ['B G', ''],
        '(': ['B G', ''],
        'dummy': ['B G', '']
    },
    'G': {
        '->': ['-> Tc | Tc', '->'],
        '(': ['', ''],
        ',': ['', '']
    },
    'B': {
        'not': ['Bt K', ''],
        '+': ['Bt K', ''],
        '-': ['Bt K', ''],
        '<IDENTIFIER>': ['Bt K', ''],
        '<INTEGER>': ['Bt K', ''],
        '<STRING>': ['Bt K', ''],
        'true': ['Bt K', ''],
        'false': ['Bt K', ''],
        'nil': ['Bt K', ''],
        '(': ['Bt K', ''],
        'dummy': ['Bt K', '']
    },
    'K': {
        'or': ['or Bt', 'or'],
        '->': ['', '']
    },
    'Bt': {
        'not': ['Bs L', ''],
        '+': ['Bs L', ''],
        '-': ['Bs L', ''],
        '<IDENTIFIER>': ['Bs L', ''],
        '<INTEGER>': ['Bs L', ''],
        '<STRING>': ['Bs L', ''],
        'true': ['Bs L', ''],
        'false': ['Bs L', ''],
        'nil': ['Bs L', ''],
        '(': ['Bs L', ''],
        'dummy': ['Bs L', '']
    },
    'L': {
        '&': ['& Bs', '&'],
        'or': ['', '']
    },
    'Bs': {
        'not': ['not Bp', 'not'],
        '+': ['Bp', ''],
        '-': ['Bp', ''],
        '<IDENTIFIER>': ['Bp', ''],
        '<INTEGER>': ['Bp', ''],
        '<STRING>': ['Bp', ''],
        'true': ['Bp', ''],
        'false': ['Bp', ''],
        'nil': ['Bp', ''],
        '(': ['Bp', ''],
        'dummy': ['Bp', '']
    },
    'Bp': {
        '+': ['A M', ''],
        '-': ['A M', ''],
        '<IDENTIFIER>': ['A M', ''],
        '<INTEGER>': ['A M', ''],
        '<STRING>': ['A M', ''],
        'true': ['A M', ''],
        'false': ['A M', ''],
        'nil': ['A M', ''],
        '(': ['A M', ''],
        'dummy': ['A M', '']
    },
    'M': {
        'gr' : ['gr A', 'gr'],
        '>': ['> A', 'gr'],
        'ge': ['ge A', 'ge'],
        '>=': ['>= A', 'ge'],
        'ls': ['ls A', 'ls'],
        '<': ['< A', 'ls'],
        'le': ['le A', 'le'],
        '<=': ['<= A', 'le'],
        'eq': ['eq A', 'eq'],
        'ne': ['ne A', 'ne'],
        '+': ['', ''],
        '-': ['', ''],
        '<IDENTIFIER>': ['', ''],
        '<INTEGER>': ['', ''],
        '<STRING>': ['', ''],
        'true': ['', ''],
        'false': ['', ''],
        'nil': ['', ''],
        '(': ['', ''],
        'dummy': ['', '']
    },
    'A': {
        '+': ['+ A', ''],
        '-': ['- A', 'neg'],
        'gr': ['At J', ''],
        '>': ['At J', ''],
        'ge': ['At J', ''],
        '>=': ['At J', ''],
        'ls': ['At J', ''],
        '<': ['At J', ''],
        'le': ['At J', ''],
        '<=': ['At J', ''],
        'eq': ['At J', ''],
        'ne': ['At J', '']
    },
    'At': {
        'gr': ['Af N', ''],
        '>': ['Af N', ''],
        'ge': ['Af N', ''],
        '>=': ['Af N', ''],
        'ls': ['Af N', ''],
        '<': ['Af N', ''],
        'le': ['Af N', ''],
        '<=': ['Af N', ''],
        'eq': ['Af N', ''],
        'ne': ['Af N', '']
    },
    'N': {
        '*': ['* Af', '*'],
        '/': ['/ Af', '/'],
        '+': ['', ''],
        '-': ['', '']
    },
    'J': {
        '+': ['+ At', '+'],
        '-': ['- At', '-'],
        '&': ['', ''],
        'or': ['', ''],
    },
    'Af': {
        '<IDENTIFIER>': ['Ap O', ''],
        '<INTEGER>': ['Ap O', ''],
        '<STRING>': ['Ap O', ''],
        'true': ['Ap O', ''],
        'false': ['Ap O', ''],
        'nil': ['Ap O', ''],
        '(': ['Ap O', ''],
        'dummy': ['Ap O', '']
    },
    'O': {
        '**': ['** Af', '**'],
        '+': ['', ''],
        '-': ['', '']
    },
    'Ap': {
        '<IDENTIFIER>': ['R Q', ''],
        '<INTEGER>': ['R Q', ''],
        '<STRING>': ['R Q', ''],
        'true': ['R Q', ''],
        'false': ['R Q', ''],
        'nil': ['R Q', ''],
        '(': ['R Q', ''],
        'dummy': ['R Q', '']
    },
    'Q': {
        '@<IDENTIFIER>': ['@<IDENTIFIER> R', '@'],
        '**': ['', '']
    },
    'D': {
        'rec': ['Da G', 'rec'],
        '<IDENTIFIER>': ['Da G', ''],
        'let': ['Da G', '']
    },
    'G': {
        'within': ['within D', 'within'],
        'in': ['', '']
    },
    'Da': {
        'rec': ['Dr H', ''],
        '<IDENTIFIER>': ['Dr H', ''],
        '(': ['Dr H', ''],
        'list': ['Dr H', '']
    },
    'H': {
        'and': ['(and Dr)+', 'and'],
        'within': ['', ''],
    },
    'Dr': {
        'rec': ['rec Db', 'rec'],
        '<IDENTIFIER>list': ['Db', ''],
        '(': ['Db', '']
    },
    'Db': {
        '<IDENTIFIER>list': ['Vl = E', '='],
        '(': ['Vl = E', '='],
        '<IDENTIFIER>': ['<IDENTIFIER> Vb+ = E', 'func_form'],
        '(': ['( D )', '']
    },
    'R': {
        '<IDENTIFIER>': ['Rn S', ''],
        '<INTEGER>': ['Rn S', ''],
        '<STRING>': ['Rn S', ''],
        'true': ['Rn S', ''],
        'false': ['Rn S', ''],
        'nil': ['Rn S', ''],
        '(': ['Rn S', ''],
        'dummy': ['Rn S', '']
    },
    'S': {
        '<IDENTIFIER>': ['R Rn', 'gamma'],
        '<INTEGER>': ['R Rn', 'gamma'],
        '<STRING>': ['R Rn', 'gamma'],
        'true': ['R Rn', 'gamma'],
        'false': ['R Rn', 'gamma'],
        'nil': ['R Rn', 'gamma'],
        '(': ['R Rn', 'gamma'],
        'dummy': ['R Rn', 'gamma']
    },
    'Rn': {
        '<IDENTIFIER>': ['<IDENTIFIER>', ''],
        '<INTEGER>': ['<INTEGER>', ''],
        '<STRING>': ['<STRING>', ''],
        'true': ['true', 'true'],
        'false': ['false', 'false'],
        'nil': ['nil', 'nil'],
        '(': ['( E )', ''],
        'dummy': ['dummy', 'dummy']
    },
    'Vb': {
        '<IDENTIFIER>': [ '<IDENTIFIER>', ''],
        '(': ['( I ', '']
    },
    'I': {
        '<IDENTIFIER>': ['Vl )', ''],
        '(': [')', '()']
    },
    'Vl': {
        '<IDENTIFIER>': ['<IDENTIFIER> list ,', ',?']
    }
}

def parser(input_str):
    stack = ['E']
    reduced_grammar = []
    tokens = input_str.split()
    start_symbol = 'E'

    for i in range(len(tokens)):
        token = tokens[i]
        print('Stack:', stack, '/nToken:', token, 'Start Symbol:', start_symbol)
        if not parse_table[start_symbol][token]:
            print("Error the token cannot be parsed")
            return
        rule = parse_table[start_symbol][token]
        stack.remove(start_symbol)
        stack = list(rule[0].split()) + stack
        
        if token == stack[0]:
            stack.remove(token)
            start_symbol = stack[0]
            continue
        reduced_grammar.append(rule[1])
        start_symbol = stack[0]
        print('Start Symbol:', start_symbol)

    if (len(stack) > 0 and len(tokens) == 0) or (len(stack) == 0 and len(tokens) > 0):
        print('Error, the input string is not valid')
        return
    
    print('The input string is valid. Parsing Successful!')
    print('Reduced grammar:', reduced_grammar)


def build_ast(reduced_grammar):
    ast = []
    # to be implemented
    return ast


input_str = "let <IDENTIFIER>"
parser(input_str)