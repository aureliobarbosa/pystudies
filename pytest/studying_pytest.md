# Studying Pytest
## Pytest 

*Resources:* 

- [Real Python](https://realpython.com/pytest-python-testing/). Accessed 2022-11-03.
- [pytest 7.2 documentation](https://docs.pytest.org/en/7.1.x/contents.html#). Accessed 2022-11-08

## Why pytest?

- 2022-10 Python Brasil: I realize it was time to learn a testing framework and start using it with my python scripts and code.
- I took a look into the the most important testing frameworks and found that unittest and pytest were the most used by the time of this note (there is a framework called Robot, for automate testing, but its scope is wider than testing). Besides that I am currently interested in learning a little bit more about numpy (the numerical library for python) and it uses pytest on its current stable version (numpy 1.23).
- I jumped in.

## Basic Usage (with example from others)

pytest automatically run files named as `test_*.py*` and `*_test.py` in the current directory tree, and you just need to call `pytest` from the terminal that it runs.

To describe the basic usage I am going through examples from above resources with minimal modifications. Let's con

```python
# content of square.py
from locale import atof

def square(x):
    return x**2

def main():
        
    input_txt = input('Type a number (any letter to escape): ')
    try:
        number = atof(input_txt)
    except:
        print('Exiting')

    number_squared = number*number
    print(f'The square of {number:.2f} is {number_squared:.2f}')
    
if __name__ == '__main__':
   main() ```
```


## Learning

- Fast script for doing something, with testing.

### Taylor expansion for the square root

### Math - simple calculator


### Text - Anagrams

## Real World Project examples

### Numpy Examples