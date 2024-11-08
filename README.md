# emulate-client-py

## How to install package
```bash
pip install git+https://github.com/BAQIC/emulate-client-py.git
```

Now you can just run the following code to use the package:
```bash
client --help
```

And you can also use it in your code:
```python
from emulate_client import qasmsim_agent

qasmsim_agent("127.0.0.1:3003", "examples/example.qasm", 100, 10, "sequence")
```