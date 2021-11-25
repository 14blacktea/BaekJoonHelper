class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['ONETWOTHREEFOUR+FIVESIXSEVEN=\r\n', 'FIVEZEROxTWOTWO-ONEONEONEONE=\r\n']
    testOutput = ['1234+567=\r\nONEEIGHTZEROONE\r\n', '50x22-1111=\r\n-ONEONE\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


