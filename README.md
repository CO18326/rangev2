# rangev2



rangev2 is next version of popular range class of python, which enables you to produce lists even by using *,/,// and % operators along with +,- operators.

  - The syntax is nearly similar to the privious versions
  - Little modification is that step (third parametr) is now string containing operand and operator
  - Example : 
```sh
>>> new_range(8,100,'*9')
>>> [8,72]
```
# New Features!

  - print(new_range(begin,end,step)) will now print the entire list
  - example 
```sh
>>> print(new_range(100,1,'//3')
>>> [100, 33, 11, 3]
```
  - the default values for begin and step are 0 and '+1' respectively.
  - in operator is overloaded: 
```sh  
>>> 3 in new_range(4) 
>>> True.
```
  - the list generated can also be accessed via list argument
  - example : 
 ```sh
>>> new_range(6).list
>>> [0,1,2,3,4,5]
```

### Installation

```sh
pip install rangev2
```



License
----

MIT

Contribute
---

All ways welcome good contributions, keeping the target to make it core functionality of python




  
