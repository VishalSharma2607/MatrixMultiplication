import numpy as np
import requests

# Generate matrices
A = np.random.randint(1, 10, (10, 10)).tolist()
B = np.random.randint(1, 10, (10, 10)).tolist()

# Split A
A1 = A[:5]
A2 = A[5:]

# Update with actual IP addresses
worker_1_url = "http://192.168.1.5:8001/multiply"
worker_2_url = "http://192.168.1.7:8002/multiply"

# Send tasks
response1 = requests.post(worker_1_url, json={"A_part": A1, "B": B})
response2 = requests.post(worker_2_url, json={"A_part": A2, "B": B})

C1 = response1.json()["C_part"]
C2 = response2.json()["C_part"]

# Merge
C = C1 + C2

# Output
print("\nMatrix A:")
[print(row) for row in A]

print("\nMatrix B:")
[print(row) for row in B]

print("\nMatrix C (Result):")
[print(row) for row in C]