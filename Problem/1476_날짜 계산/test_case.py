class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['1 16 16\r\r\n', '1 1 1\r\r\n', '1 2 3\r\r\n', '15 28 19\r\r\n']
    testOutput = ['16\r\r\n', '1\r\r\n', '5266\r\r\n', '7980\r\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


