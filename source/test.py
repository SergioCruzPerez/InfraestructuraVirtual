#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import cancion
import db

class TestFoo(unittest.TestCase):
    def test_BPMS(self):
     r = cancion.compararBPMS("Snakes","Badman")
     self.assertTrue(r)

    def test_Key(self):
     r = cancion.compararKey("Badman","Snakes")
     self.assertTrue(r)

    def test_online(self):
     r = cancion.HayInternet()
     self.assertFalse(r)

    def test_copia(self):
     r = cancion.Copia()
     self.assertNotEqual(r,0)

unittest.main()
