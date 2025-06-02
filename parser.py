from AST import AST, Node
from lexical_analyzer import Lexer
from lexical_analyzer import TokenType

tokens = []
ast_nodes = []
keywords = ['let', 'in', 'fn', 'aug', 'where', 'rec', 'within', 'and', 'or', 'not', 'gr', 'ge', 'ls', 'le', 'eq', 'ne', 'dummy']
operators_in_text = ['and', 'or', 'not', 'gr', 'ge', 'ls', 'le', 'eq', 'ne']


'''
# Expressions ############################################
E -> 'let' D 'in' E => 'let'
-> 'fn' Vb+ '.' E => 'lambda'
-> Ew;
Ew -> T 'where' Dr => 'where'
-> T;
'''

def E():
    # print(tokens[0].value, "E")
    if tokens[0].value == 'let':
        node = Node('let')
        ast_nodes.append('let')
        tokens.pop(0)
        
        node3 = D()
        
        if node: 
            
            node.children.append(node3)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)

        if len(tokens) > 0 and tokens[0].value == 'in':
            tokens.pop(0)
            
            node2 = E()
            
            if node: 
                node.children.append(node2)
                # print(str(node1.value), list(child.value for child in node1.children if child))
        
        else:
            raise SyntaxError("Error: Expected 'in' after 'let'")

        return node

    elif tokens[0].value == 'fn':
        node = Node('lambda')
        ast_nodes.append('lambda')
        tokens.pop(0)
        
        node1 = Vb()
        
        if node: 
            
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)  # Add node1 as a child, not to ast_nodes

        while tokens[0].value != '.':
            node2 = Vb()
            
            if node: 
                
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)

        if len(tokens) > 0 and tokens[0].value == '.':
            token_value = tokens[0].value
            tokens.pop(0)
            node3 = Node(token_value)  # Use the saved value
            ast_nodes.append(token_value)
            
            if node:
                node.children.append(node3)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            
            node4 = E()
            
            if node: 
                
                node.children.append(node4)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
    
            return node
    else:
        node = Ew()

        return node


'''Ew	->T 'where' Dr			=> 'where'
			->T;
'''

def Ew():
    # print(tokens[0].value, "Ew")
    node1 = T()
    if len(tokens) > 0 and tokens[0].value == 'where':
        node = Node('where')
        
        if node:
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        ast_nodes.append('where')
        tokens.pop(0)
        
        node2 = Dr()
        
        if node:
            node.children.append(node2)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node
    
    return node1
        


'''T 	-> Ta ( ',' Ta )+ => 'tau'
			-> Ta ;
'''
def T():
    # print(tokens[0].value, "T")
    node1 = Ta()
    
    if len(tokens) > 1 and tokens[0].value == ',':
        node = Node('tau')
        
        if node: 
            
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        ast_nodes.append('tau')

        while len(tokens) > 0 and tokens[0].value == ',':
            tokens.pop(0)
            node2 = Ta()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node
    
    return node1


'''Ta 	-> Ta 'aug' Tc => 'aug'
				-> Tc ;
'''
def Ta():
    # print(tokens[0].value, "Ta")
    node1 = Tc()
    if len(tokens) > 0 and tokens[0].value == 'aug':
        while len(tokens) > 0 and tokens[0].value == 'aug':
            node = Node('aug')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('aug')
            tokens.pop(0)
            
            node2 = Tc()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node
    return node1


'''Tc 	-> B '->' Tc '|' Tc => '->'
			-> B ;
'''
def Tc():
    # print(tokens[0].value, "Tc")
    node1 = B()
    if len(tokens) > 0 and tokens[0].value == '->':
        node = Node('->')
        
        if node:
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        ast_nodes.append('->')
        tokens.pop(0)

        node2 = Tc()
        
        if node: 
            
            node.children.append(node2)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)

        if tokens[0].value == '|':
            tokens.pop(0)
            node3 = Tc()
            
            if node:
                node.children.append(node3)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)

        else:
            raise SyntaxError("Error: Expected '|'")
        return node
    return node1
            


'''B 	-> B 'or' Bt 	=> 'or'
			-> Bt ;
'''
def B():
    # print(tokens[0].value, "B")
    node1 = Bt()
    if len(tokens) > 0 and tokens[0].value == 'or':
        while len(tokens) > 0 and tokens[0].value == 'or':
            node = Node('or')
            
            if node: 
                
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('or')
            tokens.pop(0)
            
            node2 = Bt()
            
            if node: 
                
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node
    return node1


'''Bt	-> Bt '&' Bs => '&'
			-> Bs ;
'''
def Bt():
    # print(tokens[0].value, "Bt")
    node1 = Bs()
    if len(tokens) > 0 and tokens[0].value == '&':
        while len(tokens) > 0 and tokens[0].value == '&':
            node = Node('&')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('&')
            tokens.pop(0)
            
            node2 = Bs()
            
            if node: 
                
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node
    return node1


'''Bs	-> 'not' Bp => 'not'
			-> Bp ;
'''
def Bs():
    # print(tokens[0].value, "Bs")
    if tokens[0].value == 'not':
        node = Node('not')
        ast_nodes.append('not')
        tokens.pop(0)

        node1 = Bp()
        
        if node: 
            
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)

        return node
        
    else:
        return Bp()


'''Bp 	-> A ('gr' | '>' ) A => 'gr'
			-> A ('ge' | '>=') A => 'ge'
			-> A ('ls' | '<' ) A => 'ls'
			-> A ('le' | '<=') A => 'le'
			-> A 'eq' A => 'eq'
			-> A 'ne' A => 'ne'
			-> A ;
'''
def Bp():
    # print(tokens[0].value, "Bp")
    node1 = A()
    if len(tokens) > 0 and (tokens[0].value == 'gr' or tokens[0].value == '>' or tokens[0].value == 'ge' or tokens[0].value == '>=' or tokens[0].value == 'ls' or tokens[0].value == '<' or tokens[0].value == 'le' or tokens[0].value == '<=' or tokens[0].value == 'eq' or tokens[0].value == 'ne'):
        if tokens[0].value == 'gr' or tokens[0].value == '>':
            node = Node('gr')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('gr')
            tokens.pop(0)

            node2 = A()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            return node
            
        elif tokens[0].value == 'ge' or tokens[0].value == '>=':
            node = Node('ge')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('ge')
            tokens.pop(0)
            
            node2 = A()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            return node
            
        elif tokens[0].value == 'ls' or tokens[0].value == '<':
            node = Node('ls')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('ls')
            tokens.pop(0)
            
            node2 = A()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            return node
            
        elif tokens[0].value == 'le' or tokens[0].value == '<=':
            node = Node('le')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('le')
            tokens.pop(0)
            
            node2 = A()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            return node
            
        elif tokens[0].value == 'eq':
            node = Node('eq')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('eq')
            tokens.pop(0)
            
            node2 = A()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            return node
            
        elif tokens[0].value == 'ne':
            node = Node('ne')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('ne')
            tokens.pop(0)
            
            node2 = A()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            return node
    return node1


'''A 	-> A '+' At => '+'
			-> A '-' At => '-'
			->	 '+' At
			->	 '-'At =>'neg'
			-> At ;
'''
def A():
    # print(tokens[0].value, "A")
    if tokens[0].value == '+':
        tokens.pop(0)
        return At()

    elif tokens[0].value == '-':
        node = Node('neg')
        ast_nodes.append('neg')
        tokens.pop(0)
        
        node1 = At()
        
        if node:
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)

        return node
        
    else:
        node1 = At()
        if len(tokens) > 0 and (tokens[0].value == '+' or tokens[0].value == '-'):
            while len(tokens) > 0 and (tokens[0].value == '+' or tokens[0].value == '-'):
                if tokens[0].value == '+':
                    node = Node('+')
                    if node:
                        node.children.append(node1)
                        # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                    ast_nodes.append('+')
                    tokens.pop(0)
                    
                    node2 = At()
                    
                    if node:
                        node.children.append(node2)
                        # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                    
                    if len(tokens) > 0 and (tokens[0].value == '+' or tokens[0].value == '-'):
                        node1 = node
                        continue
                    
                elif tokens[0].value == '-':
                    node = Node('-')
                    
                    if node:
                        node.children.append(node1)
                        # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                    ast_nodes.append('-')
                    tokens.pop(0)
                    
                    node2 = At()
                    
                    if node:
                        node.children.append(node2)
                        # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                    if len(tokens) > 0 and (tokens[0].value == '+' or tokens[0].value == '-'):
                        node1 = node
                        continue
                return node
        return node1
                

'''At 	-> At '*' Af => '*'
				-> At '/' Af => '/'
				-> Af ;
'''
def At():
    # print(tokens[0].value, "At")
    node1 = Af()
    if len(tokens) > 0 and (tokens[0].value == '*' or tokens[0].value == '/'):
        while len(tokens) > 0 and (tokens[0].value == '*' or tokens[0].value == '/'):
            if tokens[0].value == '*':
                node = Node('*')
                
                if node:
                    node.children.append(node1)
                    # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                ast_nodes.append('*')
                tokens.pop(0)
                
                node2 = Af()
                
                if node:
                    node.children.append(node2)
                    # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                if len(tokens) > 0 and (tokens[0].value == '*' or tokens[0].value == '/'):
                    node1 = node
                    continue
                
            elif tokens[0].value == '/':
                node = Node('/')
                
                if node:
                    node.children.append(node1)
                    # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                ast_nodes.append('/')
                tokens.pop(0)
                
                node2 = Af()
                
                if node:
                    node.children.append(node2)
                    # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                if len(tokens) > 0 and (tokens[0].value == '*' or tokens[0].value == '/'):
                    node1 = node
                    continue
            return node
    return node1
            


'''Af 	-> Ap '**' Af => '**'
				-> Ap ;
'''
def Af():
    # print(tokens[0].value, "Af")
    node1 = Ap()
    if len(tokens) > 0 and tokens[0].value == '**':
        while len(tokens) > 0 and tokens[0].value == '**':
            node = Node('**')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('**')
            tokens.pop(0)
            
            node2 = Af()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node
    return node1
        


'''Ap 	-> Ap '@' TokenType.ID R => '@'
				-> R ;
'''
def Ap():
    # print(tokens[0].value, "Ap")
    node1 = R()
    if len(tokens) > 0 and tokens[0].value == '@':
        while len(tokens) > 0 and tokens[0].value == '@':
            node = Node('@')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('@')
            tokens.pop(0)
            
            if tokens[0].type == TokenType.ID:
                token_value = tokens[0]
                node2 = Node(token_value)
                
                if node:
                    node.children.append(node2)
                    # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                ast_nodes.append(tokens.pop(0).value)
                
                node3 = R()
                
                if node:
                    node.children.append(node3)
                    # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                
            else:
                raise SyntaxError("Error: Expected TokenType.ID after '@'")
        
        # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node    
    return node1


'''R 	-> R Rn => 'gamma'
				-> Rn ;
'''
def R():
    # print(tokens[0].value, "R")
    node1 = Rn()
        
    while len(tokens) > 0 and (tokens[0].type == TokenType.ID or tokens[0].type == TokenType.INT or tokens[0].type == TokenType.STR or tokens[0].value == 'true' or tokens[0].value == 'false' or tokens[0].value == 'nil' or tokens[0].value == 'dummy' or str(tokens[0]) == '('):
        node = Node('gamma')
        ast_nodes.append('gamma')

        node2 = Rn()
        
        if node: 
            node.children.append(node1)
            node.children.append(node2)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        if len(tokens) > 0 and tokens[0].value not in keywords and (tokens[0].type == TokenType.ID or tokens[0].type == TokenType.INT or tokens[0].type == TokenType.STR or tokens[0].value == 'true' or tokens[0].value == 'false' or tokens[0].value == 'nil' or tokens[0].value == 'dummy' or str(tokens[0]) == '('):
            node1 = node
            continue
        else: return node
    return node1


'''Rn 	-> TokenType.ID
				-> TokenType.INT
				-> TokenType.STR
				-> 'true' => 'true'
				-> 'false' => 'false'
				-> 'nil' => 'nil'
				-> '(' E ')'
				-> 'dummy' => 'dummy' ;
'''
def Rn():
    # print(tokens[0].value, "Rn")
    if tokens[0].type == TokenType.ID:
        node = Node(tokens[0])
        ast_nodes.append(tokens.pop(0))

        return node
        
    elif tokens[0].type == TokenType.INT:
        node = Node(tokens[0])
        ast_nodes.append(tokens.pop(0))

        return node
        
    elif tokens[0].type == TokenType.STR:
        node = Node(tokens[0])
        ast_nodes.append(tokens.pop(0))

        return node
        
    elif tokens[0].value == 'true':
        tokens.pop(0)
        node = Node('true')
        ast_nodes.append('true')

        return node

    elif tokens[0].value == 'false':
        tokens.pop(0)
        node = Node('false')
        ast_nodes.append('false')

        return node

    elif tokens[0].value == 'nil':
        tokens.pop(0)
        node = Node('nil')
        ast_nodes.append('nil')

        return node

    elif str(tokens[0]) == '(':
        tokens.pop(0)
        node = E()
        if str(tokens[0]) == ')':
            tokens.pop(0)
    
            return node
        else:
            raise SyntaxError("Error: Expected ')'")
    elif tokens[0].value == 'dummy':
        tokens.pop(0)
        node = Node('dummy')
        ast_nodes.append('dummy')

        return node
    else:
        raise SyntaxError("Error: Expected a valid token")

'''D 	-> Da 'within' D => 'within'
				-> Da ;
'''
def D():
    # print(tokens[0].value, "D")
    node1 = Da()
    if tokens[0].value == 'within':
        node = Node('within')
        
        if node:
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        ast_nodes.append('within')
        tokens.pop(0)
        
        node2 = D()
        
        if node:
            node.children.append(node2)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node
    return node1
        

'''Da  -> Dr ( 'and' Dr )+ => 'and'
					-> Dr ;
'''
def Da():
    # print(tokens[0].value, "Da")
    node1 = Dr()
    if len(tokens) > 0 and tokens[0].value == 'and':
        while tokens[0].value == 'and':
            tokens.pop(0)
            node = Node('and')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('and')
            
            node2 = Dr()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        return node
    return node1


'''Dr  -> 'rec' Db => 'rec'
					-> Db ;
'''
def Dr():
    # print(tokens[0].value, "Dr")
    if tokens[0].value == 'rec':
        tokens.pop(0)
        node = Node('rec')
        ast_nodes.append('rec')
        
        node1 = Db()
        
        if node:
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)

        return node
        
    else:
        return Db()


'''Db  -> Vl '=' E => '='
				-> TokenType.ID Vb+ '=' E => 'fcn_form'
				-> '(' D ')' ; 
'''
def Db():
    # print(tokens[0].value, "Db")
    if tokens[0].type == TokenType.ID:
        node = Node('function_form')
        ast_nodes.append('function_form')
        
        node1 = Vb()
        
        if node:
            node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)

        while tokens[0].value != '=':
            node2 = Vb()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        if tokens[0].value == '=':
            tokens.pop(0)
            node3 = E()
            
            if node:
                node.children.append(node3)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
    
            return node
            
        else:
            raise SyntaxError("Error: Expected '='")
        
    elif str(tokens[0]) == '(':
        tokens.pop(0)
        
        node = D()
        if str(tokens[0]) == ')':
            tokens.pop(0)
    
            return node
            
        else:
            raise SyntaxError("Error: Expected ')'")
    
    else:
        node1 = Vl()
        if tokens[0].value == '=':
            tokens.pop(0)
            node = Node('=')
            
            if node:
                node.children.append(node1)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            ast_nodes.append('=')
            
            node2 = E()
            
            if node:
                node.children.append(node2)
                # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
            return node
        else:
            raise SyntaxError("Error: Expected '='")
            
    

'''Vb  -> TokenType.ID
			-> '(' Vl ')'
			-> '(' ')' => '()';
'''
def Vb():
    # print(tokens[0].value, "Vb")
    if tokens[0].type == TokenType.ID:
        node = Node(tokens[0])
        ast_nodes.append(tokens.pop(0))

        return node
        
    elif str(tokens[0]) == '(':
        tokens.pop(0)
        
        if str(tokens[0]) == ')':
            tokens.pop(0)
            node = Node('()')
            ast_nodes.append('()')
    
            return node
        
        node = Vl()
        if str(tokens[0]) == ')':
           
            tokens.pop(0)
    
            return node
        else:
            raise SyntaxError("Error: Expected a valid token")
        
    
    

'''Vl -> TokenType.ID list ',' => ','?
'''
def Vl():
    # print(tokens[0].value, "Vl")
    if tokens[0].type == TokenType.ID:
        # node = Node("','?")
        # ast_nodes.append("','?")

        node1 = Node(tokens[0])
        ast_nodes.append(tokens.pop(0))

        if tokens[0].value == ',':
            node = Node(',')
            ast_nodes.append(',')
        
            if node:
                node.children.append(node1)
            # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
        else:
            return node1

        while tokens[0].value == ',':
            tokens.pop(0)
            if tokens[0].type == TokenType.ID:
                node3 = Node(tokens[0])
                ast_nodes.append(tokens.pop(0))
                
                if node:
                    node.children.append(node3)
                    # print(str(node.value), list(child.value for child in node.children if child), tokens[0].value)
                 
            else:
                raise SyntaxError("Error: Expected TokenType.ID after ','")
        return node
                
    else:
        raise SyntaxError("Error: Expected TokenType.ID after ','")


def parser(source_code):
    global tokens
    tokens = Lexer(source_code).tokenize()
    return E()

def print_ast(source_code):
    root = parser(source_code)
    ast = AST(root)
    ast.pre_order_traverse(root)
    return ast


# source_code = """
# let Sum(A) = Psum (A,Order A )
# where rec Psum (T,N) = N eq 0 -> 0
#  | Psum(T,N-1)+T N
# in Print ( Sum (1,2,3,4,5) )
# """

# print_ast(source_code)