from antlr4 import *
from antlr4.tree.Trees import Trees
from RequirementLexer import RequirementLexer
from RequirementParser import RequirementParser
from collections import namedtuple
import sys, json

class RequirementAstBuilder:
  def buildPost_condition(self, node):
    return self.build(node.a)
  
  def buildY(self, node):
    return ['Y', self.build(node.a)]
  
  def buildH(self, node):
    return ['H', self.build(node.a)]

  def buildO(self, node):
    return ['O', self.build(node.a)]
  
  def buildG(self, node):
    return ['G', self.build(node.a)]
  
  def buildU(self, node):
    return ['U', self.build(node.a)]
  
  def buildX(self, node):
    return ['X', self.build(node.a)]
  
  def buildV(self, node):
    return ['V', self.build(node.a), self.build(node.b)]

  def buildF(self, node):
    return ['F', self.build(node.a)]
  
  def buildNegate(self, node):
    return [node.op.text, self.build(node.a)]

  def buildAnd(self, node):
    return ['&', self.build(node.a), self.build(node.b)]

  def buildOr(self, node):
    return [node.op.text, self.build(node.a), self.build(node.b)]
  
  def buildArrow(self, node):
    return [node.op.text, self.build(node.a), self.build(node.b)]
  
  def buildIfThen(self, node):
    return ['ifThen', self.build(node.a), self.build(node.b)]
  
  def buildRelation(self, node):
    return [node.op.text, self.build(node.a), self.build(node.b)]
  
  def buildAtPrevNext(self, node):
    if(node.op.text == 'PREVIOUS'):
        return ['atPrevOccurrenceOf', self.build(node.a), self.build(node.b)]
    else:
        return ['atNextOccurrenceOf', self.build(node.a), self.build(node.b)]

  def buildPower(self, node):
    return ['^', self.build(node.a), self.build(node.b)]

  def buildMinusNumber(self, node):
    return ['-', self.build(node.a)]
  
  def buildMulDelMod(self, node):
    return [node.op.text, self.build(node.a), self.build(node.b)]

  def buildAddSub(self, node):
    return [node.op.text, self.build(node.a), self.build(node.b)]

  def buildLong(self, node):
    return node.getText()
  
  def buildLong2(self, node):
    return node.getText()

  def buildBasicNumber(self, node):
    return node.getText()

  def buildIdentifier(self, node):
    return node.getText()

  def build(self, node):
    if not isinstance(node, ParserRuleContext):
      raise Exception(f"{node} must be a node, not a {type(node)}")
    name = "build" + type(node).__name__[:-7]
    if name[:12] == "buildTrivial":
      return self.build(node.a)
    return self.__getattribute__(name)(node)

def parseFile(path):
    asts = []
    counter = 1
    with open(path, 'r') as file:
        problemsOccurred = False
        for reqt in file:
            ast = None
            try:
              lexer = RequirementLexer(InputStream(reqt))
              stream = CommonTokenStream(lexer)
              parser = RequirementParser(stream)
              cst = parser.post_condition()
              ast = RequirementAstBuilder().build(cst)
            except:
              problemsOccurred = True
              print(counter, ' is broken!')
            asts.append({'id': counter, 'ast': ast})
            counter += 1

    if(not problemsOccurred):
        print('Successful serialisation!')

    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(asts, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
  path = sys.argv[1]
  parseFile(path)