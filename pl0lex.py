'''
pl0lex

Analizador Lexico para el lenguaje PL0
'''
import sly

class Lexer(sly.Lexer):
    tokens = {
        #Palabras Reservadas
        FUN, BEGIN, END, WHILE, DO, IF, THEN, ELSE,
        PRINT, WRITE, READ, RETURN, SKIP, BREAK, INT_T,
        FLOAT_T,
        #Asignacion (:=)
        ASIG, 

        #Operadores de Relacion (MEI = Menor igual <=) (MAI = Mayor igual >=) (II = Igual igual ==) (DI = Diferente igual !=)
        AND, OR, NOT, MEI, MAI, II, DI,

        #Literales
        INT, FLOAT, NAME, LITERAL
    }
    literals = '+-*/()[],;:<>"'

    ignore = ' \t\r0\n'

    @_(r'-?[1-9][0-9]*')
    def INT(self,t):
        t.value = int(t.value)
        return t

    @_('-?(0|[1-9][0-9]*),[0-9]+((e|E)(+|-)[0-9]+)?')
    def FLOAT(self,t):
        t.value = float(t.value)
        return t

    NAME = r'[a-zA-Z]+ [0-9]* [a-zA-Z]*'
    LITERAL = r'".*"'
    MEI    =r'<='
    MAI    =r'>='
    II     =r'=='
    DI     =r'!='
    WHILE = r'[[Ww][hH][Ii][Ll][Ee]]'
    ASIG   =r':='
    NOT    =r'[[Nn][oO][Tt]]'
    FUN    = r'[[Ff][uU][Nn]]'
    READ   = r'[rR][eE][aA][dD]' 
    WRITE   = r'[[wW][rR]i[I][Tt][eE]]'
    PRINT  = r'[[Pp][Rr][Ii][Nn][Tt]]'
    DO   = r'[[Dd][Oo]]'
    IF     = r'[[iI][fF]]'
    THEN   = r'[[Tt][Hh][Ee][Nn]]'
    ELSE =r'[[Ee][Ll][Ss][Ee]]'
    TO     = r'[[Tt][Oo]]'
    END    = r'[[Ee][Nn][Dd]]'
    BREAK  = r'[[Bb][Rr][Ee][Aa][Kk]]'
    RETURN = r'[[Rr][Ee][Tt][uU][rR][nN]]'
    SKIPE= r'[[sS][Kk][iI][pP][Ee]]'
    BEGIN    = r'[[Bb][Ee][Gg][Ii][Nn]]'
    AND    = r'[[Aa][Nn][Dd]]'
    OR    = r'[[O][R]]'
    FLOAT_T  = r'[[Ff][Ll][Oo][Aa][Tt]]'
    INT_T = r'[[iI][Nn][tT]]'

def error(self, t):
        print(f"Caracter ilegal '{t.value[0]}'")
        self.index += 1

def main(argv):
    if len(argv) != 2:
        print(f"Usage: python {argv[0]} filename")
        exit(1)
    
    lex = Lexer()
    txt = open(argv[1]).read()

    for tok in lex.tokenize(txt):
        print(tok)


if __name__ == '__main__':
    from sys import argv
    main(argv)


int main(int argc, char *argv[]) {
    
}
