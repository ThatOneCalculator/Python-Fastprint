# Python-Fastprint
I'm sure this was done before, but this is an easy way to print long strings in Python 3. 

Python3 module to print out text.

Install:
`pip install fastprint`

Usage:

```python
from fastprint import pr

pr("long\ntext") # each line takes 1 second
pr("other\n\long\text", 0.2) # each line takes 0.2 seconds
```
