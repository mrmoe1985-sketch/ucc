"""Unit tests for PandoraPass."""
import unittest
from qiskit import QuantumCircuit
from qiskit.converters import circuit_to_dag, dag_to_circuit
from ucc.transpilers.pandora_pass import PandoraPass

class TestPandoraPass(unittest.TestCase):
    def test_init(self):
        """Test pass initialization."""
        pass_obj = PandoraPass()
        self.assertIsNotNone(pass_obj)

    def test_run_large_circuit(self):
        """Test pass on larger circuit."""
        qc = QuantumCircuit(4)
        for i in range(3):
            qc.cx(i, i+1)
        dag = circuit_to_dag(qc)
        pass_obj = PandoraPass()
        result_dag = pass_obj.run(dag)
        result_qc = dag_to_circuit(result_dag)
        self.assertEqual(result_qc.num_qubits, 4)

if __name__ == "__main__":
    unittest.main()
