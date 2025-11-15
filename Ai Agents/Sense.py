class SimpleAIAgent:

    """
    A basic Sense-Process-Act agent.
    """
    def __init__(self, name="Agent Alpha"):
        self.name = name
        self.mood = "Neutral"

    def sense_environment(self, state):
        """
        1. SENSE: Reads the current state of the environment.
        """
        print(f"[{self.name}]: Sensing environment... Current state is '{state}'.")
        return state

    def process_information(self, sensed_state):
        """
        2. PROCESS (Plan/Think): Determines the appropriate action based on the state.
        """
        if "danger" in sensed_state.lower() or "alert" in sensed_state.lower():
            action = "Flee"
            self.mood = "Anxious"
        elif "food" in sensed_state.lower() or "reward" in sensed_state.lower():
            action = "Approach"
            self.mood = "Excited"
        else:
            action = "Wait"
            self.mood = "Calm"
            
        print(f"[{self.name}]: Processing state... Decided on action: '{action}'. New mood: '{self.mood}'.")
        return action

    def act(self, action):
        """
        3. ACT: Executes the determined action.
        """
        print(f"[{self.name}]: Executing action: **{action}**.")
        print("---")
        return action
        
    def run_cycle(self, environment_state):
        """
        Runs one full Sense-Process-Act cycle.
        """
        # 1. Sense
        state = self.sense_environment(environment_state)
        
        # 2. Process/Plan
        action = self.process_information(state)
        
        # 3. Act
        self.act(action)
        return action

# --- Simulation/Execution ---

# 1. Create the agent
my_agent = SimpleAIAgent("Agent Beta")

# 2. Define environment states (Inputs)
scenario_1 = "All clear."
scenario_2 = "Loud noise and a fire alert."
scenario_3 = "Smells like fresh food nearby."

print("## Scenario 1: All clear")
my_agent.run_cycle(scenario_1)

print("\n## Scenario 2: Danger!")
my_agent.run_cycle(scenario_2)

print("\n## Scenario 3: Reward!")
my_agent.run_cycle(scenario_3)
