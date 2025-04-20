# parse table for rpal grammar
# parse_table = {
#     'E': {
#           'let':['let D in E', 'let'],
#           'fn':['fn Vb+ in E', 'lambda'],
#           'not': ['Ew', ''],
#           '+': ['Ew', ''],
#           '-': ['Ew', ''],
#           '<IDENTIFIER>': ['Ew', ''],
#           '<INTEGER>': ['Ew', ''],
#           '<STRING>': ['Ew', ''],
#           'true': ['Ew', ''],
#           'false': ['Ew', ''],
#           'nil': ['Ew', ''],
#           '(': ['Ew', ''],
#           'dummy': ['Ew', '']
#         },
#     'Ew': {
#         'not': ['TX', ''],
#         '+': ['TX', ''],
#         '-': ['TX', ''],
#         '<IDENTIFIER>': ['TX', ''],
#         '<INTEGER>': ['TX', ''],
#         '<STRING>': ['TX', ''],
#         'true': ['TX', ''],
#         'false': ['TX', ''],
#         'nil': ['TX', ''],
#         '(': ['TX', ''],
#         'dummy': ['TX', '']
#     },
#     'X': {
#         'where': ['where Dr', 'where'],
#         ')': ['', '']
#     },
#     'T': {
#         'not': ['Ta Y', ''],
#         '+': ['Ta Y', ''],
#         '-': ['Ta Y', ''],
#         '<IDENTIFIER>': ['Ta Y', ''],
#         '<INTEGER>': ['Ta Y', ''],
#         '<STRING>': ['Ta Y', ''],
#         'true': ['Ta Y', ''],
#         'false': ['Ta Y', ''],
#         'nil': ['Ta Y', ''],
#         '(': ['Ta Y', ''],
#         'dummy': ['Ta Y', '']
#     },
#     'Y': {
#         ',': ['(, Ta)+', 'tau'],
#         'where': ['', '']
#     },
#     'Ta': {
#         'not': ['Tc Z', ''],
#         '+': ['Tc Z', ''],
#         '-': ['Tc Z', ''],
#         '<IDENTIFIER>': ['Tc Z', ''],
#         '<INTEGER>': ['Tc Z', ''],
#         '<STRING>': ['Tc Z', ''],
#         'true': ['Tc Z', ''],
#         'false': ['Tc Z', ''],
#         'nil': ['Tc Z', ''],
#         '(': ['Tc Z', ''],
#         'dummy': ['Tc Z', '']
#     },
#     'Z': {
#         'aug': ['aug Tc', 'aug'],
#         'where': ['', '']
#     },
#     'Tc': {
#         'not': ['B G', ''],
#         '+': ['B G', ''],
#         '-': ['B G', ''],
#         '<IDENTIFIER>': ['B G', ''],
#         '<INTEGER>': ['B G', ''],
#         '<STRING>': ['B G', ''],
#         'true': ['B G', ''],
#         'false': ['B G', ''],
#         'nil': ['B G', ''],
#         '(': ['B G', ''],
#         'dummy': ['B G', '']
#     },
#     'G': {
#         '->': ['-> Tc | Tc', '->'],
#         '(': ['', ''],
#         ',': ['', '']
#     },
#     'B': {
#         'not': ['Bt K', ''],
#         '+': ['Bt K', ''],
#         '-': ['Bt K', ''],
#         '<IDENTIFIER>': ['Bt K', ''],
#         '<INTEGER>': ['Bt K', ''],
#         '<STRING>': ['Bt K', ''],
#         'true': ['Bt K', ''],
#         'false': ['Bt K', ''],
#         'nil': ['Bt K', ''],
#         '(': ['Bt K', ''],
#         'dummy': ['Bt K', '']
#     },
#     'K': {
#         'or': ['or Bt', 'or'],
#         '->': ['', '']
#     },
#     'Bt': {
#         'not': ['Bs L', ''],
#         '+': ['Bs L', ''],
#         '-': ['Bs L', ''],
#         '<IDENTIFIER>': ['Bs L', ''],
#         '<INTEGER>': ['Bs L', ''],
#         '<STRING>': ['Bs L', ''],
#         'true': ['Bs L', ''],
#         'false': ['Bs L', ''],
#         'nil': ['Bs L', ''],
#         '(': ['Bs L', ''],
#         'dummy': ['Bs L', '']
#     },
#     'L': {
#         '&': ['& Bs', '&'],
#         'or': ['', '']
#     },
#     'Bs': {
#         'not': ['not Bp', 'not'],
#         '+': ['Bp', ''],
#         '-': ['Bp', ''],
#         '<IDENTIFIER>': ['Bp', ''],
#         '<INTEGER>': ['Bp', ''],
#         '<STRING>': ['Bp', ''],
#         'true': ['Bp', ''],
#         'false': ['Bp', ''],
#         'nil': ['Bp', ''],
#         '(': ['Bp', ''],
#         'dummy': ['Bp', '']
#     },
#     'Bp': {
#         '+': ['A M', ''],
#         '-': ['A M', ''],
#         '<IDENTIFIER>': ['A M', ''],
#         '<INTEGER>': ['A M', ''],
#         '<STRING>': ['A M', ''],
#         'true': ['A M', ''],
#         'false': ['A M', ''],
#         'nil': ['A M', ''],
#         '(': ['A M', ''],
#         'dummy': ['A M', '']
#     },
#     'M': {
#         'gr' : ['gr A', 'gr'],
#         '>': ['> A', 'gr'],
#         'ge': ['ge A', 'ge'],
#         '>=': ['>= A', 'ge'],
#         'ls': ['ls A', 'ls'],
#         '<': ['< A', 'ls'],
#         'le': ['le A', 'le'],
#         '<=': ['<= A', 'le'],
#         'eq': ['eq A', 'eq'],
#         'ne': ['ne A', 'ne'],
#         '+': ['', ''],
#         '-': ['', ''],
#         '<IDENTIFIER>': ['', ''],
#         '<INTEGER>': ['', ''],
#         '<STRING>': ['', ''],
#         'true': ['', ''],
#         'false': ['', ''],
#         'nil': ['', ''],
#         '(': ['', ''],
#         'dummy': ['', '']
#     },
#     'A': {
#         '+': ['+ A', ''],
#         '-': ['- A', 'neg'],
#         'gr': ['At J', ''],
#         '>': ['At J', ''],
#         'ge': ['At J', ''],
#         '>=': ['At J', ''],
#         'ls': ['At J', ''],
#         '<': ['At J', ''],
#         'le': ['At J', ''],
#         '<=': ['At J', ''],
#         'eq': ['At J', ''],
#         'ne': ['At J', '']
#     },
#     'At': {
#         'gr': ['Af N', ''],
#         '>': ['Af N', ''],
#         'ge': ['Af N', ''],
#         '>=': ['Af N', ''],
#         'ls': ['Af N', ''],
#         '<': ['Af N', ''],
#         'le': ['Af N', ''],
#         '<=': ['Af N', ''],
#         'eq': ['Af N', ''],
#         'ne': ['Af N', '']
#     },
#     'N': {
#         '*': ['* Af', '*'],
#         '/': ['/ Af', '/'],
#         '+': ['', ''],
#         '-': ['', '']
#     },
#     'J': {
#         '+': ['+ At', '+'],
#         '-': ['- At', '-'],
#         '&': ['', ''],
#         'or': ['', ''],
#     },
#     'Af': {
#         '<IDENTIFIER>': ['Ap O', ''],
#         '<INTEGER>': ['Ap O', ''],
#         '<STRING>': ['Ap O', ''],
#         'true': ['Ap O', ''],
#         'false': ['Ap O', ''],
#         'nil': ['Ap O', ''],
#         '(': ['Ap O', ''],
#         'dummy': ['Ap O', '']
#     },
#     'O': {
#         '**': ['** Af', '**'],
#         '+': ['', ''],
#         '-': ['', '']
#     },
#     'Ap': {
#         '<IDENTIFIER>': ['R Q', ''],
#         '<INTEGER>': ['R Q', ''],
#         '<STRING>': ['R Q', ''],
#         'true': ['R Q', ''],
#         'false': ['R Q', ''],
#         'nil': ['R Q', ''],
#         '(': ['R Q', ''],
#         'dummy': ['R Q', '']
#     },
#     'Q': {
#         '@<IDENTIFIER>': ['@<IDENTIFIER> R', '@'],
#         '**': ['', '']
#     },
#     'D': {
#         'rec': ['Da G', 'rec'],
#         '<IDENTIFIER>': ['Da G', ''],
#         'let': ['Da G', '']
#     },
#     'G': {
#         'within': ['within D', 'within'],
#         'in': ['', '']
#     },
#     'Da': {
#         'rec': ['Dr H', ''],
#         '<IDENTIFIER>': ['Dr H', ''],
#         '(': ['Dr H', ''],
#         'list': ['Dr H', '']
#     },
#     'H': {
#         'and': ['(and Dr)+', 'and'],
#         'within': ['', ''],
#     },
#     'Dr': {
#         'rec': ['rec Db', 'rec'],
#         '<IDENTIFIER>list': ['Db', ''],
#         '(': ['Db', '']
#     },
#     'Db': {
#         '<IDENTIFIER>list': ['Vl = E', '='],
#         '(': ['Vl = E', '='],
#         '<IDENTIFIER>': ['<IDENTIFIER> Vb+ = E', 'func_form'],
#         '(': ['( D )', '']
#     },
#     'R': {
#         '<IDENTIFIER>': ['Rn S', ''],
#         '<INTEGER>': ['Rn S', ''],
#         '<STRING>': ['Rn S', ''],
#         'true': ['Rn S', ''],
#         'false': ['Rn S', ''],
#         'nil': ['Rn S', ''],
#         '(': ['Rn S', ''],
#         'dummy': ['Rn S', '']
#     },
#     'S': {
#         '<IDENTIFIER>': ['R Rn', 'gamma'],
#         '<INTEGER>': ['R Rn', 'gamma'],
#         '<STRING>': ['R Rn', 'gamma'],
#         'true': ['R Rn', 'gamma'],
#         'false': ['R Rn', 'gamma'],
#         'nil': ['R Rn', 'gamma'],
#         '(': ['R Rn', 'gamma'],
#         'dummy': ['R Rn', 'gamma']
#     },
#     'Rn': {
#         '<IDENTIFIER>': ['<IDENTIFIER>', ''],
#         '<INTEGER>': ['<INTEGER>', ''],
#         '<STRING>': ['<STRING>', ''],
#         'true': ['true', 'true'],
#         'false': ['false', 'false'],
#         'nil': ['nil', 'nil'],
#         '(': ['( E )', ''],
#         'dummy': ['dummy', 'dummy']
#     },
#     'Vb': {
#         '<IDENTIFIER>': [ '<IDENTIFIER>', ''],
#         '(': ['( I ', '']
#     },
#     'I': {
#         '<IDENTIFIER>': ['Vl )', ''],
#         '(': [')', '()']
#     },
#     'Vl': {
#         '<IDENTIFIER>': ['<IDENTIFIER> list ,', ',?']
#     }
# }

tokens = []
ast_nodes = []

'''
# Expressions ############################################
E -> 'let' D 'in' E => 'let'
-> 'fn' Vb+ '.' E => 'lambda'
-> Ew;
Ew -> T 'where' Dr => 'where'
-> T;
'''

def E():
    print(tokens[0])
    if tokens[0] == 'let':
        tokens.pop(0)
        D()
        if tokens[0] == 'in':
            tokens.pop(0)
            E()
            ast_nodes.append('let')
        
        else:
            print("Error: Expected 'in' after 'let'")
            return
        
    elif tokens[0] == 'fn':
        tokens.pop(0)
        Vb()
        while tokens[0] != '.':
            Vb()
        if tokens[0] == '.':
            tokens.pop(0)
            E()
            ast_nodes.append('lambda')
    else:
        Ew()


'''Ew	->T 'where' Dr			=> 'where'
			->T;
'''

def Ew():
    print(tokens[0])
    T()
    if tokens[0] == 'where':
        tokens.pop(0)
        Dr()
        ast_nodes.append('where')


'''T 	-> Ta ( ',' Ta )+ => 'tau'
			-> Ta ;
'''
def T():
    print(tokens[0])
    Ta()
    while tokens[0] == ',':
        tokens.pop(0)
        Ta()
        if tokens[0] != ',':
            ast_nodes.append('tau')


'''Ta 	-> Ta 'aug' Tc => 'aug'
				-> Tc ;
'''
def Ta():
    print(tokens[0])
    Tc()
    while tokens[0] == 'aug':
        tokens.pop(0)
        Tc()
        if tokens[0] != 'aug':
            ast_nodes.append('aug')


'''Tc 	-> B '->' Tc '|' Tc => '->'
			-> B ;
'''
def Tc():
    print(tokens[0])
    B()
    if tokens[0] == '->':
        tokens.pop(0)
        Tc()
        if tokens[0] == '|':
            tokens.pop(0)
            Tc()
            ast_nodes.append('->')
        else:
            print("Error: Expected '|'")
            return


'''B 	-> B 'or' Bt 	=> 'or'
			-> Bt ;
'''
def B():
    print(tokens[0])
    Bt()
    while tokens[0] == 'or':
        tokens.pop(0)
        Bt()
        if tokens[0] != 'or':
            ast_nodes.append('or')


'''Bt	-> Bt '&' Bs => '&'
			-> Bs ;
'''
def Bt():
    print(tokens[0])
    Bs()
    while tokens[0] == '&':
        tokens.pop(0)
        Bs()
        if tokens[0] != '&':
            ast_nodes.append('&')


'''Bs	-> 'not' Bp => 'not'
			-> Bp ;
'''
def Bs():
    print(tokens[0])
    if tokens[0] == 'not':
        tokens.pop(0)
        Bp()
        ast_nodes.append('not')
    else:
        Bp()


'''Bp 	-> A ('gr' | '>' ) A => 'gr'
			-> A ('ge' | '>=') A => 'ge'
			-> A ('ls' | '<' ) A => 'ls'
			-> A ('le' | '<=') A => 'le'
			-> A 'eq' A => 'eq'
			-> A 'ne' A => 'ne'
			-> A ;
'''
def Bp():
    print(tokens[0])
    A()
    if tokens[0] == 'gr' or tokens[0] == '>':
        tokens.pop(0)
        A()
        ast_nodes.append('gr')
    elif tokens[0] == 'ge' or tokens[0] == '>=':
        tokens.pop(0)
        A()
        ast_nodes.append('ge')
    elif tokens[0] == 'ls' or tokens[0] == '<':
        tokens.pop(0)
        A()
        ast_nodes.append('ls')
    elif tokens[0] == 'le' or tokens[0] == '<=':
        tokens.pop(0)
        A()
        ast_nodes.append('le')
    elif tokens[0] == 'eq':
        tokens.pop(0)
        A()
        ast_nodes.append('eq')
    elif tokens[0] == 'ne':
        tokens.pop(0)
        A()
        ast_nodes.append('ne')


'''A 	-> A '+' At => '+'
			-> A '-' At => '-'
			->	 '+' At
			->	 '-'At =>'neg'
			-> At ;
'''
def A():
    print(tokens[0])
    if tokens[0] == '+':
        tokens.pop(0)
        At()
    elif tokens[0] == '-':
        tokens.pop(0)
        At()
        ast_nodes.append('neg')
    else:
        At()
        while tokens[0] == '+' or tokens[0] == '-':
            if tokens[0] == '+':
                tokens.pop(0)
                At()
                if tokens[0] != '+' or tokens[0] != '-':
                    ast_nodes.append('+')
            elif tokens[0] == '-':
                tokens.pop(0)
                At()
                if tokens[0] != '+' or tokens[0] != '-':
                    ast_nodes.append('-')

'''At 	-> At '*' Af => '*'
				-> At '/' Af => '/'
				-> Af ;
'''
def At():
    print(tokens[0])
    Af()
    while tokens[0] == '*' or tokens[0] == '/':
        if tokens[0] == '*':
            tokens.pop(0)
            Af()
            if tokens[0] != '*' or tokens[0] != '/':
                ast_nodes.append('*')
        elif tokens[0] == '/':
            tokens.pop(0)
            Af()
            if tokens[0] != '*' or tokens[0] != '/':
                ast_nodes.append('/')


'''Af 	-> Ap '**' Af => '**'
				-> Ap ;
'''
def Af():
    print(tokens[0])
    Ap()
    while tokens[0] == '**':
        tokens.pop(0)
        Af()
        if tokens[0] != '**':
            ast_nodes.append('**')


'''Ap 	-> Ap '@' '<IDENTIFIER>' R => '@'
				-> R ;
'''
def Ap():
    print(tokens[0])
    R()
    while tokens[0] == '@':
        tokens.pop(0)
        if tokens[0] == '<IDENTIFIER>':
            tokens.pop(0)
            R()
            ast_nodes.append('@')
        else:
            print("Error: Expected '<IDENTIFIER>' after '@'")
            return
    else:
        R()


'''R 	-> R Rn => 'gamma'
				-> Rn ;
'''
def R():
    print(tokens[0])
    if tokens[0] == '<IDENTIFIER>' or tokens[0] == '<INTEGER>' or tokens[0] == '<STRING>' or tokens[0] == 'true' or tokens[0] == 'false' or tokens[0] == 'nil' or tokens[0] == 'dummy' or tokens[0] == ')' or tokens[0] == '(':
        Rn()
        while tokens[0] == '<IDENTIFIER>' or tokens[0] == '<INTEGER>' or tokens[0] == '<STRING>' or tokens[0] == 'true' or tokens[0] == 'false' or tokens[0] == 'nil' or tokens[0] == 'dummy' or tokens[0] == ')' or tokens[0] == '(':
            Rn()
            ast_nodes.append('gamma')
    else:
        print("Error: Expected a valid token")
        return


'''Rn 	-> '<IDENTIFIER>'
				-> '<INTEGER>'
				-> '<STRING>'
				-> 'true' => 'true'
				-> 'false' => 'false'
				-> 'nil' => 'nil'
				-> '(' E ')'
				-> 'dummy' => 'dummy' ;
'''
def Rn():
    print(tokens[0])
    if tokens[0] == '<IDENTIFIER>':
        tokens.pop(0)
    elif tokens[0] == '<INTEGER>':
        tokens.pop(0)
    elif tokens[0] == '<STRING>':
        tokens.pop(0)
    elif tokens[0] == 'true':
        tokens.pop(0)
        ast_nodes.append('true')
    elif tokens[0] == 'false':
        tokens.pop(0)
        ast_nodes.append('false')
    elif tokens[0] == 'nil':
        tokens.pop(0)
        ast_nodes.append('nil')
    elif tokens[0] == '(':
        tokens.pop(0)
        E()
        if tokens[0] == ')':
            tokens.pop(0)
        else:
            print("Error: Expected ')'")
            return
    elif tokens[0] == 'dummy':
        tokens.pop(0)
        ast_nodes.append('dummy')
    else:
        print("Error: Expected a valid token")
        return


'''D 	-> Da 'within' D => 'within'
				-> Da ;
'''
def D():
    print(tokens[0])
    Da()
    if tokens[0] == 'within':
        tokens.pop(0)
        D()
        ast_nodes.append('within')


'''Da  -> Dr ( 'and' Dr )+ => 'and'
					-> Dr ;
'''
def Da():
    print(tokens[0])
    Dr()
    while tokens[0] == 'and':
        tokens.pop(0)
        Dr()
        ast_nodes.append('and')


'''Dr  -> 'rec' Db => 'rec'
					-> Db ;
'''
def Dr():
    print(tokens[0])
    if tokens[0] == 'rec':
        tokens.pop(0)
        Db()
        ast_nodes.append('rec')
    else:
        Db()


'''Db  -> Vl '=' E => '='
				-> '<IDENTIFIER>' Vb+ '=' E => 'fcn_form'
				-> '(' D ')' ; 
'''
def Db():
    print(tokens[0])
    if tokens[0] == '<IDENTIFIER>':
        tokens.pop(0)
        Vb()
        while tokens[0] != '=':
            Vb()
        tokens.pop(0)
        E()
        ast_nodes.append('fcn_form')
        
    elif tokens[0] == '(':
        tokens.pop(0)
        D()
        if tokens[0] == ')':
            tokens.pop(0)
        else:
            print("Error: Expected ')'")
            return
    else:
        Vl()
        if tokens[0] == '=':
            tokens.pop(0)
            E()
            ast_nodes.append('=')
        else:
            print("Error: Expected '='")
            return
        

'''Vb  -> '<IDENTIFIER>'
			-> '(' Vl ')'
			-> '(' ')' => '()';
'''
def Vb():
    print(tokens[0])
    if tokens[0] == '<IDENTIFIER>':
        tokens.pop(0)
    elif tokens[0] == '(':
        tokens.pop(0)
        if tokens[0] == ')':
            tokens.pop(0)
            ast_nodes.append('()')
            return
        Vl()
        if tokens[0] == ')':
            tokens.pop(0)
            ast_nodes.append('()')
            return
        else:
            print("Error: Expected a valid token")
            return
        
    else:
        print("Error: Expected a valid token")
        return
    

'''Vl -> '<IDENTIFIER>' list ',' => ','?
'''
def Vl():
    print(tokens[0])
    if tokens[0] == '<IDENTIFIER>':
        tokens.pop(0)
        while tokens[0] == ',':
            tokens.pop(0)
            if tokens[0] == '<IDENTIFIER>':
                tokens.pop(0)
            elif tokens[0] != ',':
                ast_nodes.append("','?")
            else:
                print("Error: Expected '<IDENTIFIER>' after ','")
                return
    else:
        print("Error: Expected '<IDENTIFIER>'")
        return

def parser():
    E()
    return


def build_ast(reduced_grammar):
    ast = []
    # to be implemented
    return ast


input_str = "let <IDENTIFIER> = <INTEGER> in <INTEGER> + <INTEGER> - <STRING> where <IDENTIFIER> = <INTEGER>"
tokens = input_str.split(" ")
parser()