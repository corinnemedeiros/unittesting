import unittest
from examples import *

class TestExamples(unittest.TestCase):

	def test_get_winner_a(self):
		a = "John"
		b = "Sally"
		result = get_winner(a, 3, b, 2)
		self.assertEqual(result, a)

	def test_get_winner_b(self):
		a = "John"
		b = "Sally"
		result = get_winner(a, 2, b, 3)
		self.assertEqual(result, b)

	def test_get_winner_tie(self):
		a = "John"
		b = "Sally"
		result = get_winner(a, 3, b, 3)
		self.assertEqual(result, a + ' ' + b)

class TestTotal(unittest.TestCase):

	def test_calculate_total_empty(self):
		result = calculate_total([])
		self.assertEqual(result, 0)

	def test_calculate_total_not_empty(self):
		result = calculate_total([1, 2, 3, 4, 5])
		self.assertEqual(result, 15)

class TestContact(unittest.TestCase):

	def setUp(self):
		self.contact_Madhan = Contact("Madhan", "Raju")
		self.contact_Madhan.add_hobby("tennis")

	def tearDown(self):
		self.contact_Madhan = None

	def test_create_contact(self):
		corinne = Contact("Corinne", "Medeiros")
		self.assertEqual(corinne.first_name, "Corinne")
		self.assertEqual(corinne.last_name, "Medeiros")
		self.assertListEqual(corinne.hobbies, [])

	def test_add_hobby_not_in_list(self):
		self.contact_Madhan.add_hobby("reading")
		self.assertEqual(len(self.contact_Madhan.hobbies), 2)
		self.assertListEqual(self.contact_Madhan.hobbies, ["tennis", "reading"])

	def test_add_hobby_already_in_list(self):
		self.contact_Madhan.add_hobby("tennis")
		self.assertEqual(len(self.contact_Madhan.hobbies), 1)
		self.assertListEqual(self.contact_Madhan.hobbies, ["tennis"])


if __name__ == '__main__':
	unittest.main()
