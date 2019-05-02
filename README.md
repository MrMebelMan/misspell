# misspell
Some functions that introduce random typographical errors in provided text.

make one typo:
```python
from misspell import make_typo

make_typo('test')  # tedt, tesw etc...
```

make typos in 50% of the characters:

```python
from misspell import make_typos
make_typos('Hello, world!', percent=50)  # 'Jell8, woelf!', 'Hdllo, sorld!' etc...
