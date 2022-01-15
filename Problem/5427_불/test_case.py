class TestCase(list):

  def __init__(self):
    self.addTestCase()

  def appendTest(self,testInput,testOutput):
    self.append((testInput,testOutput))
  
  def addTestCase(self):
    testInput = ['5\r\r\n4 3\r\r\n####\r\r\n#*@.\r\r\n####\r\r\n7 6\r\r\n###.###\r\r\n#*#.#*#\r\r\n#.....#\r\r\n#.....#\r\r\n#..@..#\r\r\n#######\r\r\n7 4\r\r\n###.###\r\r\n#....*#\r\r\n#@....#\r\r\n.######\r\r\n5 5\r\r\n.....\r\r\n.***.\r\r\n.*@*.\r\r\n.***.\r\r\n.....\r\r\n3 3\r\r\n###\r\r\n#@#\r\r\n###\r\r\n']
    testOutput = ['2\r\r\n5\r\r\nIMPOSSIBLE\r\r\nIMPOSSIBLE\r\r\nIMPOSSIBLE\r\r\n']
    for i in range(len(testInput)):
      self.appendTest(testInput=testInput[i],testOutput=testOutput[i])


