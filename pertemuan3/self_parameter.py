#	Gunakan `self` untuk mengakses properti kelas
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

#	Gunakan kata-kata this dan gweh sebagai pengganti self:
class Person:
  def __init__(this, name, age):
    this.name = name
    this.age = age

  def greet(gweh):
    print("Hello, my name is " + gweh.name)

p1 = Person("Emil", 36)
p1.greet()
