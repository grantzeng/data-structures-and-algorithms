# Design 

Distinction between sequence vs. set interface: whether ordering is _intrinsic_ (stored values have a (total) order) or _extrinsic_ (keys have a (total) order but the values don't)


Priority queue interface possible implementations (see 6.006 Recitation 8)
- (selection sort + array)
- (insertion sort + sorted array)
- (heap sort + binary heap)

Interface needs to offer:
```python
build(n)

insert(x)

delete_max()
```

I'm not entirely sure what's going on, so going to type up all the code in Recitation 8 to see what they're trying to do.


> INTERRUPT: Going to implement sorts first before I come back to this, because this depends on knowing them (2024-01-31)