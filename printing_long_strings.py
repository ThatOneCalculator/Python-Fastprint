import time
def pr(st):
	for line in st.splitlines():
	    print(line)
	    time.sleep(1)
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
on 2/13/19,
and `st` & `pr` can
be replaced
with anything"""
pr(st)
st="\nIt also\nkinda works with\nsingle quotes\nbut that kinda defeats\nthe purpose"
pr(st)
st="""\nCatch me
on Github!
My username is
ThatOneCalculator"""
pr(st)