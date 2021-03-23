from math import sqrt

class BaseCalculator:
	'''
	Class to perform basic mathmatical operations
	'''
	def addition(self, x, y):
		'''
		This method returns sum of given two integers/floats

		Args:
			x, y(int/float) : Data given by user

		Returns:
			Addition of two values
		'''
		try:
			return x + y
		except:
			return "Unable to perform addition"

	def subtraction(self, x, y):
		'''
		This method returns subtraction of given two integers/floats

		Args:
			x, y(int/float) : Data given by user

		Returns:
			Subtraction of two values
		'''
		try:
			return x - y
		except:
			return "Unable to perform the subtraction"

	def multiplication(self, x, y):
		'''
		This method returns multiplication of given two integers/floats

		Args:
			x, y(int/float) : Data given by user

		Returns:
			Multiplication of two values
		'''
		try:
			return x * y
		except:
			return "Unable to perform the multiplication"

	def division(self, x, y):
		'''
		This method returns division of given two integers/floats

		Args:
			x, y(int/float) : Data given by user

		Returns:
			Division of two values
		'''
		try:
			return x / y
		except:
			return "Unable to perform division"


class ScintificCalculator(BaseCalculator):

	# Constant
	E = 2.718281828459045

	def __init__(self):
		'''
		Constructor which defines default Sin, Cos and Tan values
		'''
		self.sin_data = {0: 0,30: self.division(1, 2),
						 45: self.division(1, sqrt(2)),
						 60: self.division(sqrt(3), 2), 90: 1
						 }
		self.cos_data = {0: 1, 30: self.division(sqrt(3), 2),
						 45: self.division(1, sqrt(2)),
						 60: self.division(1, 2), 90: 0
						 }
		self.tan_data = {0: 0, 30: self.division(1, sqrt(3)),
						 45: 1, 60: sqrt(3), 90: "Not Defined"
						 }

	def sin(self, radian):
		'''
		This method returns the sin() of given integer/float

		Args:
			radian(int/float) : Angle given by user

		Returns:
			Sin(angel)
		'''
		try:
			if radian in self.sin_data:
				return self.sin_data.get(radian, "Not available")
			output = self.E ** (self.addition(radian, 1j))
			return output.imag
		except:
			return "Invalid input"

	def cos(self, radian):
		'''
		This method returns the cos() of given integer/float

		Args:
			radian(int/float) : Angle given by user

		Returns:
			Cos(angel)
		'''
		try:
			if radian in self.cos_data:
				return self.cos_data.get(radian, "Not available")
			output = self.E ** (self.addition(radian, 1j))
			return output.real
		except:
			return "Invalid input"

	def tan(self, radian):
		'''
		This method returns the tan() of given integer/float

		Args:
			radian(int/float) : Angle given by user

		Returns:
			Tan(angel)
		'''
		if type(radian) == int or type(radin) == float:
			if radian in self.tan_data:
				return self.tan_data.get(radian, "Not available")
			output = self.division(self.sin(radian), self.cos(radian))
			return output
		else:
			return "Invalid input"
