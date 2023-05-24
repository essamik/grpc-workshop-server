**Setup**
```
python -m pip install --upgrade pip
python -m pip install grpcio 
python -m pip install grpcio-tools
```

**Generate proto files**
```
python -m grpc_tools.protoc -I protos/ --python_out=. --pyi_out=. --grpc_python_out=. .\protos\employee.proto
```

**Run Server**
```
python employee_server.py
```