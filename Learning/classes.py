class MyClass():
    def method1(self):
        print("MyClass method1")

    def method2(self, someString):
        print("MyClass method2", someString)

class AnotherClass():
    def method1(self):
        MyClass.method1(self)
        print("Another method1")

    def method2(self, someString):
        print("Another method2")

def main():
    c = MyClass()
    c.method1()
    c.method2("Hello There")

    c1 = AnotherClass()
    c1.method1()
    c1.method2("General Kenobi")



if __name__ == "__main__":
    main()
