class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['26\r\r\nadd 1\r\r\nadd 2\r\r\ncheck 1\r\r\ncheck 2\r\r\ncheck 3\r\r\nremove 2\r\r\ncheck 1\r\r\ncheck 2\r\r\ntoggle 3\r\r\ncheck 1\r\r\ncheck 2\r\r\ncheck 3\r\r\ncheck 4\r\r\nall\r\r\ncheck 10\r\r\ncheck 20\r\r\ntoggle 10\r\r\nremove 20\r\r\ncheck 10\r\r\ncheck 20\r\r\nempty\r\r\ncheck 1\r\r\ntoggle 1\r\r\ncheck 1\r\r\ntoggle 1\r\r\ncheck 1\r\r\n']
    testOutput = ['1\r\r\n1\r\r\n0\r\r\n1\r\r\n0\r\r\n1\r\r\n0\r\r\n1\r\r\n0\r\r\n1\r\r\n1\r\r\n0\r\r\n0\r\r\n0\r\r\n1\r\r\n0\r\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


