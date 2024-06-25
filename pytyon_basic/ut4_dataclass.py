'''
在Python中，@dataclass修饰符用于简化类的定义，特别是那些主要用于存储数据的类。@dataclass是Python标准库中的一个装饰器，属于dataclasses模块。它自动生成特殊方法，
如__init__()、__repr__()、__eq__()等，从而减少了样板代码的编写。下面是@dataclass的主要功能和使用示例：

主要功能
1.自动生成__init__方法：根据类的属性自动生成构造方法。
2.自动生成__repr__方法：提供一个易读的字符串表示，便于调试。
3.自动生成__eq__方法：自动生成比较方法，允许对实例进行比较。
4.默认值和类型提示：可以使用默认值和类型提示来定义属性。
'''

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str = "Unknown"  # 默认值

# 创建实例
person1 = Person(name="Alice", age=30)
person2 = Person(name="Bob", age=25, city="New York")

# 自动生成的__repr__方法
print(person1)  # 输出: Person(name='Alice', age=30, city='Unknown')
print(person2)  # 输出: Person(name='Bob', age=25, city='New York')

# 自动生成的__eq__方法
print(person1 == person2)  # 输出: False

# 自动生成的__init__方法
print(person1.name)  # 输出: Alice
print(person2.city)  # 输出: New York

#######################################################################################
'''
更多功能
@dataclass装饰器还提供了一些高级功能和选项，例如：

可变和不可变数据类：通过设置frozen=True来创建不可变的数据类。
字段元数据：使用field函数来提供更多的字段选项，如默认工厂函数等。
'''

from dataclasses import dataclass, field

@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int
    hobbies: list = field(default_factory=list)

# 创建不可变实例
person3 = ImmutablePerson(name="Charlie", age=28)

# 尝试修改属性会引发错误
# person3.age = 29  # 将引发错误: dataclasses.FrozenInstanceError

