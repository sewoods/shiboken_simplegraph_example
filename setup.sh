#!/bin/sh

set -eu

# build
rm -rf ./build
mkdir build
cd build
cmake -H.. -B. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release
make -j8
make install

# install
cd ../package
pip install . --upgrade --force-reinstall
