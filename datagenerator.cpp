#include "datagenerator.h"

#include <stdlib.h>
#include <math.h>

DataGenerator::DataGenerator() :
    internalClass()
{

}

DataGenerator::~DataGenerator()
{

}

DataGenerator::DataGenerator(const DataGenerator &other)
{
}

DataGenerator& DataGenerator::operator=(const DataGenerator &other)
{
    if (this != &other)
    {
        // Copy variables
    }
    return *this;
}

std::vector<double> DataGenerator::getData(std::vector<double> &x_data)
{
    std::vector<double> y_data;
    for (double x: x_data)
    {
        int r = rand() % 7;
        double y = sin(x) + r*0.1;
        r = rand() % 10;
        y -= r*0.1;
        y_data.push_back(y);
    }

    return y_data;

}
