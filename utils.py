def lookup(name, env):
    if name in env:
        return env[name]
    raise Exception(f"Variable '{name}' not found in environment.")

def apply_operator(op, left, right=None):
    if op == '+':
        return right + left
    elif op == '-':
        return right - left
    elif op == '*':
        return right * left
    elif op == '/':
        return right // left  # or float(left) / right
    elif op == 'eq':
        return right == left
    elif op == 'lt':
        return right < left
    elif op == 'not':
        return not right
    elif op == 'gamma':  # only when rator is not closure (basic function call maybe)
        if callable(right):
            return left(left)
        raise Exception("Cannot apply gamma to non-closure.")
    else:
        raise Exception(f"Unknown operator: {op}")
