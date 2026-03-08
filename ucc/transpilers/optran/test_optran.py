"""Unit tests for OpaqueTransformationPass."""
import unittest
from qiskit import QuantumCircuit
from qiskit.converters import circuit_to_dag, dag_to_circuit
from ucc.transpilers.optran_pass import OpaqueTransformationPass

class TestOpaqueTransformationPass(unittest.TestCase):
    def test_init(self):
        """Test pass initialization."""
        pass_obj = OpaqueTransformationPass()
        self.assertIsNotNone(pass_obj)

    def test_run_simple_circuit(self):
        """Test pass on simple circuit."""
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        dag = circuit_to_dag(qc)
        pass_obj = OpaqueTransformationPass()
        result_dag = pass_obj.run(dag)
        result_qc = dag_to_circuit(result_dag)
        self.assertEqual(result_qc.num_qubits, 2)

if __name__ == "__main__":
    unittest.main()
