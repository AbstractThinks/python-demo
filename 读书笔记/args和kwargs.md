```python

＃*args 用来发送一个非键值对的可变数量的参数列表给一个函数

def test(argv, *args):
    print("argv", argv)
    for arg in args:
        print("*args",arg)


test("1","2","3","4")
# 调用
>>> args = ("two", 3, 5)
>>> test(*args)

```

```python

＃*＊kwargs 用来发送一个不定长度的键值对参数给一个函数

def test(＊*kwargs):
    for key, value in kwargs.items():
        print("{0}=={1}".format(key, value))


test(name="jesse")

# 调用
kwargs = {"arg3":3, "arg2":"two"}
test(**kwargs)

```
