derivative <- D(expression(2 + 3*x), name='x')
print(derivative)

another_derivative <- D(expression(x^2), name='x')
print(another_derivative)