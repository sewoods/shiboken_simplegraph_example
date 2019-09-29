#ifndef __DATAGENERATOR_H
#define __DATAGENERATOR_H

#include <vector>
#include "internalclass.h"

class DataGenerator 
{
public:
    DataGenerator();
    DataGenerator(const DataGenerator &other);
    DataGenerator& operator=(const DataGenerator &other);
    ~DataGenerator();

    std::vector<double> getData(std::vector<double> &x_data);

    const InternalClass& getInternalClass();

private:

    InternalClass  internalClass;    

};
inline const InternalClass& DataGenerator::getInternalClass()
{
    return internalClass;
} 
#endif 