#pragma once

#include <vector>

#include <tuple>

using XoredChar = std::tuple< char, char >;

using XoredString = std::vector< XoredChar >;


class StringBuilder
{

public:

	std::string BuildString( const XoredString & XoredString );

};
