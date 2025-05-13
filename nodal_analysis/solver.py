def solve(VLP, IPR):
    a = VLP.a
    b = IPR.a
    c = VLP.b - IPR.b
    D = b ** 2 - 4 * a * c
    Q = None

    if D > 0:
        x1 = (-b + D ** (1 / 2)) / (2 * a)
        x2 = (-b - D ** (1 / 2)) / (2 * a)
        if x1 > 0 or x2 > 0:
            Q = max(x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        if x > 0:
            Q = x
    else:
        return None, None

    return Q, VLP.production(Q)
