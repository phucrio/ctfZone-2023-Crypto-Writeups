from gmpy2 import isqrt
import random as rnd
import logging
import re
import socketserver
from hashlib import blake2b
from Crypto.Cipher import AES
from py_ecc.fields import optimized_bn128_FQ
from py_ecc.optimized_bn128.optimized_curve import (
    Optimized_Point3D,
    normalize,
    G1,
    multiply,
    curve_order,
    add,
    neg,
)


def extended_euclidean_algorithm(a, b):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    r0, r1 = a, b
    
    #print("i\t r_i\t   s_i\t   t_i")
    #print("-" * 30)
    #print(f"0\t{r0}\t{s0}\t{t0}")
    #print(f"1\t{r1}\t{s1}\t{t1}")
    
    i = 1
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
        
        #print(f"{i}\t{r1}\t{s1}\t{t1}")
        i += 1
    
    return r0, s0, t0

a = 4898
b = 9972
gcd, s, t = extended_euclidean_algorithm(a, b)
# print(f"\nGCD({a}, {b}) = {gcd}")
# print(f"s = {s}, t = {t}")
# print(f"s * {a} + t * {b} = {s * a + t * b}")
# print(s * a + t * b == 2)

def egcd_step(prev_row, current_row):
    (s0, t0, r0) = prev_row
    (s1, t1, r1) = current_row
    q_i = r0 // r1
    return (s0 - q_i * s1, t0 - q_i * t1, r0 - q_i * r1)


def find_decomposers(lmbda, modulus):
    mod_root = isqrt(modulus)

    egcd_trace = [(1, 0, modulus), (0, 1, lmbda)]
    while egcd_trace[-2][2] >= mod_root:
        egcd_trace.append(egcd_step(egcd_trace[-2], egcd_trace[-1]))

    (_, t_l, r_l) = egcd_trace[-3]
    (_, t_l_plus_1, r_l_plus_1) = egcd_trace[-2]
    (_, t_l_plus_2, r_l_plus_2) = egcd_trace[-1]
    (a_1, b_1) = (r_l_plus_1, -t_l_plus_1)
    if (r_l**2 + t_l**2) <= (r_l_plus_2**2 + t_l_plus_2**2):
        (a_2, b_2) = (r_l, -t_l)
    else:
        (a_2, b_2) = (r_l_plus_2, -t_l_plus_2)

    return (a_1, b_1, a_2, b_2)


lmbda = 4407920970296243842393367215006156084916469457145843978461
beta = 2203960485148121921418603742825762020974279258880205651966

(a_1, b_1, a_2, b_2) = find_decomposers(lmbda, curve_order)


def compute_balanced_representation(scalar, modulus):
    c_1 = (b_2 * scalar) // modulus
    c_2 = (-b_1 * scalar) // modulus
    k_1 = scalar - c_1 * a_1 - c_2 * a_2
    k_2 = -c_1 * b_1 - c_2 * b_2
    return (k_1, k_2)


def multiply_with_endomorphism(x: int, y: int, scalar: int):
    assert scalar >= 0 and scalar < curve_order
    point = (optimized_bn128_FQ(x), optimized_bn128_FQ(y), optimized_bn128_FQ.one())
    endo_point = (
        optimized_bn128_FQ(x) * optimized_bn128_FQ(beta),
        optimized_bn128_FQ(y),
        optimized_bn128_FQ.one(),
    )
    print(point)
    print(endo_point)
    (k1, k2) = compute_balanced_representation(scalar, curve_order)
    #print("K decomposed:", k1, k2)
    if k1 < 0:
        point = neg(point)
        k1 = -k1
    if k2 < 0:
        endo_point = neg(endo_point)
        k2 = -k2
    return normalize(add(multiply(point, k1), multiply(endo_point, k2)))

print(normalize(G1))
#print(multiply_with_endomorphism(G1[0].n, G1[1].n, 1234))