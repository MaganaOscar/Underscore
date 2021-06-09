class Underscore:
    def map(self, iterable, callback):
        mapped = []
        for item in iterable:
            change = [callback(item)]
            mapped += change
        return mapped
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
    def filter(self, iterable, callback):
        filtered = []
        for item in iterable:
            if callback(item):
                check = [item]
                filtered += check
        return filtered
    def reject(self, iterable, callback):
        filtered = []
        for item in iterable:
            if not callback(item):
                check = [item]
                filtered += check
        return filtered
# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print(_.map([1,2,3], lambda x: x*3))
print(_.find([1,2,3,4,5,6], lambda x: x>3))
print(evens)
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0))
