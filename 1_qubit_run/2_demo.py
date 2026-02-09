from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

# Create circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

qc.h(0)
qc.measure(0, 0)

# Choose simulator
backend = Aer.get_backend('aer_simulator')

# Prepare and run
compiled_circuit = transpile(qc, backend)
job = backend.run(compiled_circuit, shots=1)
result = job.result()

# Get the measurement result
counts = result.get_counts()
print(counts)