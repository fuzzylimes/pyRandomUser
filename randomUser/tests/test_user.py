from unittest import TestCase

from randomUser.user import *

class TestPositiveCases(TestCase):
    def test_1_result(self):
        get_user()
        self.assertTrue(True)

    def test_5_results(self):
        res = get_user(results=5)
        self.assertEqual(len(res), 5)

    def test_gender(self):
        res = get_user(gender="female")
        self.assertTrue(res[0]['gender'] == "female")
    
    def test_pass_charset(self):
        res = get_user(pass_charset="special", pass_length="5")
        res = get_user(pass_charset="upper", pass_length="5")
        res = get_user(pass_charset="lower", pass_length="5")
        res = get_user(pass_charset="number", pass_length="5")
        res = get_user(pass_charset="special,upper,lower,number", pass_length="30")
        self.assertTrue(res)
        
    def test_pass_length_5(self):
        res = get_user(pass_charset="number", pass_length="5")
        self.assertTrue(len(res[0]['login']['password']) == 5)

    def test_pass_length_64(self):
        res = get_user(pass_charset="upper,number", pass_length="64")
        self.assertTrue(len(res[0]['login']['password']) == 64)

    def test_seed_simple(self):
        res = get_user(seed="kappa")
        res_name = res[0]['name']['first']
        res = get_user(seed="kappa")
        res2_name = res[0]['name']['first']
        self.assertEqual(res_name, res2_name)

    def test_seed_complex(self):
        res = get_user(seed="#:Us\'&MCB%#my`Dw2gr(YhARA1{#OG")
        res_name = res[0]['name']['first']
        res = get_user(seed="#:Us\'&MCB%#my`Dw2gr(YhARA1{#OG")
        res2_name = res[0]['name']['first']
        self.assertEqual(res_name, res2_name)


class TestFailureCases(TestCase):
    def test_small_results(self):
        with self.assertRaises(resultsError):
            get_user(results=0)

    def test_large_results(self):
        with self.assertRaises(resultsError):
            get_user(results=10000)

    def test_wrong_gender(self):
        with self.assertRaises(genderError):
            get_user(gender="asdf")

    def test_no_pass_charset(self):
        with self.assertRaises(RandomUserError):
            get_user(pass_length="10")

    def test_no_pass_length(self):
        with self.assertRaises(RandomUserError):
            get_user(pass_charset="upper")

    def test_invalid_pass_charset(self):
        with self.assertRaises(passwordCharsetError):
            get_user(pass_charset="uppper", pass_length="10")

    def test_invalid_pass_length_0(self):
        with self.assertRaises(passwordLengthError):
            get_user(pass_charset="upper", pass_length="0")

    def test_invalid_pass_length_80(self):
        with self.assertRaises(passwordLengthError):
            get_user(pass_charset="upper", pass_length="80")

    def test_invalid_pass_length_a(self):
        with self.assertRaises(passwordLengthError):
            get_user(pass_charset="upper", pass_length="a")

    def test_invalid_pass_length_1a(self):
        with self.assertRaises(passwordLengthError):
            get_user(pass_charset="upper", pass_length="1-a")
