import antlr4
from antlr4.InputStream import InputStream
from MathLexer import MathLexer
from MathParser import MathParser
from sympy import *

# input file name
input_file_name = "matematik_sorulari.txt"

# output file name
output_file_name = "matematik_cevaplari.txt"

# error file name
error_file_name = "hatalar.txt"

# open input file
with open(input_file_name, "r") as input_file:
    # open output file
    with open(output_file_name, "w") as output_file:
        # open error file
        with open(error_file_name, "w") as error_file:
            for line in input_file:
                # create input stream from line
                input_stream = InputStream(line.strip())

                # create lexer from input stream
                lexer = MathLexer(input_stream)

                # create token stream from lexer
                token_stream = antlr4.CommonTokenStream(lexer)

                # create parser from token stream
                parser = MathParser(token_stream)

                try:
                    # parse the input and get the expression tree
                    tree = parser.expression()

                    # evaluate the expression tree and get the answer
                    answer = float(N(tree.evalf()))

                    # write the answer to the output file
                    output_file.write(line.strip() + " = " + str(answer) + "\n")
                except Exception as e:
                    # write the error message to the error file
                    error_file.write(str(e) + ": " + line)
