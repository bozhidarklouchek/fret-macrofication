from antlr4 import *
from antlr4.tree.Trees import Trees
from collections import namedtuple
import sys, json
sys.path.append('../../grammar')
from RequirementLexer import RequirementLexer
from RequirementParser import RequirementParser


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
    if(not node.t):
      return ['G', self.build(node.a)]
    return ['G', self.build(node.t), self.build(node.a)]
  
  def buildU(self, node):
    return ['U', self.build(node.a), self.build(node.b)]
  
  def buildX(self, node):
    return ['X', self.build(node.a)]
  
  def buildV(self, node):
    return ['V', self.build(node.a), self.build(node.b)]

  def buildF(self, node):
    if(not node.t):
      return ['F', self.build(node.a)]
    return ['F', self.build(node.t), self.build(node.a)]
  
  def buildTl_intvl(self, node):
    return node.getText()
  
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

def addSerilisationToReqts(reqts, readFormulasCount):
  print('Serialising...')
  for reqt in reqts:
    reqt['serialisation'] = fret2json(reqt['reqid'], reqt['fret'])
  
  serialisedFormulasCount = len([reqt['serialisation'] for reqt in reqts if reqt['serialisation'] != None])
  
  print('I attempted to serialise', readFormulasCount, 'and serialised',
        serialisedFormulasCount, 'formulas.', end=' ')
  return reqts, serialisedFormulasCount

def fret2json(id, fret):
    if(not fret):
      return None
  
    serialised = None
    try:
      lexer = RequirementLexer(InputStream(fret))
      stream = CommonTokenStream(lexer)
      parser = RequirementParser(stream)
      cst = parser.post_condition()
      serialised = RequirementAstBuilder().build(cst)
    except Exception:
      print(id, ' FRET reqt is broken!')
      return None
    return serialised
