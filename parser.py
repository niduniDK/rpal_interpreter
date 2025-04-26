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
        if len(tokens) > 0 and tokens[0] == 'in':
            tokens.pop(0)
            E()
            ast_nodes.append('let')
        
        else:
            raise SyntaxError("Error: Expected 'in' after 'let'")
            return
        
    elif tokens[0] == 'fn':
        tokens.pop(0)
        Vb()
        while tokens[0] != '.':
            Vb()
        if len(tokens) > 0 and tokens[0] == '.':
            tokens.pop(0)
            E()
            ast_nodes.append('lambda')
        else:
            raise SyntaxError("Error: Expected '.' after 'fn'")
            return
    else:
        Ew()


'''Ew	->T 'where' Dr			=> 'where'
			->T;
'''

def Ew():
    print(tokens[0])
    T()
    if len(tokens) > 0 and tokens[0] == 'where':
        tokens.pop(0)
        Dr()
        ast_nodes.append('where')


'''T 	-> Ta ( ',' Ta )+ => 'tau'
			-> Ta ;
'''
def T():
    print(tokens[0])
    Ta()
    while len(tokens) > 0 and tokens[0] == ',':
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
    while len(tokens) > 0 and tokens[0] == 'aug':
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
    if len(tokens) > 0 and tokens[0] == '->':
        tokens.pop(0)
        Tc()
        if tokens[0] == '|':
            tokens.pop(0)
            Tc()
            ast_nodes.append('->')
        else:
            raise SyntaxError("Error: Expected '|'")
            return


'''B 	-> B 'or' Bt 	=> 'or'
			-> Bt ;
'''
def B():
    print(tokens[0])
    Bt()
    while len(tokens) > 0 and tokens[0] == 'or':
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
    while len(tokens) > 0 and tokens[0] == '&':
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
    if len(tokens) > 0:
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
        while len(tokens) > 0 and (tokens[0] == '+' or tokens[0] == '-'):
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
    while len(tokens) > 0 and (tokens[0] == '*' or tokens[0] == '/'):
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
    while len(tokens) > 0 and tokens[0] == '**':
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
    while len(tokens) > 0 and tokens[0] == '@':
        tokens.pop(0)
        if tokens[0] == '<IDENTIFIER>':
            tokens.pop(0)
            R()
            ast_nodes.append('@')
            return
        else:
            raise SyntaxError("Error: Expected '<IDENTIFIER>' after '@'")
            return
    


'''R 	-> R Rn => 'gamma'
				-> Rn ;
'''
def R():
    print(tokens[0])
    if tokens[0] == '<IDENTIFIER>' or tokens[0] == '<INTEGER>' or tokens[0] == '<STRING>' or tokens[0] == 'true' or tokens[0] == 'false' or tokens[0] == 'nil' or tokens[0] == 'dummy' or tokens[0] == '(':
        Rn()
        while len(tokens) > 0 and (tokens[0] == '<IDENTIFIER>' or tokens[0] == '<INTEGER>' or tokens[0] == '<STRING>' or tokens[0] == 'true' or tokens[0] == 'false' or tokens[0] == 'nil' or tokens[0] == 'dummy' or tokens[0] == '('):
            Rn()
            ast_nodes.append('gamma')
    else:
        raise SyntaxError("Error: Expected a valid token")
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
            raise SyntaxError("Error: Expected ')'")
            return
    elif tokens[0] == 'dummy':
        tokens.pop(0)
        ast_nodes.append('dummy')
    else:
        raise SyntaxError("Error: Expected a valid token")
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
        if tokens[0] == '=':
            tokens.pop(0)
            E()
            ast_nodes.append('fcn_form')
        else:
            raise SyntaxError("Error: Expected '='")
            return
        
    elif tokens[0] == '(':
        tokens.pop(0)
        D()
        if tokens[0] == ')':
            tokens.pop(0)
        else:
            raise SyntaxError("Error: Expected ')'")
            return
    else:
        Vl()
        if tokens[0] == '=':
            tokens.pop(0)
            E()
            ast_nodes.append('=')
        else:
            raise SyntaxError("Error: Expected '='")
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
            raise SyntaxError("Error: Expected a valid token")
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
                raise SyntaxError("Error: Expected '<IDENTIFIER>' after ','")
                return
    else:
        raise SyntaxError("Expected '<IDENTIFIER>'")
        return

def parser():
    E()
    return ast_nodes


def build_ast(reduced_grammar):
    ast = []
    # to be implemented
    return ast

# <IDENTIFIER:let>
# <IDENTIFIER:x>
# <OPERATOR:=>
# <INTEGER:53>
# <OPERATOR:+>
# <INTEGER:39>
# <IDENTIFIER:in>
# <IDENTIFIER:Print>
# (
# <STRING:Hello World>
# )


input_str = "let <IDENTIFIER> = <INTEGER> + <INTEGER> in <IDENTIFIER> ( <STRING> )"
tokens = input_str.split(" ")
print(parser())