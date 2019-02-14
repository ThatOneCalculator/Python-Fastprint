import time

st = """This is
the first
very long
string"""
def pr(st):
	for line in st.splitlines():
	    print(line)
	    time.sleep(1)
pr(st)
st="""
This is
the SECOND
one,
ok?\n
coolio.\n
This was made by
Kainoa Kanter
on 2/13/19
and `st` can
be replaced
with anything"""
pr(st)