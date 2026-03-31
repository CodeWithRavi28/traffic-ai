import random
import time
import matplotlib.pyplot as plt

lanes = [random.randint(5, 20) for _ in range(4)]
q_values = [0, 0, 0, 0]
q_history = [[], [], [], []]

def choose_action(q_values, lanes):
    if random.random() < 0.3:
        return random.randint(0, 3)
    return q_values.index(max(q_values))

for step in range(20):
    print("\nStep:", step + 1)
    print("Traffic:", lanes)

    # random emergency (ambulance)
    emergency_lane = random.randint(0, 3) if random.random() < 0.3 else -1
    if emergency_lane != -1:
        print("🚑 Emergency in lane:", emergency_lane)

    action = choose_action(q_values, lanes)
    print("Green signal:", action)

    old = lanes[action]

    # traffic reduce
    reduction = random.randint(3, 7)
    lanes[action] = max(0, lanes[action] - reduction)

    reward = old - lanes[action]

    # bonus if emergency handled correctly
    if action == emergency_lane:
        reward += 10

    # penalty if ignored emergency
    if emergency_lane != -1 and action != emergency_lane:
        reward -= 5

    # update learning
    q_values[action] += 0.2 * (reward - q_values[action])

    # increase traffic in other lanes
    for i in range(4):
        if i != action:
            lanes[i] += random.randint(1, 4)

    print("Updated Traffic:", lanes)
    print("Q-values:", q_values)

    for i in range(4):
        q_history[i].append(q_values[i])

    time.sleep(1)

for i in range(4):
    plt.plot(q_history[i], label=f"Lane {i}")

plt.xlabel("Steps")
plt.ylabel("Q-values")
plt.title("Learning Behavior of Traffic AI")
plt.legend()
plt.show()


print("\nFinal learned behavior:", q_values)