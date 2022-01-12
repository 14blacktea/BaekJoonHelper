class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['1 1 1\r\r\n1\r\r\n1 1 1\r\r\n', '1 1 4\r\r\n1\r\r\n1 1 1\r\r\n', '5 2 1\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 1 3\r\r\n3 2 3\r\r\n', '5 2 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 1 3\r\r\n3 2 3\r\r\n', '5 2 3\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 1 3\r\r\n3 2 3\r\r\n', '5 2 4\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 1 3\r\r\n3 2 3\r\r\n', '5 2 5\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 1 3\r\r\n3 2 3\r\r\n', '5 2 6\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 3 2 3 2\r\r\n2 1 3\r\r\n3 2 3\r\r\n']
    testOutput = ['1\r\r\n', '0\r\r\n', '2\r\r\n', '15\r\r\n', '13\r\r\n', '13\r\r\n', '13\r\r\n', '85\r\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


