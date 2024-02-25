import numpy as np

def cohen_d(x, y):
    """Compute Cohen's d effect size for two groups / columns of a DataFrame.
    
    Check out the following link for more information:
    https://en.wikipedia.org/wiki/Effect_size#Cohen's_d

    Args:
        x: The first group / array of data containing the samples
        y: The second group / array of data containing the samples

    Returns:
        The value of Cohen's d effect size
    """
    mean_diff = np.mean(x) - np.mean(y)
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    pooled_std = np.sqrt(((nx-1) * np.std(x, ddof=1) ** 2 + (ny-1) * np.std(y, ddof=1) ** 2) / dof)
    return mean_diff / pooled_std