import fastprint
import asyncio

# Sync (Blocking)
st = """This is
the first
very long
string"""
fastprint.run(st)
st="""
This is
the SECOND
one, ok?\n
coolio.\n"""
fastprint.run(st)
st="""\n\nThis was made by
Kainoa Kanter
on 2/13/19"""
fastprint.run(st)
st="\nIt also\nkinda works with\nsingle quotes\nbut that kinda defeats\nthe purpose"
fastprint.run(st)
st="""\nYou can also change the
print time!
This is at 0.3
instead of
1.0"""
fastprint.run(st, 0.3)
st="""\nCatch me
on Github!
My username is
ThatOneCalculator"""
fastprint.run(st)


# Asynchronous
st = """
This
is 
very long
its also 
async!
"""

async def foo:
    return fastprint.asyncrun(st)
