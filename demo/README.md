step 1: `$ pip install protobuf`

step 2: generate protobuf class

```bash
cd protobuf-python-demo
$ .\protobuf-complier\protoc-3.13.0-win64\bin\protoc.exe --python_out=.\demo\generated_code .\demo\addressbook.proto
```

or to use syntax proto3:

```bash
cd protobuf-python-demo
$ .\protobuf-complier\protoc-3.13.0-win64\bin\protoc.exe --python_out=.\demo\generated_code .\demo\addressbook_syntax_proto3.proto
```

step 3: run `python main.py`

or to use syntax proto3:

run `python main_syntax_proto3.py`