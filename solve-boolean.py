def solve_boolean(s):
    def eval_bool_expr(s):
        s = s.replace("&", " and ")
        s = s.replace("|", " or ")
        return eval(s)

    return eval_bool_expr(s)