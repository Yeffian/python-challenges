# class A:
#     def f(self):
#         return self.g()

#     def g(self):
#         return 'A'

# class B(A):
#     def g(self):
#         return 'B'

# a = A()
# b = B()
# print(a.f(), b.f())
# print(a.g(), b.g())
# ans:
# A, B
# A, B

# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")
# ans:
# a, c, d
# except isnt called since there is no error

# try:
#     print("a")
#     raise Exception("doom")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")
# ans:
# a, b, d
# no else called since there is an exception

# def f():
#     try:
#         print("a")
#         return
#     except:
#         print("b")
#     else:
#         print("c")
#     finally:
#         print("d")

# f()
# ans:
# a, d
# try, suceed, then go to the finally