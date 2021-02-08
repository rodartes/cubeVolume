import unittest
import volume

class TestVolume(unittest.TestCase):
  def test1(self):
    self.assertEqual(volume.main("2"), 8)
  def test2(self):
    self.assertEqual(volume.main("-2"), "Error")
  def test3(self):
    self.assertEqual(volume.main("Cat"), "Error")

if __name__ == '__main__':
  unittest.main()