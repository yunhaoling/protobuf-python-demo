# protobuf-python-demo

There're two implementation of python protobuf: pure python or python c++
- To install pure Python version
  - option1: pip install protobuf
  - option2: install from source code
    - $ python setup.py install
- To install C++ version from source code
  - (cd .. && make install); $ python setup.py install --cpp_implementation
  - "This step may require superuser privileges. NOTE: To use C++ implementation, you need to export an environment variable before running your program. See the "C++ Implementation" section below for more details."
    - The C++ implementation for Python messages is built as a Python extension to improve the overall protobuf Python performance.
    - To use the C++ implementation, you need to install the C++ protobuf runtime library, see https://github.com/protocolbuffers/protobuf/tree/master/src.


protobuf python: https://github.com/protocolbuffers/protobuf/tree/master/python
python install introduction: https://docs.python.org/3.8/install/