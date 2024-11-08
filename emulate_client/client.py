import requests

class EmulateClient:
    def __init__(self, agent_ip):
        self.agent_ip = agent_ip

    def qasmsim_agent(self, file, shots, qubits, task_mode):
        with open(file) as f:
            content = f.read()
        payload = {
            "task_id": "test",
            "qasm": content,
            "shots": shots,
            "mode": task_mode,
            "qubits": qubits,
        }
        r = requests.post(f"http://{self.agent_ip}/submit", data=payload)
        print(r.json())

    def update_qasmsim_agent(self, qubits, capacity):
        payload = {}
        if qubits != 0:
            payload["qubits"] = qubits
        if capacity != 0:
            payload["capacity"] = capacity
        r = requests.post(f"http://{self.agent_ip}/update", data=payload)
        print(r.json())

    def get_qasmsim_agent(self, position):
        payload = {"pos": position}
        r = requests.get(f"http://{self.agent_ip}/get_measure", params=payload)
        print(r.json())
