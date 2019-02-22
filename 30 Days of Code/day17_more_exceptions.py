
class Calculator:
    @staticmethod
    def power(n, p):
        """
            Return n to the power of p, if either n or p is positive 
            else raise an error 
        """
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
        return n ** p
