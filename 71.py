string=raw_input()
rev_string=reversed(string)
if list(string)==list(rev_string):
    print "yes"
else:
    print "no"
