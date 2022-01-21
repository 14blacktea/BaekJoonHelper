class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['4 2 1\r\n1 1 5 2 2\r\n1 4 7 1 6\r\n', '4 2 2\r\n1 1 5 2 2\r\n1 4 7 1 6\r\n', '4 2 3\r\n1 1 5 2 2\r\n1 4 7 1 6\r\n', '7 5 3\r\n1 3 5 2 4\r\n2 3 5 2 6\r\n5 2 9 1 7\r\n6 2 1 3 5\r\n4 4 2 4 2\r\n']
    testOutput = ['8\r\n', '8\r\n', '0\r\n', '9\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


