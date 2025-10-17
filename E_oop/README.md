# E_oop - برنامه‌نویسی شیءگرا

این پوشه شامل 150 مسئله در مورد OOP در پایتون است.

## ساختار مسائل

### بخش اول: ساده (E0001-E0050)
**مفاهیم پایه**
- E0001-E0005: ✅ کلاس، شیء، attribute
- E0006-E0010: متدها
- E0011-E0015: Constructor و Destructor
- E0016-E0020: self و instance
- E0021-E0025: Class variables vs Instance variables
- E0026-E0030: متدهای ساده
- E0031-E0035: __str__ و __repr__
- E0036-E0040: کلاس‌های ساده کاربردی
- E0041-E0045: Getter و Setter
- E0046-E0050: Property decorator

### بخش دوم: متوسط (E0051-E0100)
**مفاهیم پیشرفته**
- E0051-E0060: وراثت (Inheritance)
- E0061-E0070: چندریختی (Polymorphism)
- E0071-E0080: Encapsulation
- E0081-E0085: Method Overriding
- E0086-E0090: super()
- E0091-E0095: Multiple Inheritance
- E0096-E0100: MRO (Method Resolution Order)

### بخش سوم: سخت (E0101-E0150)
**مفاهیم پیچیده**
- E0101-E0110: Abstract Classes
- E0111-E0120: Interface
- E0121-E0130: Magic Methods
- E0131-E0135: Operator Overloading
- E0136-E0140: Metaclasses
- E0141-E0145: Design Patterns (Singleton, Factory, etc.)
- E0146-E0150: Dataclasses و پروژه‌های کامل

## وضعیت پیاده‌سازی
- ✅ E0001-E0003: کامل شده
- ⏳ E0004-E0150: در حال تکمیل

## مثال استفاده
```python
# E0001 - کلاس ساده
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.name)
```
