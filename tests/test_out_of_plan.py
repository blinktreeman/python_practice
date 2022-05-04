from unittest import TestCase
import part_05.out_of_plan as oop_05


class Part05Test(TestCase):
    def test_base64_to_decimal(self):
        self.assertEqual(oop_05.base64_to_decimal('BA'), 64, 'Should be 64')
        self.assertEqual(oop_05.base64_to_decimal('BB'), 65, 'Should be 65')
        self.assertEqual(oop_05.base64_to_decimal('BC'), 66, 'Should be 66')

    def test_high(self):
        self.assertEqual(oop_05.high('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(oop_05.high('what time are we climbing up the volcano'), 'volcano')
        self.assertEqual(oop_05.high('take me to semynak'), 'semynak')
        self.assertEqual(oop_05.high('aa b'), 'aa')
        self.assertEqual(oop_05.high('b aa'), 'b')
        self.assertEqual(oop_05.high('bb d'), 'bb')
        self.assertEqual(oop_05.high('d bb'), 'd')
        self.assertEqual(oop_05.high("aaa b"), "aaa")

    def test_dec_2_fact_string(self):
        self.assertEqual(oop_05.dec_2_fact_string(463), "341010")
        self.assertEqual(oop_05.dec_2_fact_string(2982), "4041000")

    def test_fact_string_2_dec(self):
        self.assertEqual(oop_05.fact_string_2_dec("341010"), 463)
        self.assertEqual(oop_05.fact_string_2_dec("4042100"), 2990)

    def test_make_readable(self):
        self.assertEqual(oop_05.make_readable(0), "00:00:00")
        self.assertEqual(oop_05.make_readable(60), "00:01:00")
        self.assertEqual(oop_05.make_readable(86399), "23:59:59")
        self.assertEqual(oop_05.make_readable(359999), "99:59:59")
