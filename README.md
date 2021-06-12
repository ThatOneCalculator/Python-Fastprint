# Python-Fastprint

Python 3 module to print out long strings of text with intervals of time inbetween

Install:
`pip install fastprint`

Sync Usage:

```python
from fastprint import pr

pr("long\ntext") # each line takes 1 second
pr("other\n\long\text", 0.2) # each line takes 0.2 seconds
```

Async usage:

```python
from async_fastprint import async_pr

async def foo:
    return async_pr("This\nis\nasynchrounous!")
```

Check out example.py for more
