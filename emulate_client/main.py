import click
from .client import EmulateClient

@click.command()
@click.option(
    "--mode",
    type=click.Choice(
        ["QasmSimAgent", "UpdateQasmSimAgent", "GetQasmSimAgent"],
        case_sensitive=False,
    ),
    required=True,
    help="The mode of the emulate client",
)
@click.option(
    "--agent-ip",
    "-a",
    type=str,
    default="127.0.0.1:3003",
    help="The agent ip address, include ip and port, please make sure your format is xxx.xxx.xxx.xxx:xxx",
)
@click.option("--file", "-f", type=str, default="", help="The qasm file path")
@click.option(
    "--shots",
    "-s",
    type=int,
    default=0,
    help="The number of shots the quantum circuit will run",
)
@click.option(
    "--qubits",
    "-q",
    type=int,
    default=0,
    help="The number of qubits the quantum circuit has",
)
@click.option(
    "--capacity",
    "-c",
    type=int,
    default=0,
    help="The capacity of the agent, the memory size of the agent",
)
@click.option(
    "--position",
    "-p",
    type=int,
    default=0,
    help="The position of the query in the agent memory, please make sure the position is valid",
)
@click.option(
    "--task-mode",
    "-t",
    type=click.Choice(
        ["sequence", "aggregation", "max", "min", "expectation"], case_sensitive=False
    ),
    default="sequence",
    help="The mode of the task",
)
def main(mode, agent_ip, file, shots, qubits, capacity, position, task_mode):
    client = EmulateClient(agent_ip)

    if mode == "QasmSimAgent":
        client.qasmsim_agent(file, shots, qubits, task_mode)
    elif mode == "UpdateQasmSimAgent":
        client.update_qasmsim_agent(agent_ip, qubits, capacity)
    elif mode == "GetQasmSimAgent":
        client.get_qasmsim_agent(agent_ip, position)
    else:
        raise ValueError("Invalid mode")
