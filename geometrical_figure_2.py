from geometrical_figure import Geometrical_figure, Square, Circle

rect_1 = Geometrical_figure(3, 4)
rect_2 = Geometrical_figure(12, 5)

print(rect_1.getArea())
print(rect_2.getArea())

print('\n')

square_1 = Square(5)
square_2 = Square(10)

print(square_1.getAreaSquare(), square_2.getAreaSquare())

figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.getAreaSquare())
    else:
        print(figure.getArea())

cir_1 = Circle(2)
cir_2 = Circle(4)

print(cir_1.getAreaCircle(), cir_2.getAreaCircle())

