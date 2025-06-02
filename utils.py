def lookup(name, env, env_list):
    # print("\nName :",name," and Env :", env)

    if name in env:
        return env[name]
    # Then check all environments in the list (from latest to earliest)
    for e in reversed(env_list):
        if name in e:
            return e[name]
    raise Exception(f"Variable '{name}' not found in environment.")

def apply_operator(op, left, right):
    # print('operator is :', op)
    # print('left: ', left, 'right: ', right)
    if op == '+':
        return right + left
    elif op == '-':
        return right - left
    elif op == '*':
        return right * left
    elif op == '**':
        return right ** left
    elif op == '/':
        return right // left  # or float(left) / right
    elif op in ['not']:
        return not left
    elif op == 'neg':
        return -left
    elif op == 'eq':
        return right == left
    elif op == 'ne':
        return right != left
    elif op == 'le':
        return right <= left
    elif op == 'ls':
        return right < left
    elif op == 'gr':
        return right > left
    elif op == 'ge':
        return right >= left
    elif op == '&':
        return right and left
    elif op == '|':
        return right or left
    elif op == 'gamma':
        if callable(right):
            return left(left)
        raise Exception("Cannot apply gamma to non-closure.")
    else:
        raise Exception(f"Unknown operator: {op}")
