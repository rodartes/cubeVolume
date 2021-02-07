import unittest
import volume

class TestVolume(unittest.TestCase):
  def test_cube(self):
    self.assertEqual(volume.volumeCube(2), 8)
    self.assertEqual(volume.volumeCube(0), 0)
    self.assertEqual(volume.volumeCube(1), 1)

if __name__ == '__main__':
  unittest.main()