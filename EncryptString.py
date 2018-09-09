# A tool made for StringBuilder, which prints out encrypted strings with random xor values
# made by calb/ cragson

from random import randint

# Only unicode
def GetDecimalFromChar( CHAR ):
    return ord( CHAR )

# 0 <= DECIMAL <= 0x10FFFF
def GetCharFromDecimal( DECIMAL ):
    return chr( DECIMAL )

def encrypt_str( STRING ):
    
    xor_list = []

    _num1 = 0
    _num2 = 0

    _elemDecimal = 0
    
    for _elem in STRING:
        
        _elemDecimal = GetDecimalFromChar( _elem.encode("ascii") )

        while( _num1 ^ _num2 != _elemDecimal ):
            _num1 = randint(-128,127)
            _num2 = randint(-128,127)

        xor_list.append( _num1 )
        xor_list.append( _num2 )

    return xor_list

def decrypt_str( XOR_LIST ):

    msg = ""

    for _i in range( 0, len( XOR_LIST ) - 1, 2 ):
        
        msg += GetCharFromDecimal( XOR_LIST[ _i ] ^ XOR_LIST[ _i + 1 ] )
        
    return msg


def generate_c_code( STRING_ARRAY ):

    code = []

    codeElement = ""
    
    xor_list = []

    _VariableName = ""
    
    for _string in STRING_ARRAY:

        xor_list = encrypt_str( _string )

        _VariableName = _string.upper().replace('.', '')

        codeElement = "XoredString " + _VariableName + " = { "  
        
        for _xorIndex in range( 0, len( xor_list ) - 1, 2 ):
            
            if( _xorIndex == len( xor_list ) - 2 ):
                codeElement += "std::tuple< char, char >( " +  str( xor_list[ _xorIndex ] ) + " , " + str( xor_list[ _xorIndex + 1 ] ) + " ) }"
            else:
                codeElement += "std::tuple< char, char >( " + str( xor_list[ _xorIndex ] ) + " , " + str( xor_list[ _xorIndex + 1 ] ) + " ) , "
                
        codeElement = ''.join( codeElement ).strip()

        codeElement += "; // Decrypted String: " + _string

        code.append( codeElement )

    return code

def display_c_code( CODE ):

    for _codeLine in CODE:
        print(_codeLine + "\n" )
    

def main():

    xor = [ "LoadLibraryW", "ntdll", "ZwReadVirtualMemory" ]

    code = generate_c_code( xor )

    display_c_code( code )

if __name__ == '__main__':
    main()
