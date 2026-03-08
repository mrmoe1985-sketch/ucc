"""Unit tests for QCrankPass."""
import unittest
from qiskit import QuantumCircuit
from qiskit.converters import circuit_to_dag, dag_to_circuit
from ucc.transpilers.qcrank_pass import QCrankPass

class TestQCrankPass(unittest.TestCase):
    def test_init(self):
        """Test pass initialization."""
        pass_obj = QCrankPass()
        self.assertIsNotNone(pass_obj)

    def test_run_circuit(self):
        """Test pass on circuit."""
        qc = QuantumCircuit(3)
        qc.h(0)
        qc.cx(0, 1)
        qc.cx(1, 2)
        dag = circuit_to_dag(qc)
        pass_obj = QCrankPass()
        result_dag = pass_obj.run(dag)
        result_qc = dag_to_circuit(result_dag)
        self.assertEqual(result_qc.num_qubits, 3)

if __name__ == "__main__":
    unittest.main()
