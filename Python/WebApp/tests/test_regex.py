import unittest
from regex import *


class TestRegex(unittest.TestCase):

    def test_os_regex(self):
        specs1 = '''Minimum:OS:Microsoft® Windows® XP SP2 / Vista / 7Processor:Intel® Pentium 2,0 GHz/AMD 
        2000+Memory:2 GB RAMGraphics:GeForce 7300/Radeon 9200DirectX®:9.0cHard Drive:2 GB HD 
        spaceSound:DirectX® compatible'''
        specs2 = '''Minimum:OS: Windows VistaProcessor: Intel Core 2 Duo E6550Memory: 3 GB RAMGraphics: 
        nVidia GeForce 9400 1 Gb/Amd Radeon HD 4550 1 GbDirectX: Version 9.0cStorage: 9 GB available space'''
        incorrect_specs = '''Minimum Configuration: Windows XP, Pentium II 233 Mhz, 32 Mb RAM, 1200 MB hard 
        disk space, DirectX 7.1, 16-bit sound card, Video Card with 8 MB RAM'''
        none_specs = None
        self.assertEqual(5, os_regex(specs1))
        self.assertEqual(6, os_regex(specs2))
        self.assertEqual(None, os_regex(incorrect_specs))
        self.assertEqual(None, os_regex(none_specs))

    def test_mem_regex(self):
        specs1 = '''Minimum:OS:Microsoft® Windows® XP SP2 / Vista / 7Processor:Intel® Pentium 2,0 GHz/AMD 
        2000+Memory:2 GB RAMGraphics:GeForce 7300/Radeon 9200DirectX®:9.0cHard Drive:2 GB HD 
        spaceSound:DirectX® compatible'''
        specs2 = '''Minimum:OS: Windows VistaProcessor: Intel Core 2 Duo E6550Memory: 3 GB RAMGraphics: 
        nVidia GeForce 9400 1 Gb/Amd Radeon HD 4550 1 GbDirectX: Version 9.0cStorage: 9 GB available space'''
        incorrect_specs = '''Minimum Configuration: Windows XP, Pentium II 233 Mhz, 32 Mb RAM, 1200 MB hard 
        disk space, DirectX 7.1, 16-bit sound card, Video Card with 8 MB RAM'''
        specs_512 = '''Minimum:OS: Windows XPProcessor: Pentium 4 1300 MHz 1.3 GHzMemory: 512 MB RAMGraphics: 
        Geforce2 MX 400 64/128-bit SDR, 64-bit DDR or betterStorage: 500 MB available space'''
        none_specs = None
        self.assertEqual(2.0, ram_regex(specs1))
        self.assertEqual(3.0, ram_regex(specs2))
        self.assertEqual(0.5, ram_regex(specs_512))
        self.assertEqual(None, ram_regex(incorrect_specs))
        self.assertEqual(None, ram_regex(none_specs))

