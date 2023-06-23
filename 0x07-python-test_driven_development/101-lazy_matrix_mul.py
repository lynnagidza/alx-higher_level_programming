import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix.

    Raises:
        ValueError: If the matrices cannot be multiplied.

    """

    try:
        matrix_a = np.array(m_a)
        matrix_b = np.array(m_b)
        result = np.matmul(matrix_a, matrix_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
