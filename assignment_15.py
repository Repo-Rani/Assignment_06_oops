# 15. Method Resolution Order (MRO) and Diamond Inheritance

class A:
  def show(self):
    print("A")

class B(A):
  def show(self):
    print("B")

class C(A):
  def show(self):
    print("C")
  
class D(B, C):
  pass

d1 = D()
d1.show()

print(D.mro())