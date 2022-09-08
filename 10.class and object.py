class Parrot:
    species = "bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


blaa = Parrot("blaa", 10)
boom = Parrot("boom", 15)


print("blaa is a {}".format(blaa.__class__.species))

print("boom is also a {}".format(boom.__class__.species))



print("{} is {} years old".format( blaa.name, blaa.age))
print("{} is {} years old".format( boom.name, boom.age))
