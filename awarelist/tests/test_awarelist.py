# -*- coding: utf-8 -*-
from __future__ import absolute_import

import unittest
import awarelist

class TestAwareList(unittest.TestCase):
	def test_logic(self):
		aw_list = awarelist.AwareList(["InitialA", "InitialB"])
		self.assertEqual(aw_list.added, [])
		self.assertEqual(aw_list.removed, [])

		aw_list.append('MyFirstAppend')
		aw_list.insert(0, 'MyFirstInsert')

		self.assertEqual(aw_list, ["MyFirstInsert", "InitialA", "InitialB", "MyFirstAppend"])
		self.assertEqual(aw_list.added, ["MyFirstAppend", "MyFirstInsert"])
		self.assertEqual(aw_list.removed, [])

		aw_list.extend(["ExtendA", "ExtendB"])
		self.assertEqual(aw_list, ["MyFirstInsert", "InitialA", "InitialB", "MyFirstAppend", "ExtendA", "ExtendB"])
		self.assertEqual(aw_list.added, ["MyFirstAppend", "MyFirstInsert", "ExtendA", "ExtendB"])
		self.assertEqual(aw_list.removed, [])

		aw_list.remove('ExtendA')
		self.assertEqual(aw_list, ["MyFirstInsert", "InitialA", "InitialB", "MyFirstAppend", "ExtendB"])
		aw_list.pop()
		self.assertEqual(aw_list, ["MyFirstInsert", "InitialA", "InitialB", "MyFirstAppend"])
		self.assertEqual(aw_list.added, ["MyFirstAppend", "MyFirstInsert"])
		self.assertEqual(aw_list.removed, [])

		aw_list.remove('InitialA')
		self.assertEqual(aw_list.added, ["MyFirstAppend", "MyFirstInsert"])
		self.assertEqual(aw_list.removed, ['InitialA'])

		aw_list.append('InitialB')
		self.assertEqual(aw_list.added, ["MyFirstAppend", "MyFirstInsert", "InitialB"])

	def test_magic(self):
		aw_list = awarelist.AwareList(['A', 'B', 'C'])
		self.assertEqual(aw_list.added, [])
		self.assertEqual(aw_list.removed, [])

		aw_list.append('new')
		self.assertEqual(aw_list.added, ['new'])
		self.assertEqual(aw_list.removed, [])
		self.assertEqual(aw_list, ['A','B','C','new'])

		del aw_list[:]
		self.assertEqual(aw_list, [])
		self.assertEqual(aw_list.added, [])
		self.assertEqual(aw_list.removed, ['A','B','C'])
		
if __name__ == '__main__':
	unittest.main()