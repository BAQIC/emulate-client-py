# emulate-client-py

## How to install package
```bash
pip install git+https://github.com/BAQIC/emulate-client-py.git
```

Now you can just run the following code to get the help message:
```bash
client --help
```

You can use yaml config or command option to run the example:
```bash
client --mode QasmSimAgent --config examples/config.yaml

client --mode QasmSimAgent -f examples/bell.qasm --qubits 2 --shots 10 --task-mode sequence --agent-ip 127.0.0.1:3003
```

And you can also use it in your code:
```python
from emulate_client import EmulateClient

client = EmulateClient("127.0.0.1:3003")
client.qasmsim_agent("examples/example.qasm", 100, 10, "sequence")
```