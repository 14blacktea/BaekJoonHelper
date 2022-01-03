class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['4 5 1\r\r\n1 2\r\r\n1 3\r\r\n1 4\r\r\n2 4\r\r\n3 4\r\r\n', '5 5 3\r\r\n5 4\r\r\n5 2\r\r\n1 2\r\r\n3 4\r\r\n3 1\r\r\n', '1000 1 1000\r\r\n999 1000\r\r\n']
    testOutput = ['1 2 4 3\r\r\n1 2 3 4\r\r\n', '3 1 2 5 4\r\r\n3 1 4 2 5\r\r\n', '1000 999\r\r\n1000 999\r\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


