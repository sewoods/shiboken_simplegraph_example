#ifndef __DATAGENERATOR_H
#define __DATAGENERATOR_H

#include <vector>

class DataGenerator 
{
public:
    DataGenerator();
    DataGenerator(const DataGenerator &other);
    DataGenerator& operator=(const DataGenerator &other);
    ~DataGenerator();

    std::vector<double> getData(std::vector<double> &x_data);

    void notUsedMethod();

};
#endif 