def say_hi(name: str, age: int) -> str:
    print("Hi. My name is {} and I'm {} years old".format(name, age))


say_hi('Alex', 32)
say_hi('Frank', 68)

"""
say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
"""