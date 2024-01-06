# class  Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def __eq__(self, other):
#         return self.radius == other.radius
#     def __gt__(self, other):
#         return self.radius > other.radius
#     def __lt__(self, other):
#         return self.radius < other.radius
#     def __le__(self, other):
#         return self.radius <= other.radius
#     def __ge__(self, other):
#         return self.radius >= other.radius
#     def __add__(self, number):
#         return Circle(self.radius + number)
#     def __iadd__(self, number):
#         self.radius += number
#         return self
#     def __sub__(self, value):
#         return Circle(self.radius - value)
#     def __isub__(self, value):
#         self.radius -= value
#         return self
#     def __str__(self):
#         return f"Радиус круга:{self.radius}"
# circle1 = Circle(5)
# circle2 = Circle(7)
#
# print(circle1 == circle2)
# print(circle1 < circle2)
# print(circle1 + 3)
# print(circle2 - 2)
# circle1 += 2
# print(circle1)



# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imag + other.imag)
#     def __sub__(self, other):
#         return Complex(self.real - other.real, self.imag - other.imag)
#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.real * other.imag + self.imag * other.real
#         return Complex(real_part, imag_part)
#     def __truediv__(self, other):
#         d = other.real ** 2 + other.imag ** 2
#         real_part = (self.real * other.real + self.imag * other.imag) / d
#         imag_part = (self.imag * other.real - self.real * other.imag) / d
#         return Complex(real_part, imag_part)
#     def __str__(self):
#         return f"{self.real} + {self.imag}j"
# complex1 = Complex(3, 2)
# complex2 = Complex(1, 5)
# result_add = complex1 + complex2
# result_sub = complex1 - complex2
# result_mul = complex1 * complex2
# result_div = complex1 / complex2
# print(result_add)
# print(result_sub)
# print(result_mul)
# print(result_div)




# class Airplane:
#     def __init__(self, model, max_passengers, current_passengers):
#         self.model = model
#         self.max_passengers = max_passengers
#         self.current_passengers = current_passengers
#     def __eq__(self, other):
#         return self.model == other.model
#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers
#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers
#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers
#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers
#     def __add__(self, passengers):
#         return self.current_passengers + passengers
#     def __iadd__(self, passengers):
#         self.current_passengers += passengers
#         return self
#     def __sub__(self, passengers):
#         return self.current_passengers - passengers
#     def __isub__(self, passengers):
#         self.current_passengers -= passengers
#         return self
#     def __str__(self):
#         return f"{self.model} - Вместимость самолета: {self.max_passengers}, Всего пассажиров: {self.current_passengers}"
# plane1 = Airplane("Boeing 747", 500, 200)
# plane2 = Airplane("Airbus A380", 550, 250)
# print(plane1 == plane2)
# print(plane1 > plane2)
# print(plane1 + 50)
# print(plane2 - 20)
# plane1 += 30
# print(plane1)




class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area
    def __ne__(self, other):
        return self.area != other.area
    def __gt__(self, other):
        return self.price > other.price
    def __lt__(self, other):
        return self.price < other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price
flat1 = Flat(80, 120000)
flat2 = Flat(90, 130000)
print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 > flat2)
print(flat1 < flat2)
print(flat1 >= flat2)
print(flat1 <= flat2)