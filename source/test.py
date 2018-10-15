#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from cancion import canciones

class TestFoo(unittest.TestCase):
    def test_cargar_cancion(self):
        song = canciones("Snakes")
        assert isinstance(song, canciones), "No se ha podido cargar la canción deseada"

    def test_BPMS(self):
        song = canciones("Snakes")
        assert song.compararBPMS("Badman")==True, "La mezcla no sonaría bien"

    def test_Key(self):
        song = canciones("Badman")
        assert song.compararKey("Snakes")==True, "La mezcla no sonaría bien"

    def test_online(self):
        song = canciones("Snakes")
        assert song.HayInternet()==False, "No existe conexión a Internet"

unittest.main()
