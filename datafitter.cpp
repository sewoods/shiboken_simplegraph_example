#include "datafitter.h"

#include <algorithm>
#include <numeric>

DataFitter::DataFitter()
{

}

DataFitter::~DataFitter()
{

}

DataFitter::DataFitter(const DataFitter &other)
{

}

DataFitter& DataFitter::operator=(const DataFitter &other)
{
    if (this != &other)
    {
        // Copy variables
    }
    return *this;
}

std::vector<double> DataFitter::linearRegression(std::vector<double> &x,
                                    std::vector<double> &y)
{
    const auto n    = x.size();
    const auto s_x  = std::accumulate(x.begin(), x.end(), 0.0);
    const auto s_y  = std::accumulate(y.begin(), y.end(), 0.0);
    const auto s_xx = std::inner_product(x.begin(), x.end(), x.begin(), 0.0);
    const auto s_xy = std::inner_product(x.begin(), x.end(), y.begin(), 0.0);
    const auto a    = (n * s_xy - s_x * s_y) / (n * s_xx - s_x * s_x);
    const auto b    = (s_y - a*s_x)/n;
    std::vector<double> slope_intercept;
    slope_intercept.push_back(a);
    slope_intercept.push_back(b);
    return slope_intercept;

}