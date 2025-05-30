from Closure import Closure
from utils import lookup, apply_operator

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
            print(f"\nControl: {self.control}")
            print(f"Stack: {self.stack}")
            print(f"Enviornment: {self.environment}")
            instr = self.control.pop()
            print(f"now we are popping : {instr}\n")

            if isinstance(instr, str):
                if instr == 'gamma':  # CSE Rule 3 or Rule 4
                    self._apply_gamma()

                elif instr == "β":
                    self._apply_beta()

                elif instr in ['+', '-', '*', '/', 'eq', 'le','not','ls','neg','gr','ge','ne']:
                    if instr == 'not' or instr == 'neg':
                        #operand = self.stack.pop()
                        result = apply_operator(instr, None, None)

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
                    self.stack.append(result)

                elif instr.startswith('e') and instr[1:].isdigit():  #  CSE Rule 5
                    return_value = self.stack.pop()   
                    env_marker = self.stack.pop()     
                    print(f"Exiting environment {env_marker} and preserving return value: {return_value}")
                    self.stack.append(return_value)   
                    

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
                                if new_val == "<ID:print>" :
                                    self._apply_print()
                                else:
                                    val = lookup(new_val, self._current_env())
                                #self.stack.append(val)
                            else:
                                raise Exception(f"Unsupported literal type: {tag_type}")
                            self.stack.append(val)
                        except Exception as e:
                            raise Exception(f"Failed to parse tagged literal {instr}: {e}")
                    else:
                        
                        val = lookup(instr, self._current_env())
                        self.stack.append(val)

            elif isinstance(instr, tuple) and instr[0] == 'lambda':  # CSE Rule 2
                _, k, x = instr
                closure = Closure(k, x, self._current_env())
                self.stack.append(closure)

            elif isinstance(instr, tuple) and instr[0] == 'tau':  # Tuple constructor (if you use it)
                n = instr[1]
                tuple_values = [self.stack.pop() for _ in range(n)]
                self.stack.append(tuple(reversed(tuple_values)))

            elif isinstance(instr, str) and instr in ['+', '-', '*', '/', 'eq', 'le', 'not','ls','neg','gr','ge','ne']:  # Operators
                right = self.stack.pop()
                left = self.stack.pop() if instr != 'not' else None
                result = apply_operator(instr, left, right)
                self.stack.append(result)

            else:
                # Assume literals (int, etc.)
                self.stack.append(instr)
        print(self.stack)
        return self.stack[-1]
    

    def _apply_gamma(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow: Not enough elements to apply 'gamma'")

        rand = self.stack.pop()
        rator = self.stack.pop()
        print('rand : ',rand , 'and rator :',rator)

        if isinstance(rand, Closure):  # Rule 4
            closure = rand
            new_env = closure.env.copy()
            
            new_env = closure.env.copy()
            new_env[closure.var] = rator  
            self.environment.append(new_env)
            
            new_env_label = f"e{len(self.environment) - 1}"


            delta_label = f"δ{closure.delta_index}"
            if delta_label not in self.control_structures:
                raise Exception(f"Missing control structure: {delta_label}")

            new_control =list(self.control_structures[delta_label]) #list(reversed(self.control_structures[delta_label]))
            self.control.extend([new_env_label]+new_control)
            self.stack.append(new_env_label)

        else:
            # Rule 3 (apply operator or built-in function)
            result = apply_operator("gamma", rator, rand)
            self.stack.append(result)

    def _apply_beta(self):
        condition = self.stack.pop()

        if len(self.control) < 2:
            raise Exception("Control underflow: Not enough elements to apply β")

        false_branch = self.control.pop()
        true_branch = self.control.pop()

        if condition == 'true':
            chosen_branch = true_branch
        else:
            chosen_branch = false_branch

        if chosen_branch not in self.control_structures:
            raise Exception(f"Missing control structure: {chosen_branch}")

        new_control = list(self.control_structures[chosen_branch])
        self.control.extend(new_control)

    def _apply_print(self):
        self.control.pop()
        print("This is what I got now :\ncontrol",self.control,"and stack",self.stack)
        self.stack.pop()