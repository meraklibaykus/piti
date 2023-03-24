from antlr4 import *
from MathParser import MathParser

class MathListener(ParseTreeListener):
    def enterAdd(self, ctx:MathParser.AddContext):
        print("Entering add expression:", ctx.getText())

    def exitAdd(self, ctx:MathParser.AddContext):
        print("Exiting add expression:", ctx.getText())

    def enterSubtract(self, ctx:MathParser.SubtractContext):
        print("Entering subtract expression:", ctx.getText())

    def exitSubtract(self, ctx:MathParser.SubtractContext):
        print("Exiting subtract expression:", ctx.getText())

    def enterMultiply(self, ctx:MathParser.MultiplyContext):
        print("Entering multiply expression:", ctx.getText())

    def exitMultiply(self, ctx:MathParser.MultiplyContext):
        print("Exiting multiply expression:", ctx.getText())

    def enterDivide(self, ctx:MathParser.DivideContext):
        print("Entering divide expression:", ctx.getText())

    def exitDivide(self, ctx:MathParser.DivideContext):
        print("Exiting divide expression:", ctx.getText())

    def enterPower(self, ctx:MathParser.PowerContext):
        print("Entering power expression:", ctx.getText())

    def exitPower(self, ctx:MathParser.PowerContext):
        print("Exiting power expression:", ctx.getText())

    def enterConstant(self, ctx:MathParser.ConstantContext):
        print("Entering constant expression:", ctx.getText())

    def exitConstant(self, ctx:MathParser.ConstantContext):
        print("Exiting constant expression:", ctx.getText())

    def enterVariable(self, ctx:MathParser.VariableContext):
        print("Entering variable expression:", ctx.getText())

    def exitVariable(self, ctx:MathParser.VariableContext):
        print("Exiting variable expression:", ctx.getText())
