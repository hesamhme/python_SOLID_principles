'''
in open close principle code should be open for develope and close for change 
we coulden't change a code source even we change a module or a object.
'''

ice_cream_flavors = ['chocolate', 'vanilla']

class MakeIceCream:

    def __init__(self, flavor):
        self.flavor = flavor

    def make(self):
        if self.flavor in ice_cream_flavors:
            print("Great success. You now have ice cream.")
        else:
            print("Epic fail. No ice cream for you.")

'''
here in this example if we want to add a new flavor of ice cream we should directly add it to our array 
this is against the Open Close principle. To solve that problem we impelant a class to add new flavor.
'''

class AddIceCream:

    def __init__(self, flavor):
        self.flavor = flavor
        
    def add(self):
        ice_cream_flavors.append(self.flavor)


'''
now we can add new flavor without effecting on source code
'''

add_strawberry_flavor = AddIceCream('strawberry')
add_strawberry_flavor.add()

make_strawberry_icecream = MakeIceCream('strawberry')
make_strawberry_icecream.make()
