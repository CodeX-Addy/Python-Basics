from collections import namedtuple
User = namedtuple('User', ['name', 'age', 'role'])
user = User("Alice", 30, "Engineer")

print(user.age)  # 30 (Highly readable!)
