#!/usr/bin/env python
import unittest

from celebBot import extractWords

class CleanStringTest(unittest.TestCase):
    def testEmptyString(self):
        # TODO: This should probably actually return an empty list.
        self.assertEqual(extractWords(''), [''])

    def testLowercase(self):
        self.assertEqual(extractWords('asdf'), ['asdf'])

    def testUppercase(self):
        self.assertEqual(extractWords('ASDF'), ['asdf'])

    def testSpaces(self):
        self.assertEqual(extractWords('asdf qwer'), ['asdf', 'qwer'])
        # TODO: Remove blank strings.
        self.assertEqual(extractWords('asdf  qwer'), ['asdf', '', 'qwer'])
        # TODO: Support any spaces for separators.
        self.assertEqual(extractWords("asdf\tqwer"), ['asdfqwer'])

    def testDigits(self):
        # TODO: Remove blank strings.
        self.assertEqual(extractWords('1234'), [''])
        self.assertEqual(extractWords('as12df'), ['asdf'])

if __name__ == '__main__':
    unittest.main()
