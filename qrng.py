import qiskit as q
from math import sqrt
from numpy import arccos
from qiskit.execute_function import execute
from js import console

def prepare_register(n):
    quantum = q.QuantumRegister(n)
    classical = q.ClassicalRegister(n)
    register = q.QuantumCircuit(quantum, classical)
    register.x(0)
    
    count = n
    for i in range(0, n - 1):
        angle = 2.0* arccos(1.0 / sqrt(count))
        register.cry(angle, i, i + 1)
        register.cx(i + 1, i)
        count -= 1
    
    return register

def measure_register(register):
    register.measure_all()

    backend = q.BasicAer.get_backend('qasm_simulator')
    job = execute(register, backend, shots=1)
    result = job.result()
    counts = result.get_counts()
    return counts