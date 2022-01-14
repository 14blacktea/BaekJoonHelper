class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['1 2 2\r\n1 2 1\r\n2 1 3\r\n3 3 3\r\n', '1 2 1\r\n1 2 1\r\n2 1 3\r\n3 3 3\r\n', '1 2 3\r\n1 2 1\r\n2 1 3\r\n3 3 3\r\n', '1 2 4\r\n1 2 1\r\n2 1 3\r\n3 3 3\r\n', '1 2 5\r\n1 2 1\r\n2 1 3\r\n3 3 3\r\n', '3 3 3\r\n1 1 1\r\n1 1 1\r\n1 1 1\r\n']
    testOutput = ['0\r\n', '1\r\n', '2\r\n', '52\r\n', '-1\r\n', '2\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


