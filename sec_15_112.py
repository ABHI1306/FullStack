import re

def multi_re_find(patt,phr):
    for p in patt:
        print("I'm searching for: "+p)
        print(re.findall(p, phr))

test_ph = 'sdsd..sssddd...sdsdsdsdd...sds...dsdsd.s.d.sdssdd'
test_pat = ['sd*']
multi_re_find(test_pat, test_ph)



