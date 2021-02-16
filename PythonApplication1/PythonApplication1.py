

print("Hi");
x = 1;
y = "Testing" if x>1 else "Sorry!"
print(y)

def show_all(a, b, *args, **kwargs):
    print(f"a is {a}, b is {b}")

    for arg in args:
        print(f"arg is {arg}")
    
    print(type(args))
    print(type(kwargs))
    print(type(kwargs.keys()))
    for k,v in kwargs.items():
        print(f"{k} : {v}")

show_all(1,2,hi="hi",test="man",name="Name", value="Tes!")

x = range(1,10,2);
print(list(x))

sq = list(y*2 for y in x if y > 5)
print(sq)

sq1 = list(map(lambda s: s*3,x))
print(sq1)

print(type(x))

fm = list (x for x in range(1,5))
print(fm)

fm2 = list (x for x in range(1,5) for y in range(1,x))
print(fm2)

fm3 = list (y for x in range(1,5) for y in range(1,x))
print(fm3)

for x in range(1,5):
    for y in range(1,x):
        print(x)

class Animal:
    def __init__(self,name):
        self.name = name;
    
    def walks(self):
        return f"{self.name} walks!!!";

class Cat(Animal):
    def __init__(self,name,sound):
        super().__init__(name);
        self.sound = sound;
    
    def sounds(self):
        return f"{self.name} {self.sound}!!!";

cat = Cat("Simy","meows");
print(type(cat) , cat);
print(cat.walks());
print(cat.sounds())

import bfs as b; # queue 

arr_types = ['A',12,3.14];
print(arr_types);

import dfs as d; # recursive















