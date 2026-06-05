import random
import time

class NanoNeuralCore:
    def __init__(self):
        # AI's single "Brain Cell" or Synapse starting with zero knowledge
        self.synapse_weight = random.uniform(-1, 1)

    def think(self, data):
        # The AI makes a raw prediction based on its current brain state
        return data * self.synapse_weight

    def learn(self, input_data, correct_answer):
        # Backpropagation: AI calculates its own mistake and fixes its brain
        prediction = self.think(input_data)
        error = correct_answer - prediction
        
        # Adjusting the brain pattern (Learning Rate: 0.05)
        self.synapse_weight += error * input_data * 0.05
        return prediction, abs(error)

# --- The AI Simulation Matrix ---
print("🧠 BOOTING NANO AI NEURAL CORE...")
time.sleep(1)

ai_brain = NanoNeuralCore()
print(f"[!] AI Born with Random Brain Pattern: {ai_brain.synapse_weight:.4f}\n")
time.sleep(1)

# Mission: Convert Kilometers (KM) to Miles. 
# SECRET: The AI DOES NOT know the formula (1 KM = 0.621371 Miles).
# We will only give it raw data, and it will figure out the secret formula itself!
training_km = [10, 25, 50, 10, 5, 80]
true_miles = [6.21, 15.53, 31.06, 6.21, 3.10, 49.70]

print("⚡ COMMENCING SECRET DEEP LEARNING SEQUENCE...\n")
# The AI will train for 6 generations to become smart
for generation in range(1, 7):
    print(f"--- Generation {generation} ---")
    total_error = 0
    
    for idx in range(len(training_km)):
        km = training_km[idx]
        miles = true_miles[idx]
        
        pred, err = ai_brain.learn(km, miles)
        total_error += err
        print(f"Data: {km}KM -> AI Guessed: {pred:.2f} Miles | Mistake: {err:.2f}")
    
    print(f"⚠️ Total Brain Error in Gen {generation}: {total_error:.4f}\n")
    time.sleep(0.5)

print("🎓 AI HAS BECOME SELF-AWARE (Training Complete!)")
print(f"Hidden Synapse Formula Discovered: {ai_brain.synapse_weight:.6f}")

print("\n=======================================================")
print("🔮 TEST THE AI WITH A BRAND NEW NUMBER")
print("=======================================================")

try:
    test_km = float(input("Enter any Kilometers to test the AI's intelligence: "))
    final_result = ai_brain.think(test_km)
    print(f"\n👉 The AI predicts {test_km} KM is exactly {final_result:.2f} Miles!")
    print("Check on Google to see how accurate the AI is!")
except ValueError:
    print("❌ Critical Error: Please enter a valid number.")
