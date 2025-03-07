from enum import Enum
import time


# Define RRC States
class RRCState(Enum):
    IDLE = "RRC_IDLE"
    CONNECTED = "RRC_CONNECTED"


# UE class to simulate the device
class UE:
    def __init__(self, ue_id):
        self.ue_id = ue_id
        self.state = RRCState.IDLE
        self.c_rnti = None

    def random_access(self, network):
        print(f"UE [{self.ue_id}] in {self.state.value}: Sending Random Access Preamble...")
        time.sleep(0.5)
        network.receive_preamble(self)

    def receive_rar(self, timing_advance, uplink_grant, network):
        print(f"UE [{self.ue_id}]: Received RAR - TA: {timing_advance}, Grant: {uplink_grant}")
        self.initiate_connection(network)

    def initiate_connection(self, network):
        print(f"UE [{self.ue_id}]: Sending RRC Connection Request...")
        network.receive_rrc_connection_request(self)

    def receive_rrc_connection_setup(self, c_rnti, config):
        print(f"UE [{self.ue_id}]: Received RRC Connection Setup, C-RNTI: {c_rnti}")
        self.c_rnti = c_rnti
        self.state = RRCState.CONNECTED
        print(f"UE [{self.ue_id}]: Transitioned to {self.state.value}")
        return {"message": "RRC Connection Setup Complete", "ue_id": self.ue_id}


# Network class to simulate eNodeB
class Network:
    def receive_preamble(self, ue):
        print("Network: Received Random Access Preamble")
        time.sleep(0.5)
        self.send_rar(ue)

    def send_rar(self, ue):
        timing_advance = "1.2ms"
        uplink_grant = "Allocated"
        ue.receive_rar(timing_advance, uplink_grant, self)  # Pass 'self' (network instance)

    def receive_rrc_connection_request(self, ue):
        print(f"Network: Received RRC Connection Request from UE [{ue.ue_id}]")
        time.sleep(1)  # Simulate processing delay
        c_rnti = "C-RNTI-1234"  # Assign a temporary identifier
        config = {"SRB1": "Configured"}
        response = {"c_rnti": c_rnti, "config": config}
        ue.receive_rrc_connection_setup(response["c_rnti"], response["config"])
        self.receive_rrc_connection_setup_complete(ue)

    def receive_rrc_connection_setup_complete(self, ue):
        print(f"Network: Received RRC Connection Setup Complete from UE [{ue.ue_id}]")
        print(f"Network: UE [{ue.ue_id}] is now in {ue.state.value}")


# Main simulation function
def simulate_rrc_connection():
    ue = UE("UE-001")
    network = Network()
    print("Starting RRC Connection Establishment Simulation...")
    ue.random_access(network)


# Run the simulation
if __name__ == "__main__":
    simulate_rrc_connection()
