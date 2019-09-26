#ifndef __DATAFITTER_H
#define __DATAFITTER_H

#include <vector>

class DataFitter
{
public:
    DataFitter();
    DataFitter(const DataFitter &other);
    DataFitter& operator=(const DataFitter &other);
    ~DataFitter();

    std::vector<double> linearRegression(std::vector<double> &x_data,
                            std::vector<double> &y_data);

};

#endif