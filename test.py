class Employee():

  raise_amt = 1.04
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  @property
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = self.pay * self.raise_amt

  def __repr__(self):
    return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

  def __str__(self):
    return '{} - {}'.format(self.fullname, self.email)

emp_1 = Employee('Tazmond', 'Merchant', 100000)

# print(emp_1)

print(help(count))