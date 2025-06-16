import numpy as np


total_diff = []
for i in range(1,9):
    result = np.load(f'./results/knowledge_{i}.npz')
    result = dict(result)
    differences = result["scores"]
    differences = np.sum(differences, axis=0)
    print(differences.shape)
    total_diff.append(differences)

