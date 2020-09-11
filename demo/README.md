step 1: `$ pip install protobuf`

step 2: generate protobuf class

```bash
$ ..\protobuf-complier\protoc-3.13.0-win64\bin\protoc.exe --python_out=.\demo\generated_code .\demo\addressbook.proto
```

step 3: run `main.py`