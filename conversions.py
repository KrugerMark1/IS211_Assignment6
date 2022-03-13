import unittest

class ConversionNotPossibleException(Exception):
	def __init__(self, message):
		super().__init__(message)

def convert(fromUnit, toUnit, value):
	temperatures = set(['Kelvin', 'Celsius', 'Fahrenheit'])
	distances = set(['Miles', 'Yards', 'Meters'])

	newValue = 0

	is_temperature = False

	if fromUnit in distances and toUnit in distances:
		if toUnit == 'Miles':
			if fromUnit == 'Yards':
				newValue = value / 1760
			elif fromUnit == 'Meters':
				newValue = value * 0.00062137
			else:
				newValue = value
		elif toUnit == 'Yards':
			if fromUnit == 'Meters':
				newValue = value * 1.09361
			elif fromUnit == 'Miles':
				newValue = value * 1760
			else:
				newValue = value
		else:
			if fromUnit == 'Miles':
				newValue = value * 1609.344
			elif fromUnit == 'Yards':
				newValue = value * 0.9144
			else:
				newValue = value

	elif fromUnit in temperatures and toUnit in temperatures:
		is_temperature = True

		if toUnit == 'Kelvin':
			if fromUnit == 'Celsius':
				newValue = value + 273.15
			elif fromUnit == 'Fahrenheit':
				newValue = (value + 459.67) * 5/9
			else:
				newValue = value
		elif toUnit == 'Celsius':
			if fromUnit == 'Kelvin':
				newValue = value - 273.15
			elif fromUnit == 'Fahrenheit':
				newValue = (value - 32) * 5/9
			else:
				newValue = value
		else:
			if fromUnit == 'Celsius':
				newValue = (value * 9/5) + 32
			elif fromUnit == 'Kelvin':
				newValue = (value * 9/5) - 459.67
			else:
				newValue = value
	else:
		raise ConversionNotPossibleException('Conversion Not Possible.')

	return round(newValue, 2) if is_temperature else round(newValue, 5)

class TestConversionMethods(unittest.TestCase):

	def test_distances(self):
		print("Checking Miles to Yards for 1 input, expecting 1760...")
		self.assertEqual(convert('Miles', 'Yards', 1), 1760)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 26752...")
		self.assertEqual(convert('Miles', 'Yards', 15.2), 26752)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 160160...")
		self.assertEqual(convert('Miles', 'Yards', 91), 160160)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting 40480...")
		self.assertEqual(convert('Miles', 'Yards', 23), 40480)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 20944...")
		self.assertEqual(convert('Miles', 'Yards', 11.9), 20944)
		print("Passed.")

		print("Checking Miles to Yards for 1 input, expecting 1609.344...")
		self.assertEqual(convert('Miles', 'Meters', 1), 1609.344)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 24462.0288...")
		self.assertEqual(convert('Miles', 'Meters', 15.2), 24462.0288)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 146450.304...")
		self.assertEqual(convert('Miles', 'Meters', 91), 146450.304)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting 37014.912...")
		self.assertEqual(convert('Miles', 'Meters', 23), 37014.912)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 19151.1936...")
		self.assertEqual(convert('Miles', 'Meters', 11.9), 19151.1936)
		print("Passed.")

		print("Checking Miles to Yards for 1 input, expecting 1...")
		self.assertEqual(convert('Miles', 'Miles', 1), 1)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 15.2...")
		self.assertEqual(convert('Miles', 'Miles', 15.2), 15.2)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 91...")
		self.assertEqual(convert('Miles', 'Miles', 91), 91)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting 23...")
		self.assertEqual(convert('Miles', 'Miles', 23), 23)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 11.9...")
		self.assertEqual(convert('Miles', 'Miles', 11.9), 11.9)
		print("Passed.")

		print("Checking Miles to Yards for 1 input, expecting 0.00057...")
		self.assertEqual(convert('Yards', 'Miles', 1), 0.00057)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 0.00864...")
		self.assertEqual(convert('Yards', 'Miles', 15.2), 0.00864)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 0.05170...")
		self.assertEqual(convert('Yards', 'Miles', 91), 0.05170)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting .01307...")
		self.assertEqual(convert('Yards', 'Miles', 23), 0.01307)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 0.00676...")
		self.assertEqual(convert('Yards', 'Miles', 11.9), 0.00676)
		print("Passed.")

		print("Checking Miles to Yards for 1 input, expecting 0.9144...")
		self.assertEqual(convert('Yards', 'Meters', 1), 0.9144)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 13.89888...")
		self.assertEqual(convert('Yards', 'Meters', 15.2), 13.89888)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 83.2104...")
		self.assertEqual(convert('Yards', 'Meters', 91), 83.2104)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting 21.0312...")
		self.assertEqual(convert('Yards', 'Meters', 23), 21.0312)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 10.88136...")
		self.assertEqual(convert('Yards', 'Meters', 11.9), 10.88136)
		print("Passed.")

		print("Checking Miles to Yards for 1 input, expecting 1...")
		self.assertEqual(convert('Yards', 'Yards', 1), 1)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 15.2...")
		self.assertEqual(convert('Yards', 'Yards', 15.2), 15.2)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 91...")
		self.assertEqual(convert('Yards', 'Yards', 91), 91)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting 23...")
		self.assertEqual(convert('Yards', 'Yards', 23), 23)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 11.9...")
		self.assertEqual(convert('Yards', 'Yards', 11.9), 11.9)
		print("Passed.")

		print("Checking Miles to Yards for 1 input, expecting 0.00062...")
		self.assertEqual(convert('Meters', 'Miles', 1), 0.00062)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 0.00944...")
		self.assertEqual(convert('Meters', 'Miles', 15.2), 0.00944)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 0.05654...")
		self.assertEqual(convert('Meters', 'Miles', 91), 0.05654)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting 0.01429...")
		self.assertEqual(convert('Meters', 'Miles', 23), 0.01429)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 0.00739...")
		self.assertEqual(convert('Meters', 'Miles', 11.9), 0.00739)
		print("Passed.")

		print("Checking Miles to Yards for 1 input, expecting 1.09361...")
		self.assertEqual(convert('Meters', 'Yards', 1), 1.09361)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 16.62287...")
		self.assertEqual(convert('Meters', 'Yards', 15.2), 16.62287)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 99.51851...")
		self.assertEqual(convert('Meters', 'Yards', 91), 99.51851)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting 25.15303...")
		self.assertEqual(convert('Meters', 'Yards', 23), 25.15303)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 13.01396...")
		self.assertEqual(convert('Meters', 'Yards', 11.9), 13.01396)
		print("Passed.")

		print("Checking Miles to Yards for 1 input, expecting 1...")
		self.assertEqual(convert('Meters', 'Meters', 1), 1)
		print("Passed.")
		print("Checking Miles to Yards for 15.2 input, expecting 15.2...")
		self.assertEqual(convert('Meters', 'Meters', 15.2), 15.2)
		print("Passed.")
		print("Checking Miles to Yards for 91 input, expecting 91...")
		self.assertEqual(convert('Meters', 'Meters', 91), 91)
		print("Passed.")
		print("Checking Miles to Yards for 23 input, expecting 23...")
		self.assertEqual(convert('Meters', 'Meters', 23), 23)
		print("Passed.")
		print("Checking Miles to Yards for 11.9 input, expecting 11.9...")
		self.assertEqual(convert('Meters', 'Meters', 11.9), 11.9)
		print("Passed.")

	def test_temperatures(self):
		print("Checking C to F for 30 input, expecting 86...")
		self.assertEqual(convert('Celsius', 'Fahrenheit', 30.0), 86)
		print("Passed.")
		print("Checking C to F for 45 input, expecting 113...")
		self.assertEqual(convert('Celsius', 'Fahrenheit', 45.0), 113)
		print("Passed.")
		print("Checking C to F for 23 input, expecting 73.4...")
		self.assertEqual(convert('Celsius', 'Fahrenheit', 23.0), 73.4)
		print("Passed.")
		print("Checking C to F for 12 input, expecting 53.6...")
		self.assertEqual(convert('Celsius', 'Fahrenheit', 12.0), 53.6)
		print("Passed.")
		print("Checking C to F for 1 input, expecting 33.8...")
		self.assertEqual(convert('Celsius', 'Fahrenheit', 1.0), 33.8)
		print("Passed.")
		print("C to F tests have passed.")

		print("Checking C to K for 30 input, expecting 303.15...")
		self.assertEqual(convert('Celsius', 'Kelvin', 30.0), 303.15)
		print("Passed.")
		print("Checking C to K for 1 input, expecting 274.15...")
		self.assertEqual(convert('Celsius', 'Kelvin', 1.0), 274.15)
		print("Passed.")
		print("Checking C to K for 90 input, expecting 363.15...")
		self.assertEqual(convert('Celsius', 'Kelvin', 90.0), 363.15)
		print("Passed.")
		print("Checking C to K for -30 input, expecting 243.15...")
		self.assertEqual(convert('Celsius', 'Kelvin', -30.0), 243.15)
		print("Passed.")
		print("Checking C to K for 19 input, expecting 292.15...")
		self.assertEqual(convert('Celsius', 'Kelvin', 19.0), 292.15)
		print("Passed.")
		print("C to K tests have passed.")

		print("Checking K to F for 19 input, expecting 425.47...")
		self.assertEqual(convert('Kelvin', 'Fahrenheit', 19), -425.47)
		print("Passed.")
		print("Checking K to F for 102 input, expecting -276.07...")
		self.assertEqual(convert('Kelvin', 'Fahrenheit', 102), -276.07)
		print("Passed.")
		print("Checking K to F for 23 input, expecting -418.27...")
		self.assertEqual(convert('Kelvin', 'Fahrenheit', 23), -418.27)
		print("Passed.")
		print("Checking K to F for 2 input, expecting -456.07...")
		self.assertEqual(convert('Kelvin', 'Fahrenheit', 2), -456.07)
		print("Passed.")
		print("Checking K to F for 912 input, expecting 1181.93...")
		self.assertEqual(convert('Kelvin', 'Fahrenheit', 912), 1181.93)
		print("Passed.")

		print("Checking K to C for 303.15 input, expecting 30...")
		self.assertEqual(convert('Kelvin', 'Celsius', 303.15), 30.0)
		print("Passed.")
		print("Checking K to C for 274.15 input, expecting 1...")
		self.assertEqual(convert('Kelvin', 'Celsius', 274.15), 1.0)
		print("Passed.")
		print("Checking K to C for 363.15 input, expecting 90...")
		self.assertEqual(convert('Kelvin', 'Celsius', 363.15), 90.0)
		print("Passed.")
		print("Checking K to C for 243.15 input, expecting -30...")
		self.assertEqual(convert('Kelvin', 'Celsius', 243.15), -30)
		print("Passed.")
		print("Checking K to C for 292.15 input, expecting 19...")
		self.assertEqual(convert('Kelvin', 'Celsius', 292.15), 19.0)
		print("Passed.")
		print("K to C tests have passed.")

		print("Checking F to C for 86 input, expecting 30...")
		self.assertEqual(convert('Fahrenheit', 'Celsius', 86.0), 30.0)
		print("Passed.")
		print("Checking F to C for 113 input, expecting 45...")
		self.assertEqual(convert('Fahrenheit', 'Celsius', 113.0), 45.0)
		print("Passed.")
		print("Checking F to C for 73.4 input, expecting 23...")
		self.assertEqual(convert('Fahrenheit', 'Celsius', 73.4), 23.0)
		print("Passed.")
		print("Checking F to C for 53.6 input, expecting 12...")
		self.assertEqual(convert('Fahrenheit', 'Celsius', 53.6), 12.0)
		print("Passed.")
		print("Checking F to C for 33.8 input, expecting 1...")
		self.assertEqual(convert('Fahrenheit', 'Celsius', 33.8), 1.0)
		print("Passed.")
		print("F to C tests have passed.")

		print("Checking F to K for 425.47 input, expecting 19...")
		self.assertEqual(convert('Fahrenheit', 'Kelvin', -425.47), 19)
		print("Passed.")
		print("Checking F to K for -276.07 input, expecting 102...")
		self.assertEqual(convert('Fahrenheit', 'Kelvin', -276.07), 102)
		print("Passed.")
		print("Checking F to K for -418.27 input, expecting 23...")
		self.assertEqual(convert('Fahrenheit', 'Kelvin', -418.27), 23)
		print("Passed.")
		print("Checking F to K for -456.07 input, expecting 2...")
		self.assertEqual(convert('Fahrenheit', 'Kelvin', -456.07), 2)
		print("Passed.")
		print("Checking F to K for 1181.93 input, expecting 912...")
		self.assertEqual(convert('Fahrenheit', 'Kelvin', 1181.93), 912)
		print("Passed.")

	def test_error(self):
		with self.assertRaises(ConversionNotPossibleException):
			convert('Miles', 'Celsius', 30)


if __name__ == '__main__':
	unittest.main()