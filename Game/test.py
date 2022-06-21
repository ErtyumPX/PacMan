class Test:
    def __init__ (self, name):
        self.name = name
    def __del__ (self):
        print(self.name)

x = Test("x")

while True:
    y = Test("y")
    break

if True:
    z = Test("z")

def test_func(i=0) -> None:
    t = Test(f"t{i}")
    if i<3:
        test_func(i+1)
test_func()

print("End")
