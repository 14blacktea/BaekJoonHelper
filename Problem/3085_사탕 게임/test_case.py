class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['3\r\nCCP\r\nCCP\r\nPPC\r\n', '4\r\nPPPP\r\nCYZY\r\nCCPY\r\nPPCC\r\n', '5\r\nYCPZY\r\nCYZZP\r\nCCPPP\r\nYCYZC\r\nCPPZZ\r\n']
    testOutput = ['3\r\n', '4\r\n', '4\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


