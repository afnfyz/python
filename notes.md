## Using timeit module

The `timeit` module in Python provides a simple way to time small bits of Python code. The module provides a `timeit()` function which takes a statement to be timed as input and runs it for a specified number of loops. Here are the basic steps to use the `timeit` module:

1. Import the `timeit` module:

```python
import timeit
```

2. Define the statement you want to time as a string:

```python
mycode = 'print("hello world")'
```

3. Use the `timeit()` function to time the statement. Here's an example that runs the statement 1000 times:

```python
timeit.timeit(mycode, number=1000)
```

This will output the time taken to execute the statement 1000 times in seconds.

You can also use the `timeit` module to time functions. Here's an example:

```python
def myfunc():
    return "hello world"
    
timeit.timeit(myfunc, number=1000)
```

This will output the time taken to call `myfunc()` 1000 times in seconds.