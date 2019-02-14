import time
def pr(st, delay=1):
	for line in st.splitlines():
	    print(line)
	    delay==1
	    time.sleep(delay)
st = """This is
the first
very long
string"""
pr(st)
st="""
This is
the SECOND
one, ok?\n
coolio.\n"""
pr(st)
st="""\n\nThis was made by
Kainoa Kanter
on 2/13/19"""
pr(st)
st="\nIt also\nkinda works with\nsingle quotes\nbut that kinda defeats\nthe purpose"
pr(st)
st="""\nYou can also change the
print time!
This is at 0.3
instead of
1.0"""
pr(st, 0.3)
st="""\nCatch me
on Github!
My username is
ThatOneCalculator"""
pr(st)