Quantum Random Bit Generator (Qiskit)

This project demonstrates a simple quantum circuit using Qiskit that generates a random output (`0` or `1`) by placing a qubit into superposition and measuring it.

The program runs on the Qiskit Aer simulator and does not require real quantum hardware.

## Installation

Make sure Python (3.8 or higher) is installed, then install the required modules:

```bash
pip install qiskit qiskit-aer

$ python 1_qubit_run/1_demo.py

        ┌───┐ ░ ┌─┐
     q: ┤ H ├─░─┤M├
        └───┘ ░ └╥┘
meas: 1/═════════╩═
                 0

python 1_qubit_run/2_demo.py
{'1': 1}

