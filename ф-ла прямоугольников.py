def rectangular(f, a, b, n):
	"""
	Вычисляет приближенное значение интеграла с помощью формулы прямоугольников
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
	h = float(b - a)/n
	result = f(a+0.5*h)
	for i in range(1, n):
		result += f(a + 0.5*h + i*h)
	result *= h
	return result