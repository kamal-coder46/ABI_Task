import unittest

from task_abi import ScintificCalculator



class AbiTests(unittest.TestCase):

	def setUp(self):
		self.sci_obj = ScintificCalculator()

	def test_addition(self):
		self.assertEqual(self.sci_obj.addition(10, 20), 30, "Failed")

	def test_addition_with_float(self):
		self.assertEqual(self.sci_obj.addition(10.5, 15.5), 26.0, "Failed")

	def test_addition_with_invalid_inputs(self):
		self.assertEqual(self.sci_obj.addition('10.5', '15.5'), "10.515.5", "Failed")

	def test_subtraction(self):
		self.assertEqual(self.sci_obj.subtraction(20, 10), 10, "Failed")

	def test_subtraction_with_float(self):
		self.assertEqual(self.sci_obj.subtraction(15.5, 10.5), 5.0, "Failed")

	def test_subtraction_with_invalid_inputs(self):
		self.assertEqual(self.sci_obj.subtraction('10.5', '15.5'), "Unable to perform the subtraction", "Failed")

	def test_multiplication(self):
		self.assertEqual(self.sci_obj.multiplication(20, 10), 200, "Failed")

	def test_multiplication_with_float(self):
		self.assertEqual(self.sci_obj.multiplication(15.5, 10.5), 162.75, "Failed")

	def test_multiplication_with_invalid_inputs(self):
		self.assertEqual(self.sci_obj.multiplication('10.5', '15.5'), "Unable to perform the multiplication", "Failed")

	def test_division(self):
		self.assertEqual(self.sci_obj.division(20, 10), 2.0, "Failed")

	def test_division_with_float(self):
		self.assertEqual(self.sci_obj.division(15.5, 10.5), 1.4761904761904763, "Failed")

	def test_division_with_invalid_inputs(self):
		self.assertEqual(self.sci_obj.division('10.5', '15.5'), "Unable to perform division", "Failed")

	def test_sin(self):
		self.assertEqual(self.sci_obj.sin(0), 0, "Failed")

	def test_sin_with_70(self):
		self.assertEqual(self.sci_obj.sin(70), 2.1166686556422098e+30, "Failed")

	def test_sin_with_string(self):
		self.assertEqual(self.sci_obj.sin("Hi"), "Invalid input", "Failed")

	def test_cos(self):
		self.assertEqual(self.sci_obj.cos(0), 1, "Failed")

	def test_cos_with_70(self):
		self.assertEqual(self.sci_obj.cos(70), 1.3590973141675095e+30, "Failed")

	def test_cos_with_string(self):
		self.assertEqual(self.sci_obj.cos("Hi"), "Invalid input", "Failed")

	def test_tan(self):
		self.assertEqual(self.sci_obj.tan(0), 0, "Failed")

	def test_tan_with_60(self):
		self.assertEqual(self.sci_obj.tan(60), 1.7320508075688772, "Failed")

if __name__ == '__main__':
	unittest.main()
