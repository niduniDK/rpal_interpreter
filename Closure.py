class Closure:
    def __init__(self, delta_index, var, env):
        self.delta_index = delta_index
        self.var = var
        self.env = env

    def __repr__(self):
        return f"<Closure δ{self.delta_index} λ {self.var} env={self.env}>"
