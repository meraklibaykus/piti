# Generated from Math.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
from .MathListener import MathListener
from .MathLexer import MathLexer
from .MathParser import MathParser

class MathParser(Parser):

    # Visit a parse tree produced by MathParser#expression.
    def visitExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#multiplyingExpression.
    def visitMultiplyingExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#powExpression.
    def visitPowExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#signedAtom.
    def visitSignedAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#atom.
    def visitAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#scientific.
    def visitScientific(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#constant.
    def visitConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#variable.
    def visitVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#relop.
    def visitRelop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#mulop.
    def visitMulop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#addop.
    def visitAddop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#unary.
    def visitUnary(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#bracketedExpression.
    def visitBracketedExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#function.
    def visitFunction(self, ctx):
        return self.visitChildren(ctx)



del MathParser
