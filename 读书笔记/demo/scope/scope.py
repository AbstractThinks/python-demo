name = "jesse"

def func1():
    print("func1:"+name)

def func2():
    name = "alvin"
    func1()
    print("func2:"+name)

func2()
