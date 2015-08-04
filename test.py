#!/usr/bin/env python
import unittest

from celebBot import extractWords

class CleanStringTest(unittest.TestCase):
    def testEmptyString(self):
        self.assertEqual(extractWords(''), [])

    def testLowercase(self):
        self.assertEqual(extractWords('asdf'), ['asdf'])

    def testUppercase(self):
        self.assertEqual(extractWords('ASDF'), ['asdf'])

    def testSpaces(self):
        self.assertEqual(extractWords('asdf qwer'), ['asdf', 'qwer'])
        self.assertEqual(extractWords('asdf  qwer'), ['asdf', 'qwer'])
        self.assertEqual(extractWords("asdf\tqwer"), ['asdf', 'qwer'])

    def testDigits(self):
        self.assertEqual(extractWords('1234'), [])
        self.assertEqual(extractWords('as12df'), ['asdf'])

if __name__ == '__main__':
    unittest.main()
