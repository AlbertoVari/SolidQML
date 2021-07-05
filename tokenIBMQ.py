# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
IBMQ.save_account('MY_TOKEN')
#IBMQ.load_account(
provider = IBMQ.load_account()
# END

#create profile in folder $HOME/.qiskit/qiskitrc

# [ibmq]
# token = MY_TOKEN
# url = https://auth.quantum-computing.ibm.com/api
# verify = True