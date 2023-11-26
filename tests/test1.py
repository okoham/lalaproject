# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest

from lala.amodule import add
from lala.bmodule import myarray


class TestSimple(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_aray_length(self):
        self.assertEqual(len(myarray(3)), 4)


if __name__ == '__main__':
    unittest.main()