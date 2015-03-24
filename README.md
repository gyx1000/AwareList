# AwareList

AwareList is a simple python class able to keep trace of added and removed elements. 

### Use

Initialisation:
```python
aw_list = AwareList(["Element1", "Element2"]
```

Work like a normal list:
```python
aw_list += ["New element"]
aw_list.append("New append")
aw_list.pop()
aw_list.remove("Element1")
aw_list.extend(["Extend 1", "Extend 2"])
aw_list.insert(2, "New Insert")
aw_list[0:1] = ["Element 1", "Element 2"]
del aw_list[2]
```

Access added and removed lists:
```python
aw_list.added
aw_list.removed
```
### Version
0.0.1

### Todo's

 - Write setup.py
 - Implement Travis-CI
 - Add Code Comments

License
----

MIT
