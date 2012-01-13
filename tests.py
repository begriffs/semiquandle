import axioms
import filler

for i in range(3**(3*3)):
        tablefunc = axioms.t2f(filler.ithNTable(2, i))
        if axioms.check(range(2), tablefunc, tablefunc, axioms.semiquandle):
                print i
