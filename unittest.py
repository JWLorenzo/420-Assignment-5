import unittest
def FirstIsntChar(text):
  sChars = '"!@#$%^&*()-+?_=,<>/'
  if(not text[0] in sChars):
    return "1"
  else:
    return "0"
def FirstIsntDigit(text):
  if(not text[0].isdigit()):
    return "1"
  else:
    return "0"
def ContainsChar(text):
  sChars = '"!@#$%^&*()-+?_=,<>/'
  if(any(c in sChars for c in text)):
    return "1"
  else:
    return "0"
def ContainsLetter(text):
  if(any(c.isalpha() for c in text)):
    return "1"
  else:
    return "0"
def ContainsDigit(text):
  if(any(c.isdigit() for c in text)):
    return "1"
  else:
    return "0"
def CheckLength16(text):
  if(len(text) == 16):
    return "1"
  else:
    return "0"
def VerifyPassword(text):
 x = ""
 x += CheckLength16(text)
 x += ContainsDigit(text)
 x += ContainsLetter(text)
 x += ContainsChar(text)
 x += FirstIsntDigit(text)
 x += FirstIsntChar(text)
 return x
def OnlyNumCheck(text):
  if(all(c.isdigit() for c in text)):
    return "1"
  else:
    return "0"
def VerifyCredit(text):
 x = ""
 x += CheckLength16(text)
 x += OnlyNumCheck(text)

 return x
class TestValidity(unittest.TestCase):
  def test_FirstIsntChar(self):
    self.assertEqual(FirstIsntChar("abcdef7@ijklmnop"),"1")
#################################################################
  def test_FirstIsntDigit(self):
    self.assertEqual(FirstIsntDigit("abcdef7@ijklmnop"),"1")
#################################################################
  def test_ContainsChar(self):
    self.assertEqual(ContainsChar("abcdef7@ijklmnop"),"1")
#################################################################
  def test_ContainsLetter(self):
    self.assertEqual(ContainsLetter("abcdef7@ijklmnop"),"1")
#################################################################
  def test_ContainsDigit(self):
    self.assertEqual(ContainsDigit("abcdef7@ijklmnop"),"1")
#################################################################
  def test_CheckLength16(self):
    self.assertEqual(CheckLength16("abcdef7@ijklmnop"),"1")
#################################################################
  def test_OnlyNumCheck(self):
    self.assertEqual(OnlyNumCheck("1234567891234567"),"1")
#################################################################
  def test_VerifyPassword(self):
    self.assertEqual(VerifyPassword("abcdef7@ijklmnop"),"111111")
#################################################################
  def test_VerifyCredit(self):
    self.assertEqual(VerifyCredit("1234567891234567"),"11")
#################################################################
if __name__ == "__main__":
    unittest.main()
