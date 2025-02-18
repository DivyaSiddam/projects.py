import unittest

def getNumber(upperCaseLetter):
    """
    Converts an uppercase letter to its corresponding telephone keypad digit.
    If the character is not in A-Z, it returns the character unchanged.
    """
    letter_to_digit = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    
    if upperCaseLetter.isalpha():
        return letter_to_digit[upperCaseLetter.upper()]
    elif upperCaseLetter.isdigit() or upperCaseLetter in ['*', '#', '-']:
        return upperCaseLetter  # Keep digits and symbols unchanged
    else:
        raise ValueError(f"Invalid character: {upperCaseLetter}")


def convertPhoneWord(s):
    """
    Converts a phone-word string into its corresponding telephone number string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    result = []
    for char in s:
        converted_char = getNumber(char)
        result.append(converted_char)
    
    return "".join(result)


class TestGetNumber(unittest.TestCase):
    def test_group_ABC(self):
        for ch in "ABC":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "2")

    def test_group_DEF(self):
        for ch in "DEF":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "3")

    def test_group_GHI(self):
        for ch in "GHI":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "4")

    def test_group_JKL(self):
        for ch in "JKL":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "5")

    def test_group_MNO(self):
        for ch in "MNO":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "6")

    def test_group_PQRS(self):
        for ch in "PQRS":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "7")

    def test_group_TUV(self):
        for ch in "TUV":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "8")

    def test_group_WXYZ(self):
        for ch in "WXYZ":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "9")

    def test_non_letter_characters(self):
        for ch in ["1", "0", "#", "*", "-"]:
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), ch)

    def test_lowercase_letters(self):
        for ch in "abcdefghijklmnopqrstuvwxyz":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), getNumber(ch.upper()))


class TestConvertPhoneWord(unittest.TestCase):
    def test_standard_uppercase(self):
        self.assertEqual(convertPhoneWord("CALLNOW"), "2255669")

    def test_standard_lowercase(self):
        self.assertEqual(convertPhoneWord("callnow"), "2255669")

    def test_standard_mixed_case(self):
        self.assertEqual(convertPhoneWord("GoOdDaY"), "4663329")

    def test_1_800_FLOWERS(self):
        self.assertEqual(convertPhoneWord("1-800-FLOWERS"), "1-800-3569377")

    def test_1_800_CALLSAM(self):
        self.assertEqual(convertPhoneWord("1-800-CALLSAM"), "1-800-2255726")

    def test_standalone_symbols_and_digits(self):
        self.assertEqual(convertPhoneWord("*228"), "*228")
        self.assertEqual(convertPhoneWord("#54652"), "#54652")
        self.assertEqual(convertPhoneWord("1-989-555-5555"), "1-989-555-5555")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

