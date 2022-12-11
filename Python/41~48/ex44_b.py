#显式覆盖
class Parent(object):

    def implicit(self):
        print("PARENT override()")

class Child(Parent):
    def implicit(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
