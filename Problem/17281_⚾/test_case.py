class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['2\r\n4 0 0 0 0 0 0 0 0\r\n4 0 0 0 0 0 0 0 0\r\n', '2\r\n4 0 0 0 1 1 1 0 0\r\n0 0 0 0 0 0 0 0 0\r\n', '2\r\n0 4 4 4 4 4 4 4 4\r\n0 4 4 4 4 4 4 4 4\r\n', '2\r\n4 3 2 1 0 4 3 2 1\r\n1 2 3 4 1 2 3 4 0\r\n', '9\r\n4 4 4 4 4 4 4 4 0\r\n4 4 4 4 4 4 4 4 0\r\n4 4 4 4 4 4 4 4 0\r\n4 4 4 4 4 4 4 4 0\r\n4 4 4 4 4 4 4 4 0\r\n4 4 4 4 4 4 4 4 0\r\n4 4 4 4 4 4 4 4 0\r\n4 4 4 4 4 4 4 4 0\r\n4 4 4 4 4 4 4 4 0\r\n', '9\r\n1 2 4 3 0 2 1 0 3\r\n1 2 1 2 0 0 0 0 1\r\n3 4 2 3 1 2 3 4 0\r\n0 1 2 3 4 2 1 0 0\r\n0 0 0 0 0 0 1 4 4\r\n0 4 0 4 0 4 0 4 0\r\n0 4 2 2 2 2 2 2 2\r\n1 1 1 1 1 1 1 1 0\r\n0 2 0 3 0 1 0 2 0\r\n']
    testOutput = ['1\r\n', '4\r\n', '43\r\n', '46\r\n', '216\r\n', '89\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


