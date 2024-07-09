import random
import time

class LWFFeeder:
    def __init__(self, initial_weight, setpoint, feed_factor):
        self.weight = initial_weight
        self.setpoint = setpoint
        self.feed_factor = feed_factor
        self.drive_command = 0
        self.last_weight = initial_weight
        self.last_time = time.time()

    def get_noisy_weight(self):
        # Simulate noisy weight measurement
        noise = random.gauss(0, 0.1)  # Mean 0, standard deviation 0.1
        return self.weight + noise

    def update_weight(self):
        # Simulate weight loss based on current drive command
        time_elapsed = time.time() - self.last_time
        weight_loss = (self.drive_command / 100) * self.feed_factor * time_elapsed
        self.weight -= weight_loss
        self.last_time = time.time()

    def calculate_mass_flow(self):
        current_weight = self.get_noisy_weight()
        time_elapsed = time.time() - self.last_time
        if time_elapsed > 0:
            mass_flow = (self.last_weight - current_weight) / time_elapsed
            self.last_weight = current_weight
            return max(mass_flow, 0)  # Ensure non-negative mass flow
        return 0

    def update_drive_command(self, mass_flow):
        error = self.setpoint - mass_flow
        self.drive_command += error * 0.1  # Simple proportional control
        self.drive_command = max(0, min(100, self.drive_command))  # Limit to 0-100%

    def run_simulation(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.update_weight()
            mass_flow = self.calculate_mass_flow()
            self.update_drive_command(mass_flow)
            
            print(f"Time: {time.time() - start_time:.2f}s, "
                  f"Weight: {self.weight:.2f}, "
                  f"Mass Flow: {mass_flow:.2f}, "
                  f"Drive Command: {self.drive_command:.2f}%")
            
            time.sleep(0.1)  # Simulate processing time

# Run the simulation
feeder = LWFFeeder(initial_weight=100, setpoint=5, feed_factor=10)
feeder.run_simulation(duration=30)