import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError('List must contain nine numbers.')
  else:
    arr = np.reshape(list,(3,3))
    
    avg_results = [np.mean(arr,axis=0).tolist(),
              np.mean(arr,axis=1).tolist(),
              np.mean(arr).tolist()]
    
    var_results = [np.var(arr,axis=0).tolist(),
              np.var(arr,axis=1).tolist(),
              np.var(arr).tolist()]
    
    std_results = [np.std(arr,axis=0).tolist(),
              np.std(arr,axis=1).tolist(),
              np.std(arr).tolist()]
    
    max_results = [np.max(arr,axis=0).tolist(),
              np.max(arr,axis=1).tolist(),
              np.max(arr).tolist()]
    
    min_results = [np.min(arr,axis=0).tolist(),
              np.min(arr,axis=1).tolist(),
              np.min(arr).tolist()]
    
    sum_results = [np.sum(arr,axis=0).tolist(),
              np.sum(arr,axis=1).tolist(),
              np.sum(arr).tolist()]

    calculations = {
                    'mean': avg_results,
                    'variance':var_results,
                    'standard deviation':std_results,
                    'max': max_results,
                    'min': min_results,
                    'sum': sum_results
                    }

    return calculations