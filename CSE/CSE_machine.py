from CSE.Closure import Closure, ClosuerEta
from CSE.utils import lookup, apply_operator

class CSEMachine:
    def __init__(self, control_structures):
        self.stack = ['e0']
        self.environment = [{}]  
        self.control = ['e0'] + list(control_structures["δ0"]) #list(reversed(control_structures["δ0"]))  # reverse for stack-like processing
        self.control_structures = control_structures

    def _current_env(self):
        return self.environment[-1]

    def run(self):
        while self.control:
            # print(f"\nControl: {self.control}")
            # print(f"Stack: {self.stack}")
            # print(f"Enviornment: {self.environment}")
            instr = self.control.pop()
            # print(f"now we are popping : {instr}\n")

            if isinstance(instr, str):
                if instr == 'gamma':  # CSE Rule 3 or Rule 4
                    self._apply_gamma()

                elif instr == "β":
                    self._apply_beta()

                elif instr == '<nil>':
                    self.stack.append('nil')
                
                elif instr == '<dummy>':
                    self.stack.append('dummy')

                elif instr == 'aug':
                    self._apply_aug()

                elif instr in ['+', '-', '**', '*', '/', '&', '|', 'eq', 'le','not','ls','neg','gr','ge','ne']:
                    if instr == 'not' or instr == 'neg':
                        operand = self.stack.pop()
                        result = apply_operator(instr, operand, None)

                    else:
                        right = self.stack.pop()
                        left = self.stack.pop()
                        #self.control.pop()
                        #self.control.pop()
                        if self.control and self.control[-1] == 'gamma':
                            self.control.pop()  
                            if self.control:
                                self.control.pop() 
                        result = apply_operator(instr, left, right)
                        # print("Result is :",result)
                    self.stack.append(result)

                elif instr.startswith('e') and instr[1:].isdigit():  #  CSE Rule 5
                    return_value = self.stack.pop()   
                    env_marker = self.stack.pop()
                    self.environment.pop()  # Exit the environment     
                    # print(f"Exiting environment {env_marker} and preserving return value: {return_value}")
                    self.stack.append(return_value)   
                    
                elif instr == '<Y*>':
                    self.stack.append('Y*')

                else:  # CSE Rule 1: variable name
                    #val = lookup(instr, self._current_env())
                    #self.stack.append(val)

                    # Check if instr is a literal tag like <INT:3> or <STR:'hello'>
                    if instr.startswith('<') and ':' in instr and instr.endswith('>'):
                        try:
                            tag_type, raw_val = instr[1:-1].split(':', 1)
                            if tag_type == 'INT':
                                val = int(raw_val)
                            elif tag_type == 'STR':
                                val = eval(raw_val)  # handles quotes, e.g. "'hello'"
                            elif tag_type == 'ID':
                                new_val ="<ID:"+raw_val+">"

                                if new_val == "<ID:print>" or new_val == "<ID:Print>":
                                    self._apply_print()

                                elif new_val == "<ID:order>" or new_val == "<ID:Order>":
                                    self._apply_order()
                                    continue

                                elif new_val == "<ID:Conc>" or new_val == "<ID:conc>":
                                    self._apply_conc()
                                    continue

                                elif new_val == "<ID:Stem>" or new_val == "<ID:stem>":
                                    self._apply_stem()
                                    continue

                                elif new_val == "<ID:Stern>" or new_val == "<ID:stern>":
                                    self._apply_stern()
                                    continue
                                 
                                elif new_val == "<ID:Istuple>":
                                    self._apply_istuple()
                                    continue

                                elif new_val == "<ID:Isinteger>":
                                    self._apply_isinteger()
                                    continue

                                elif new_val == "<ID:Istruthvalue>":
                                    self._apply_istruthvalue()
                                    continue
                                
                                elif new_val == "<ID:Isstring>":
                                    self._apply_isstring()
                                    continue
                                
                                elif new_val == "<ID:Isfunction>":
                                    self._apply_isfunction()
                                    continue
                                
                                elif new_val == "<ID:Isdummy>":
                                    self._apply_isdummy()
                                    continue
                                
                                else:
                                    val = lookup(new_val, self._current_env(),self.environment)
                                #self.stack.append(val)
                            else:
                                raise Exception(f"Unsupported literal type: {tag_type}")
                            self.stack.append(val)
                        except Exception as e:
                            raise Exception(f"Failed to parse tagged literal {instr}: {e}")
                    else:
                        
                        val = lookup(instr, self._current_env(), self.environment)
                        self.stack.append(val)

            elif isinstance(instr, tuple) and instr[0] == 'lambda':  # CSE Rule 2
                _, k, x = instr
                closure = Closure(k, x, self._current_env())
                self.stack.append(closure)

            elif isinstance(instr, tuple) and instr[0] == '𝜏':  # Tuple constructor (if you use it) 𝜏
                n = instr[1]
                tuple_values = [self.stack.pop() for _ in range(n)]
                self.stack.append(tuple(reversed(tuple_values)))

            #elif isinstance(instr, str) and instr in ['+', '-', '*', '/', 'eq', 'le', 'not','ls','neg','gr','ge','ne']:  # Operators
                #right = self.stack.pop()
                #left = self.stack.pop() if instr != 'not' else None
                #result = apply_operator(instr, left, right)
                #self.stack.append(result)

            else:
                # Assume literals (int, etc.)
                self.stack.append(instr)
        # print(self.stack)
        return self.stack
    

    def _apply_gamma(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow: Not enough elements to apply 'gamma'")

        rand = self.stack.pop()
        rator = self.stack.pop()
        # print('rand : ',rand , 'and rator :',rator)
        if isinstance(rand, str) and not rator:
            self.stack.append('dummy')
            return

        if isinstance(rand, Closure):  # Rule 4 ,Rule 10 and Rule 11
            closure = rand
            new_env = closure.env.copy()

            # print("\nThis is the env :",closure.delta_index, closure.env)

            if isinstance(rator, tuple) and isinstance(rand, int): #Rule 10
                if 1 <= rand <= len(rator):  
                    self.stack.append(rator[rand - 1])
                    return
                else:
                    raise Exception(f"Index {rand} out of bounds for tuple of length {len(rator)}")

            if isinstance(closure.var, list): #Rule 11
                # print('Now this is the correct path to go')
                reversed_vars = list(reversed(closure.var))
                
                # print('\nrator is:', rator)

                if not isinstance(rator, tuple) or len(rator) != len(reversed_vars):
                    raise Exception("Mismatch between number of arguments and parameters")

                for i in range(len(reversed_vars)):
                    param = reversed_vars[i]
                    arg = rator[i]
                    new_env[param] = arg

            
            else: # Rule 4
                new_env[closure.var] = rator  

            self.environment.append(new_env)
            
            new_env_label = f"e{len(self.environment) - 1}"


            delta_label = f"δ{closure.delta_index}"
            if delta_label not in self.control_structures:
                raise Exception(f"Missing control structure: {delta_label}")

            new_control =list(self.control_structures[delta_label]) #list(reversed(self.control_structures[delta_label]))
            self.control.extend([new_env_label]+new_control)
            self.stack.append(new_env_label)

        elif isinstance(rator, Closure) and rand == 'Y*':
            # Rule 12
            closure = rator
            # print("This is the closure :",closure)
            # new_env = closure.env.copy()
            # print("This is the New Env :",new_env)
            n_closure = ClosuerEta(closure.delta_index, closure.var, closure.env)
            # new_env[closure.var] = n_closure
            # self.environment.append(new_env)
            self.stack.append(n_closure)

        elif isinstance(rand, ClosuerEta):
            self.stack.append(rator)  # Push the rator back to the stack for further processing
            self.stack.append(rand)  # Rule 13, just push the eta closure back to the stack
            self.stack.append(Closure(rand.delta_index, rand.var, rand.env))
            self.control.append('gamma')  # Reapply gamma for eta closure
            self.control.append('gamma')  # Reapply gamma for the rator

            # print("This is the new control :",self.control)

        elif isinstance(rand, tuple) and isinstance(rator, int):
            if 1 <= rator <= len(rand):  # Rule 9
                self.stack.append(rand[len(rand) - rator])
        else:
            # Rule 3
            result = apply_operator("gamma", rator, rand)
            self.stack.append(result)


    def _apply_beta(self):
        condition = self.stack.pop()
        # print("The condition is :",condition)

        if len(self.control) < 2:
            raise Exception("Control underflow: Not enough elements to apply β")

        false_branch = self.control.pop()
        true_branch = self.control.pop()
        # print('False_branch :',false_branch, "and True_branch :",true_branch)

        if condition == True:
            chosen_branch = true_branch
        elif condition == False:
            chosen_branch = false_branch

        # print('chosen_branch : ',chosen_branch)
        if chosen_branch not in self.control_structures:
            raise Exception(f"Missing control structure: {chosen_branch}")

        new_control = list(self.control_structures[chosen_branch])
        self.control.extend(new_control)

    def _apply_print(self):
        self.control.pop()
        # print("This is what I got now :\ncontrol",self.control,"and stack",self.stack)
        print(self.stack.pop(), end='')

    def _apply_order(self):
        self.control.pop()
        # print("This is what I got now :\ncontrol",self.control,"and stack",self.stack)
        self.stack.append((len(self.stack.pop())))

    def _apply_aug(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow: Not enough elements to apply 'aug'")

        rator = self.stack.pop()
        if rator == 'nil':
            rand = self.stack.pop()
            self.stack.append((rand,))
        elif isinstance(rator, tuple):
            rand = self.stack.pop()
            new_tuple = rator + (rand,)
            self.stack.append(new_tuple)
        
    def _apply_conc(self):
        self.control.pop()
        self.control.pop()
        rand1 = self.stack.pop()
        rand2 = self.stack.pop()

        if isinstance(rand1, str) and isinstance(rand2, str):
            new_str = rand1 + rand2
            self.stack.append(new_str)

    def _apply_istuple(self):
        self.control.pop()
        rand = self.stack.pop()
        if isinstance(rand, tuple):
            self.stack.append(True)
        else:
            self.stack.append(False)
    
    def _apply_isinteger(self):
        self.control.pop()
        rand = self.stack.pop()
        if isinstance(rand, int):
            self.stack.append(True)
        else:
            self.stack.append(False)

    def _apply_istruthvalue(self):
        self.control.pop()
        rand = self.stack.pop()
        if isinstance(rand, bool):
            self.stack.append(True)
        else:
            self.stack.append(False)

    def _apply_isstring(self):
        self.control.pop()
        rand = self.stack.pop()
        if isinstance(rand, str):
            self.stack.append(True)
        else:
            self.stack.append(False)
    
    def _apply_isfunction(self):
        self.control.pop()
        rand = self.stack.pop()
        if isinstance(rand, Closure) or isinstance(rand, ClosuerEta):
            self.stack.append(True)
        else:
            self.stack.append(False)

    def _apply_isdummy(self):
        self.control.pop()
        rand = self.stack.pop()
        if isinstance(rand, str) and rand == 'dummy' or rand == '<dummy>':
            self.stack.append(True)
        else:
            self.stack.append(False)

    def _apply_stem(self):
        self.control.pop()
        rand = self.stack.pop()
        if isinstance(rand, str):
            stemmed_word = rand[0]
            self.stack.append(stemmed_word)
        else:
            raise Exception("Stem operation can only be applied to strings.")
        
    def _apply_stern(self):
        self.control.pop()
        rand = self.stack.pop()
        if isinstance(rand, str):
            stemmed_word = rand[1:]
            self.stack.append(stemmed_word)
        else:
            raise Exception("Stem operation can only be applied to strings.")