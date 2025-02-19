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
        return None  # Return None for invalid characters


def convertPhoneWord(s):
    """
    Converts a phone-word string into its corresponding telephone number string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")

    result = []
    for char in s:
        converted_char = getNumber(char)
        if converted_char is None:
            raise ValueError(f"Invalid character in input: {char}")
        result.append(converted_char)

    return "".join(result)


class TestGetNumber(unittest.TestCase):
    def test_group_ABC(self):
        for ch in "ABC":
            self.assertEqual(getNumber(ch), "2")

    def test_group_DEF(self):
        for ch in "DEF":
            self.assertEqual(getNumber(ch), "3")

    def test_group_GHI(self):
        for ch in "GHI":
            self.assertEqual(getNumber(ch), "4")

    def test_group_JKL(self):
        for ch in "JKL":
            self.assertEqual(getNumber(ch), "5")

    def test_group_MNO(self):
        for ch in "MNO":
            self.assertEqual(getNumber(ch), "6")

    def test_group_PQRS(self):
        for ch in "PQRS":
            self.assertEqual(getNumber(ch), "7")

    def test_group_TUV(self):
        for ch in "TUV":
            self.assertEqual(getNumber(ch), "8")

    def test_group_WXYZ(self):
        for ch in "WXYZ":
            self.assertEqual(getNumber(ch), "9")

    def test_non_letter_characters(self):
        for ch in ["1", "0", "#", "*", "-"]:
            self.assertEqual(getNumber(ch), ch)

    def test_lowercase_letters(self):
        for ch in "abcdefghijklmnopqrstuvwxyz":
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

    def test_only_letters(self):
        self.assertEqual(convertPhoneWord("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "22233344455566677778889999")

    def test_invalid_characters(self):
        invalid_inputs = ["HELLO WORLD", "TEST!", "A@B", "123_456", "CALL,ME"]
        for inp in invalid_inputs:
            with self.assertRaises(ValueError):
                convertPhoneWord(inp)

    def test_empty_string(self):
        self.assertEqual(convertPhoneWord(""), "")

    def test_single_letter(self):
        self.assertEqual(convertPhoneWord("A"), "2")

    def test_single_digit(self):
        self.assertEqual(convertPhoneWord("5"), "5")

    def test_single_symbol(self):
        self.assertEqual(convertPhoneWord("*"), "*")
        self.assertEqual(convertPhoneWord("#"), "#")
        self.assertEqual(convertPhoneWord("-"), "-")

    def test_repeated_letters(self):
        self.assertEqual(convertPhoneWord("AAA"), "222")

    def test_only_digits(self):
        self.assertEqual(convertPhoneWord("1234567890"), "1234567890")

    def test_only_symbols(self):
        self.assertEqual(convertPhoneWord("*-#-*-#"), "*-#-*-#")

    def test_edge_dashes(self):
        self.assertEqual(convertPhoneWord("-CALL-"), "-2255-")

    def test_complex_mix(self):
        self.assertEqual(convertPhoneWord("1-800-GETCASH"), "1-800-4382274")

    def test_long_string(self):
        input_str = "CALLNOW" * 10
        expected_length = len("2255669" * 10)
        self.assertEqual(len(convertPhoneWord(input_str)), expected_length)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
