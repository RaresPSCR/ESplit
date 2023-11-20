def no = 0
def nt = 1
def ct = 0

if (ct == 10)
    goto 15
endif

print no
def aux = no+nt
no= nt
nt= aux
ct = ct+1
goto 4

print "finish"