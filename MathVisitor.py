from antlr4 import *
from MathParser import MathParser


class MathVisitor(ParseTreeVisitor):
    def visitAdd(self, ctx: MathParser.AddContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right

    def visitSubtract(self, ctx: MathParser.SubtractContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left - right

    def visitMultiply(self, ctx: MathParser.MultiplyContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right

    def visitDivide(self, ctx: MathParser.DivideContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left / right

    def visitNumber(self, ctx: MathParser.NumberContext):
        return float(ctx.NUMBER().getText())

    def visitParentheses(self, ctx: MathParser.ParenthesesContext):
        return self.visit(ctx.expr())
