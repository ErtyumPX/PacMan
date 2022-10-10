"""
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
"""

a = {"A": "assfvfdb", "B": "adbnsagadşlakdşbammba", "C": "naa", "D": "mfdsbsşlfmbsl", "E": "adömadkbmaavakdnbakdlkanbkanbkanbdla"}

sorted_a_items_list = [list(a.items())[0]]
for key, value in a.items():
    match = False
    for index in range(len(sorted_a_items_list)):
        if len(value) > len(sorted_a_items_list[index][1]): sorted_a_items_list.insert(index, (key, value)); break
    if not match: sorted_a_items_list.insert(-1, (key, value))
sorted_a = {key: value for key, value in sorted_a_items_list }


print(sorted_a) 
sorted_a_by_sorted = {key: value for key, value in sorted(a.items(), reverse=True, key=lambda item: len(item[1]))}
print(sorted_a_by_sorted) 
