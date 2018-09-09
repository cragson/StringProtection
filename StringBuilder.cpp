#include "StringBuilder.hpp"

#include <iostream>

std::string StringBuilder::BuildString( const XoredString & XoredString )
{
	std::string result = "";

	for ( uint16_t _index = 0; _index < XoredString.size(); _index++ )
	{
		const auto xoredChar = XoredString.at(_index);

		result += static_cast<char>( std::get< 0 >(xoredChar) ^ std::get< 1 >(xoredChar) );
	}

	return result;
}
