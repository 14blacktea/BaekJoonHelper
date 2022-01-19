class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['5 6 2\r\n1 2 3 2 5 6\r\n3 8 7 2 1 3\r\n8 2 3 1 4 5\r\n3 4 5 1 1 1\r\n9 3 2 1 4 3\r\n3 4 2\r\n4 2 1\r\n']
    testOutput = ['12\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


