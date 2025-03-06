import sys    #  sys is used to modify the Python path
sys.path.append('..')  # Add parent directory to path

from prach_simulation import PrachSimulation  # Use relative import

def test_low_load_success():
    sim = PrachSimulation(num_ues=10)
    result = sim.simulate_cfbra()
    assert result["successRate"] == 1.0, "Low load should have 100% success"
    assert result["collisionProb"] == 0.0, "No collisions expected"

def test_high_load_collision():
    sim = PrachSimulation(num_ues=100)
    result = sim.simulate_cfbra()
    assert result["successRate"] < 1.0, "High load should have reduced success"
    assert result["collisionProb"] > 0.0, "Collisions expected"

def test_network_check():
    sim = PrachSimulation(num_ues=10)
    result = sim.simulate_cfbra()
    assert result["networkStatus"] in ["Connected", "Disconnected"]





'''
What This Code is Doing?
Imports PrachSimulation from a parent directory.
Defines test functions to check different scenarios.
Breakdown of Tests
test_low_load_success()

Simulates a scenario with 10 UEs (low load).
Expects 100% success rate and 0% collision.
test_high_load_collision()

Simulates 100 UEs (high load).
Expects reduced success rate and some collisions.
test_network_check()

Checks whether the network status is either "Connected" or "Disconnected".
Testing Method Used
The script uses assertions (assert) to verify expected vs actual results.
If an assertion fails, it raises an AssertionError indicating a test failure.
✅ This is a basic unit testing approach without using a formal testing framework like pytest or unittest

'''