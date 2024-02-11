# Generated from Requirement.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RequirementParser import RequirementParser
else:
    from RequirementParser import RequirementParser

# This class defines a complete generic visitor for a parse tree produced by RequirementParser.

class RequirementVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RequirementParser#reqts.
    def visitReqts(self, ctx:RequirementParser.ReqtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#reqt.
    def visitReqt(self, ctx:RequirementParser.ReqtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#reqt_body.
    def visitReqt_body(self, ctx:RequirementParser.Reqt_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#freeform.
    def visitFreeform(self, ctx:RequirementParser.FreeformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#nasa.
    def visitNasa(self, ctx:RequirementParser.NasaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#scope.
    def visitScope(self, ctx:RequirementParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#reqt_condition.
    def visitReqt_condition(self, ctx:RequirementParser.Reqt_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#regular_condition.
    def visitRegular_condition(self, ctx:RequirementParser.Regular_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#qualifier_word.
    def visitQualifier_word(self, ctx:RequirementParser.Qualifier_wordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#qualified_condition1.
    def visitQualified_condition1(self, ctx:RequirementParser.Qualified_condition1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#qualified_condition2.
    def visitQualified_condition2(self, ctx:RequirementParser.Qualified_condition2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#scope_condition.
    def visitScope_condition(self, ctx:RequirementParser.Scope_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#scope_mode.
    def visitScope_mode(self, ctx:RequirementParser.Scope_modeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#pre_condition.
    def visitPre_condition(self, ctx:RequirementParser.Pre_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#stop_condition.
    def visitStop_condition(self, ctx:RequirementParser.Stop_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#component.
    def visitComponent(self, ctx:RequirementParser.ComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#response.
    def visitResponse(self, ctx:RequirementParser.ResponseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#satisfaction.
    def visitSatisfaction(self, ctx:RequirementParser.SatisfactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#timing.
    def visitTiming(self, ctx:RequirementParser.TimingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#timing_aux.
    def visitTiming_aux(self, ctx:RequirementParser.Timing_auxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#duration_upper.
    def visitDuration_upper(self, ctx:RequirementParser.Duration_upperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#duration_lower.
    def visitDuration_lower(self, ctx:RequirementParser.Duration_lowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#component_name.
    def visitComponent_name(self, ctx:RequirementParser.Component_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#mode_name.
    def visitMode_name(self, ctx:RequirementParser.Mode_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#duration.
    def visitDuration(self, ctx:RequirementParser.DurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#timeunit.
    def visitTimeunit(self, ctx:RequirementParser.TimeunitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#post_condition.
    def visitPost_condition(self, ctx:RequirementParser.Post_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#AtPrevNext.
    def visitAtPrevNext(self, ctx:RequirementParser.AtPrevNextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#Arrow.
    def visitArrow(self, ctx:RequirementParser.ArrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#TrivialParan.
    def visitTrivialParan(self, ctx:RequirementParser.TrivialParanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#Relation.
    def visitRelation(self, ctx:RequirementParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#Or.
    def visitOr(self, ctx:RequirementParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#And.
    def visitAnd(self, ctx:RequirementParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#Long.
    def visitLong(self, ctx:RequirementParser.LongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#Negate.
    def visitNegate(self, ctx:RequirementParser.NegateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#IfThen.
    def visitIfThen(self, ctx:RequirementParser.IfThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#TrivialFalse.
    def visitTrivialFalse(self, ctx:RequirementParser.TrivialFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#TrivialTrue.
    def visitTrivialTrue(self, ctx:RequirementParser.TrivialTrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#MulDelMod.
    def visitMulDelMod(self, ctx:RequirementParser.MulDelModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#Long2.
    def visitLong2(self, ctx:RequirementParser.Long2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#AddSub.
    def visitAddSub(self, ctx:RequirementParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#TrivialParan2.
    def visitTrivialParan2(self, ctx:RequirementParser.TrivialParan2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#MinusNumber.
    def visitMinusNumber(self, ctx:RequirementParser.MinusNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#BasicNumber.
    def visitBasicNumber(self, ctx:RequirementParser.BasicNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RequirementParser#Power.
    def visitPower(self, ctx:RequirementParser.PowerContext):
        return self.visitChildren(ctx)



del RequirementParser