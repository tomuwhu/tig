# Elemi algoritmusok

## Lineáris algoritmusok

- eldöntés
  - all()
  - any()
  - in
  - not in
- leszámlálás
  - len()
  - [].count()

```python
lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
print ([ [l, lst.count(l)] for l in set(lst)])
print (dict( (l, lst.count(l) ) for l in set(lst)))
```

- kiválasztás, keresés

- leválogatás, szétválogatás
  - filter()
  
- összegzés
  - sum()

- halmazműveletek

[Függvények](https://docs.python.org/3/library/functions.html)