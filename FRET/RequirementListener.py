# Generated from Requirement.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RequirementParser import RequirementParser
else:
    from RequirementParser import RequirementParser

# This class defines a complete listener for a parse tree produced by RequirementParser.
class RequirementListener(ParseTreeListener):

    # Enter a parse tree produced by RequirementParser#reqts.
    def enterReqts(self, ctx:RequirementParser.ReqtsContext):
        pass

    # Exit a parse tree produced by RequirementParser#reqts.
    def exitReqts(self, ctx:RequirementParser.ReqtsContext):
        pass


    # Enter a parse tree produced by RequirementParser#reqt.
    def enterReqt(self, ctx:RequirementParser.ReqtContext):
        pass

    # Exit a parse tree produced by RequirementParser#reqt.
    def exitReqt(self, ctx:RequirementParser.ReqtContext):
        pass


    # Enter a parse tree produced by RequirementParser#reqt_body.
    def enterReqt_body(self, ctx:RequirementParser.Reqt_bodyContext):
        pass

    # Exit a parse tree produced by RequirementParser#reqt_body.
    def exitReqt_body(self, ctx:RequirementParser.Reqt_bodyContext):
        pass


    # Enter a parse tree produced by RequirementParser#freeform.
    def enterFreeform(self, ctx:RequirementParser.FreeformContext):
        pass

    # Exit a parse tree produced by RequirementParser#freeform.
    def exitFreeform(self, ctx:RequirementParser.FreeformContext):
        pass


    # Enter a parse tree produced by RequirementParser#nasa.
    def enterNasa(self, ctx:RequirementParser.NasaContext):
        pass

    # Exit a parse tree produced by RequirementParser#nasa.
    def exitNasa(self, ctx:RequirementParser.NasaContext):
        pass


    # Enter a parse tree produced by RequirementParser#scope.
    def enterScope(self, ctx:RequirementParser.ScopeContext):
        pass

    # Exit a parse tree produced by RequirementParser#scope.
    def exitScope(self, ctx:RequirementParser.ScopeContext):
        pass


    # Enter a parse tree produced by RequirementParser#reqt_condition.
    def enterReqt_condition(self, ctx:RequirementParser.Reqt_conditionContext):
        pass

    # Exit a parse tree produced by RequirementParser#reqt_condition.
    def exitReqt_condition(self, ctx:RequirementParser.Reqt_conditionContext):
        pass


    # Enter a parse tree produced by RequirementParser#regular_condition.
    def enterRegular_condition(self, ctx:RequirementParser.Regular_conditionContext):
        pass

    # Exit a parse tree produced by RequirementParser#regular_condition.
    def exitRegular_condition(self, ctx:RequirementParser.Regular_conditionContext):
        pass


    # Enter a parse tree produced by RequirementParser#qualifier_word.
    def enterQualifier_word(self, ctx:RequirementParser.Qualifier_wordContext):
        pass

    # Exit a parse tree produced by RequirementParser#qualifier_word.
    def exitQualifier_word(self, ctx:RequirementParser.Qualifier_wordContext):
        pass


    # Enter a parse tree produced by RequirementParser#qualified_condition1.
    def enterQualified_condition1(self, ctx:RequirementParser.Qualified_condition1Context):
        pass

    # Exit a parse tree produced by RequirementParser#qualified_condition1.
    def exitQualified_condition1(self, ctx:RequirementParser.Qualified_condition1Context):
        pass


    # Enter a parse tree produced by RequirementParser#qualified_condition2.
    def enterQualified_condition2(self, ctx:RequirementParser.Qualified_condition2Context):
        pass

    # Exit a parse tree produced by RequirementParser#qualified_condition2.
    def exitQualified_condition2(self, ctx:RequirementParser.Qualified_condition2Context):
        pass


    # Enter a parse tree produced by RequirementParser#scope_condition.
    def enterScope_condition(self, ctx:RequirementParser.Scope_conditionContext):
        pass

    # Exit a parse tree produced by RequirementParser#scope_condition.
    def exitScope_condition(self, ctx:RequirementParser.Scope_conditionContext):
        pass


    # Enter a parse tree produced by RequirementParser#scope_mode.
    def enterScope_mode(self, ctx:RequirementParser.Scope_modeContext):
        pass

    # Exit a parse tree produced by RequirementParser#scope_mode.
    def exitScope_mode(self, ctx:RequirementParser.Scope_modeContext):
        pass


    # Enter a parse tree produced by RequirementParser#pre_condition.
    def enterPre_condition(self, ctx:RequirementParser.Pre_conditionContext):
        pass

    # Exit a parse tree produced by RequirementParser#pre_condition.
    def exitPre_condition(self, ctx:RequirementParser.Pre_conditionContext):
        pass


    # Enter a parse tree produced by RequirementParser#stop_condition.
    def enterStop_condition(self, ctx:RequirementParser.Stop_conditionContext):
        pass

    # Exit a parse tree produced by RequirementParser#stop_condition.
    def exitStop_condition(self, ctx:RequirementParser.Stop_conditionContext):
        pass


    # Enter a parse tree produced by RequirementParser#component.
    def enterComponent(self, ctx:RequirementParser.ComponentContext):
        pass

    # Exit a parse tree produced by RequirementParser#component.
    def exitComponent(self, ctx:RequirementParser.ComponentContext):
        pass


    # Enter a parse tree produced by RequirementParser#response.
    def enterResponse(self, ctx:RequirementParser.ResponseContext):
        pass

    # Exit a parse tree produced by RequirementParser#response.
    def exitResponse(self, ctx:RequirementParser.ResponseContext):
        pass


    # Enter a parse tree produced by RequirementParser#satisfaction.
    def enterSatisfaction(self, ctx:RequirementParser.SatisfactionContext):
        pass

    # Exit a parse tree produced by RequirementParser#satisfaction.
    def exitSatisfaction(self, ctx:RequirementParser.SatisfactionContext):
        pass


    # Enter a parse tree produced by RequirementParser#timing.
    def enterTiming(self, ctx:RequirementParser.TimingContext):
        pass

    # Exit a parse tree produced by RequirementParser#timing.
    def exitTiming(self, ctx:RequirementParser.TimingContext):
        pass


    # Enter a parse tree produced by RequirementParser#timing_aux.
    def enterTiming_aux(self, ctx:RequirementParser.Timing_auxContext):
        pass

    # Exit a parse tree produced by RequirementParser#timing_aux.
    def exitTiming_aux(self, ctx:RequirementParser.Timing_auxContext):
        pass


    # Enter a parse tree produced by RequirementParser#duration_upper.
    def enterDuration_upper(self, ctx:RequirementParser.Duration_upperContext):
        pass

    # Exit a parse tree produced by RequirementParser#duration_upper.
    def exitDuration_upper(self, ctx:RequirementParser.Duration_upperContext):
        pass


    # Enter a parse tree produced by RequirementParser#duration_lower.
    def enterDuration_lower(self, ctx:RequirementParser.Duration_lowerContext):
        pass

    # Exit a parse tree produced by RequirementParser#duration_lower.
    def exitDuration_lower(self, ctx:RequirementParser.Duration_lowerContext):
        pass


    # Enter a parse tree produced by RequirementParser#component_name.
    def enterComponent_name(self, ctx:RequirementParser.Component_nameContext):
        pass

    # Exit a parse tree produced by RequirementParser#component_name.
    def exitComponent_name(self, ctx:RequirementParser.Component_nameContext):
        pass


    # Enter a parse tree produced by RequirementParser#mode_name.
    def enterMode_name(self, ctx:RequirementParser.Mode_nameContext):
        pass

    # Exit a parse tree produced by RequirementParser#mode_name.
    def exitMode_name(self, ctx:RequirementParser.Mode_nameContext):
        pass


    # Enter a parse tree produced by RequirementParser#duration.
    def enterDuration(self, ctx:RequirementParser.DurationContext):
        pass

    # Exit a parse tree produced by RequirementParser#duration.
    def exitDuration(self, ctx:RequirementParser.DurationContext):
        pass


    # Enter a parse tree produced by RequirementParser#timeunit.
    def enterTimeunit(self, ctx:RequirementParser.TimeunitContext):
        pass

    # Exit a parse tree produced by RequirementParser#timeunit.
    def exitTimeunit(self, ctx:RequirementParser.TimeunitContext):
        pass


    # Enter a parse tree produced by RequirementParser#post_condition.
    def enterPost_condition(self, ctx:RequirementParser.Post_conditionContext):
        pass

    # Exit a parse tree produced by RequirementParser#post_condition.
    def exitPost_condition(self, ctx:RequirementParser.Post_conditionContext):
        pass


    # Enter a parse tree produced by RequirementParser#AtPrevNext.
    def enterAtPrevNext(self, ctx:RequirementParser.AtPrevNextContext):
        pass

    # Exit a parse tree produced by RequirementParser#AtPrevNext.
    def exitAtPrevNext(self, ctx:RequirementParser.AtPrevNextContext):
        pass


    # Enter a parse tree produced by RequirementParser#Arrow.
    def enterArrow(self, ctx:RequirementParser.ArrowContext):
        pass

    # Exit a parse tree produced by RequirementParser#Arrow.
    def exitArrow(self, ctx:RequirementParser.ArrowContext):
        pass


    # Enter a parse tree produced by RequirementParser#TrivialParan.
    def enterTrivialParan(self, ctx:RequirementParser.TrivialParanContext):
        pass

    # Exit a parse tree produced by RequirementParser#TrivialParan.
    def exitTrivialParan(self, ctx:RequirementParser.TrivialParanContext):
        pass


    # Enter a parse tree produced by RequirementParser#Relation.
    def enterRelation(self, ctx:RequirementParser.RelationContext):
        pass

    # Exit a parse tree produced by RequirementParser#Relation.
    def exitRelation(self, ctx:RequirementParser.RelationContext):
        pass


    # Enter a parse tree produced by RequirementParser#Or.
    def enterOr(self, ctx:RequirementParser.OrContext):
        pass

    # Exit a parse tree produced by RequirementParser#Or.
    def exitOr(self, ctx:RequirementParser.OrContext):
        pass


    # Enter a parse tree produced by RequirementParser#And.
    def enterAnd(self, ctx:RequirementParser.AndContext):
        pass

    # Exit a parse tree produced by RequirementParser#And.
    def exitAnd(self, ctx:RequirementParser.AndContext):
        pass


    # Enter a parse tree produced by RequirementParser#Long.
    def enterLong(self, ctx:RequirementParser.LongContext):
        pass

    # Exit a parse tree produced by RequirementParser#Long.
    def exitLong(self, ctx:RequirementParser.LongContext):
        pass


    # Enter a parse tree produced by RequirementParser#Negate.
    def enterNegate(self, ctx:RequirementParser.NegateContext):
        pass

    # Exit a parse tree produced by RequirementParser#Negate.
    def exitNegate(self, ctx:RequirementParser.NegateContext):
        pass


    # Enter a parse tree produced by RequirementParser#IfThen.
    def enterIfThen(self, ctx:RequirementParser.IfThenContext):
        pass

    # Exit a parse tree produced by RequirementParser#IfThen.
    def exitIfThen(self, ctx:RequirementParser.IfThenContext):
        pass


    # Enter a parse tree produced by RequirementParser#TrivialFalse.
    def enterTrivialFalse(self, ctx:RequirementParser.TrivialFalseContext):
        pass

    # Exit a parse tree produced by RequirementParser#TrivialFalse.
    def exitTrivialFalse(self, ctx:RequirementParser.TrivialFalseContext):
        pass


    # Enter a parse tree produced by RequirementParser#TrivialTrue.
    def enterTrivialTrue(self, ctx:RequirementParser.TrivialTrueContext):
        pass

    # Exit a parse tree produced by RequirementParser#TrivialTrue.
    def exitTrivialTrue(self, ctx:RequirementParser.TrivialTrueContext):
        pass


    # Enter a parse tree produced by RequirementParser#MulDelMod.
    def enterMulDelMod(self, ctx:RequirementParser.MulDelModContext):
        pass

    # Exit a parse tree produced by RequirementParser#MulDelMod.
    def exitMulDelMod(self, ctx:RequirementParser.MulDelModContext):
        pass


    # Enter a parse tree produced by RequirementParser#Long2.
    def enterLong2(self, ctx:RequirementParser.Long2Context):
        pass

    # Exit a parse tree produced by RequirementParser#Long2.
    def exitLong2(self, ctx:RequirementParser.Long2Context):
        pass


    # Enter a parse tree produced by RequirementParser#AddSub.
    def enterAddSub(self, ctx:RequirementParser.AddSubContext):
        pass

    # Exit a parse tree produced by RequirementParser#AddSub.
    def exitAddSub(self, ctx:RequirementParser.AddSubContext):
        pass


    # Enter a parse tree produced by RequirementParser#TrivialParan2.
    def enterTrivialParan2(self, ctx:RequirementParser.TrivialParan2Context):
        pass

    # Exit a parse tree produced by RequirementParser#TrivialParan2.
    def exitTrivialParan2(self, ctx:RequirementParser.TrivialParan2Context):
        pass


    # Enter a parse tree produced by RequirementParser#MinusNumber.
    def enterMinusNumber(self, ctx:RequirementParser.MinusNumberContext):
        pass

    # Exit a parse tree produced by RequirementParser#MinusNumber.
    def exitMinusNumber(self, ctx:RequirementParser.MinusNumberContext):
        pass


    # Enter a parse tree produced by RequirementParser#BasicNumber.
    def enterBasicNumber(self, ctx:RequirementParser.BasicNumberContext):
        pass

    # Exit a parse tree produced by RequirementParser#BasicNumber.
    def exitBasicNumber(self, ctx:RequirementParser.BasicNumberContext):
        pass


    # Enter a parse tree produced by RequirementParser#Power.
    def enterPower(self, ctx:RequirementParser.PowerContext):
        pass

    # Exit a parse tree produced by RequirementParser#Power.
    def exitPower(self, ctx:RequirementParser.PowerContext):
        pass



del RequirementParser