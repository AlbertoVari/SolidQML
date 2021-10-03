
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ, QuantumRegister, ClassicalRegister
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from numpy import pi
import json
# Loading your IBM Q account(s)
IBMQ.load_account()
provider = IBMQ.load_account()
print(provider.backends())
# exit(
# Simulation)
# backend = provider.get_backend('ibmq_qasm_simulator')
backend = provider.get_backend('ibmq_lima')
status = backend.status()
is_operational = status.operational
jobs_in_queue = status.pending_jobs
print(is_operational,jobs_in_queue)



from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[0])
circuit.barrier(qreg_q[0])
circuit.ry(pi/2, qreg_q[0])
circuit.barrier(qreg_q[0])
circuit.measure(qreg_q[0], creg_c[0])

print(circuit)
num_shots = 1000
job = execute(circuit, backend, shots=num_shots)
result = job.result()
counts = result.get_counts(circuit)
print("Result : ",result)

sort_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
states = 0
prob = [0,0]

print("Res  Counts  Prob")
for i in sort_counts:
        prob[states] = i[1]/num_shots
        print(i[0], i[1], i[1]/num_shots)
        states = states + 1

