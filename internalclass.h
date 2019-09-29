#ifndef __INTERNALCLASS_H
#define __INTERNALCLASS_H

#include <string>

// This is an example of a class used internally by the 
// C++ library that we will not need to wrap or access from
// Python
class InternalClass
{
public:
    InternalClass();

private:

    std::string internalString;

};

#endif