import numpy as np

def calculate(list):
    try:
        np.array(list).reshape(3,3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3,3)

    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            matrix.mean()
            ],

        'variance': [np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            matrix.var()
            ],
        
        'standard deviation': [np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            matrix.std()
            ],

        'max': [np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            matrix.max()
            ],
        
        'min': [np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            matrix.min()
            ],
        
        'sum': [np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            matrix.sum()
            ],

    }

    return calculations
