# scicfg

`scicfg` is a python hierarchical configuration structure designed for scientific experiments.

```python
import scicfg

t = scicfg.SciConfig()
t.temperature = 10
t._branch('experiment1')
t.experiment1.duration = 3600.0
```

### Status

`scicfg` is considered beta at this point. It has a rich collection of unitary tests, but it has not been used enough in practical situations to be considered stable or mature.

### Design

`scicfg` has been designed to be easy to use while ensuring data integrity. It features many ways to protect the tree data incorrect inputs. It also features coverage and history logging, enabling the ability to check that the data structure was correctly used during an experiment. Because the main goal of the authors of the library was to ensure that their scientific experiments were correct, some of the design choices led to an characteristically unpythonic API.

#### SciConfig branches have to be explicitely declared

Is applies only if you use the attribute interface. You can implicitly declare branch using the dict interface.

```python
import scicfg

t = scicfg.SciConfig()
t.temperature = 10
t._branch('experiment1')
t.experiment1.duration = 3600.0     # attribute interface
t['experiment2.duration'] = 1800.0  # dict interface
t.experiment3.duration = 7200.0     # raises KeyError
```

#### Underscores are reserved to methods

Branches and leaves names cannot start with an underscore. Inversely, all public methods start with an underscore. This ensure a clean separation between user-defined data and instance methods.

#### Not a dict

`SciConfig` is not inherited from `dict`. It offers most of the dict methods, but is not a drop-in replacement: method are all prefixed with an underscore : (`_update()`, `_get()`, `_setdefault()`, `_items()` etc), and their behavior are designed to be consistent with the hiearchical data structure, not the `dict` interface.

#### Not a lean data structure

The datastructure is geared toward preventing and detecting misuse. That creates overhead that makes `SciConfig` ill fitted for intensive applications.

#### Values can optionally be validated when they are set

They can be validated either by their type:

```python
import numbers
t._isinstance('temperature', numbers.Real)
t.temperature = 10.0  # isinstance(10, numbers.Real) is run
t.temperature = "25"  # raises TypeError
```

Or using a custom defined function that returns `True` when check passes.

```python
def check_byte(value):
    return 0 <= value < 256

t._validate('flag', check_bytes)
t.flag = 150
t.flag = 300 # raises TypeError
```

#### Coverage and history records are kept

The numbers of time an attribute was accessed is recorded, as well as the successive values an attribute was set.

```python
t.flag = 150
t._coverage('flag') # returns 0
t._history('flag') # returns [150]
t.flag
t._coverage('flag') # returns 1
t.flag = 153
t._history('flag') # returns [150, 153]
```

This is useful to check if an attribute which should have had been accessed was indeed, or that an attribute was not set to wrong values over the course of the execution.
