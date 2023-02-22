nbdev-hello-world
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This file will become your README and also the index of your
documentation.

## Install

``` sh
pip install nbdev_hello_world
```

## How to use

This file contains all the testcases of Functions written in
testing.ipynb .

## TestCases

``` python
class TestName(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,3),4)
        
    def test_subtract(self):
        self.assertEqual(subtract(1,3),-2)
        
    def test_multiply(self):
        self.assertEqual(multiply(1,3),3)
        
    def test_divide(self):
        self.assertEqual(divide(1,3),0.33)
```

    test_add (__main__.TestName) ... ok
    test_divide (__main__.TestName) ... ok
    test_multiply (__main__.TestName) ... ok
    test_subtract (__main__.TestName) ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.010s

    OK

### Testing using Fastcore

``` python
class TestName(unittest.TestCase):
    def test_add(self):
        assert add(1,3)== 4
        
    def test_subtract(self):
        assert subtract(1,3)== 4
        
    def test_multiply(self):
        test_eq(multiply(1,3), 3)
        
    def test_divide(self):
        test_eq(divide(1,3), 0.33)
```

    test_add (__main__.TestName) ... ok
    test_divide (__main__.TestName) ... ok
    test_multiply (__main__.TestName) ... ok
    test_subtract (__main__.TestName) ... FAIL

    ======================================================================
    FAIL: test_subtract (__main__.TestName)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "C:\Users\5115\AppData\Local\Temp\ipykernel_22516\4123861692.py", line 7, in test_subtract
        assert subtract(1,3)== 4
    AssertionError

    ----------------------------------------------------------------------
    Ran 4 tests in 0.013s

    FAILED (failures=1)

### Testing using pytest

``` python
def test_add():
    assert add(1,3) == 4
    
def test_subtract():
    assert subtract(1,3) == 2
    
def test_multiply():
    assert multiply(1,3) == 3
    
def test_divide():
    assert divide(1,3) == 0.33
```

    .F..                                                                                         [100%]
    ============================================ FAILURES =============================================
    __________________________________________ test_subtract __________________________________________

        def test_subtract():
    >       assert subtract(1,3) == 2
    E       assert -2 == 2
    E        +  where -2 = subtract(1, 3)

    C:\Users\5115\AppData\Local\Temp\ipykernel_22516\2678314103.py:5: AssertionError
    ===================================== short test summary info =====================================
    FAILED t_dcfcb849b5634211b31c8d80c2082597.py::test_subtract - assert -2 == 2
    1 failed, 3 passed in 0.53s
