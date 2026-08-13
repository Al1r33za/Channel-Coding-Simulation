
from gf import *
import lrsolve
import cir, poly


def encode(n, k, t, /, u: list, gen: list, field):
    '''Encode nonbinary BCH/RS-like code using an LFSR division.'''
    alph, loga = field[0], field[1]
    if len(gen) <= 1:
        return u[:]
    if gen[-1] != alph[0]:
        raise ValueError('Generator polynomial must be monic')
    
    regs = [0] * (len(gen) - 1)
    u =(regs + u).copy()
    for uu in reversed(u):
        lead = regs[-1]
        regs[1:] = regs[:-1]
        regs[0] = uu
        if lead != 0:
            for j in range(len(gen) - 1):
                regs[j] ^= mul(lead, gen[j], field)

    return regs + u[len(regs):]

def encode_textbook(n, k, t, /, u: list, gen: list, field):
    '''Encode a non-binary BCH/RS-like codeword with length n using long division.'''
    alph, loga = field[0], field[1]
    codeword = [0] * (len(gen) - 1) + u
    q, r = poly.long_div(codeword, gen, field)
    codeword = r + codeword[len(r):]
    return codeword


def syndrome(n, k, t, /, r: list, field) -> tuple:
    """Calculate the non-binary BCH/RS syndrome over the actual received length."""
    alph, loga = field[0], field[1]

    if len(r) == 0:
        return [0] * (2 * t)

    code_len = len(r)
    S = [0] * (2 * t)
    S1 = [0] * code_len

    for i, rr in enumerate(r):
        ai = power(alph[1], i, field)
        S1[i] = mul(rr, ai, field)

    for i in range(2 * t):
        for ss in S1:
            S[i] ^= ss
        for j in range(code_len):
            aj = power(alph[1], j, field)
            S1[j] = mul(S1[j], aj, field)

    return S


def forney_algorithm(L: list, Z: list, loc, field) -> list:
    '''Calculate error values using the Forney error-evaluation formula.'''
    alph, loga = field[0], field[1]

    dL = poly.diff(L)
    error_values = []
    for wj in loc:
        try:
            dk = div(poly.eval(Z, wj, field),
                    poly.eval(dL,wj, field), field)
            error_values.append(dk)
        except ZeroDivisionError:
            error_values.append(0)

    # error_values.reverse()
    return error_values


def decode(n, k, t, /, r: list, field) -> tuple:
    '''Decode a non-binary BCH/RS codeword using Berlekamp-Massey and Forney.'''
    alph, loga = field[0], field[1]

    if (len(r) != n):
        raise ValueError('dimension error: r not n bit!')
 
    S = syndrome(n, k, t, r=r, field=field)
    c = r[(n-k):]

    # check if syndrome is zero:
    if all(v == 0 for v in S):
        return c, [], []

    L, Z = lrsolve.BM(S, field)
    loc = lrsolve.chien_search(L, field)

    # check if decoder failed:
    # if (len(L) - 1 > t):
    #     raise ValueError('rs decoder failed!')

    error_locations = []
    error_values = []
    u_star = list(r)

    for ll in loc:
        ll = inv(ll, field)
        error_locations.append(loga[ll])
    
    if error_locations:
        error_values = forney_algorithm(L, Z, loc, field)
        for loc, value in zip(error_locations, error_values):
            if 0 <= loc < len(u_star):
                u_star[loc] ^= value
            else:
                break

    # If the result is a no-correction decoder state, keep the pipeline honest.
    if error_values and all(v == 0 for v in error_values):
        error_locations = []
        error_values = []

    return u_star[n-k:], error_locations, error_values