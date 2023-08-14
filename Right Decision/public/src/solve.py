from pwn import *

r = process(['python3', 'main.py'])
r.interactive()