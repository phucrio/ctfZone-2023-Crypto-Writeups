var('k0 k334 k607 d')
h607 = 78282214192163227426682790111550511221164406262175233718002272476488812943257
r607 = 38231493725448632172369788987279761485606673579291907884585541142025488063778
s607 = 50064827529145556928345108181407617889944156406102271615957746106670382931497
h334 = 24338748425475181849259516650938772078855802211527109752420007020703396280987
r334 = 24428211383726462881348584800161555881744158778750242628824798906481919616162
s334 = 83729325612422400174915921934242523062368438550674357320667100019791865721531
h0 = 106132995759974998927623038931468101728092864039673367661724550078579493516352
r0 = 18051166252496627800102264022724027258301377836259456556817994423615643066667
s0 = 92640317177062616510163453417907524626349777891295335142117609371090060820235
n = 115792089210356248762697446949407573529996955224135760342422259061068512044369
Fp = GF(n)



A = Matrix(Fp,[[1,1,-1,0],[s0,0,0,-r0],[0,s334,0,-r334],[0,0,s607,-r607]])
V = vector([Fp(0),Fp(h0),Fp(h334),Fp(h607)])
r = A.solve_right(V)
print(r)