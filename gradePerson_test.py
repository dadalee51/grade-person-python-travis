import unittest
from gradePerson import GradePerson
class TestGradePerson(unittest.TestCase):

	def setUp(self):
		self.gp = GradePerson()

	def tearDown(self):
		pass

	def test_compareOrder_eq(self):
		self.assertEqual(self.gp.compOrd(["ABC","DEF",100], ["ABC","DEF",100]), 0)
		self.assertEqual(self.gp.compOrd(["XYZ","DEF",5], ["XYZ","DEF",5]), 0)
		self.assertEqual(self.gp.compOrd(["ABC","MNO",5], ["ABC","MNO",5]), 0)

	def test_compareOrder_lt(self):
		self.assertEqual(self.gp.compOrd(["ABC","DEF",100], ["ABC","DEF",88]), -1)
		self.assertEqual(self.gp.compOrd(["ABC","DEF",100], ["ABC","XYZ",100]), -1)
		self.assertEqual(self.gp.compOrd(["ABC","XYZ",100], ["BCD","XYZ",100]), -1)

	def test_compareOrder_gt(self):
		self.assertEqual(self.gp.compOrd(["ABC","DEF",88], ["ABC","DEF",100]), 1)
		self.assertEqual(self.gp.compOrd(["XYZ","DEF",100], ["ABC","DEF",100]), 1)
		self.assertEqual(self.gp.compOrd(["ABC","DEF",100], ["ABC","AAA",100]), 1)

if __name__ == '__main__':
	unittest.main()