"""Example unit tests for Homework 1

Important
=========

Do not modify the way in which your solution functions are called or imported.
The actual test suite used to grade your homework will import and call your
functions in the exact same way.

"""

# the unit test module
import unittest

# some useful functions from Numpy for creating your own tests
import numpy
from numpy import sin, cos, exp, pi, dot, eye, zeros, ones, array
from numpy.linalg import norm
from numpy.random import randn

# import the homework functions
from homework1.exercise1 import collatz_step, collatz
from homework1.exercise2 import gradient_step, gradient_descent
from homework1.exercise3 import (
    decompose,
    is_sdd,
    jacobi_step,
    jacobi_iteration,
    gauss_seidel_step,
    gauss_seidel_iteration,
)

class TestExercise1(unittest.TestCase):
    """Testing the validity of

    * homework1.exercise1.collatz_step
    * homework1.exercise1.collatz

    Here we list some suggested tests you should write for your code.
    """
    def test_collatz_step(self):
        # you should probably write some tests to determine if collatz_step is
        # being correctly computed
        raise NotImplementedError() # delete this line before writing tests

    def test_collatz_step_one(self):
        # you should probably write a test to see if collatz_step handles the
        # n=1 case correctly
        raise NotImplementedError() # delete this line before writing tests

    def test_collatz_step_error(self):
        # this test has been written for you. it demonstrates how to test if a
        # function raises an error
        with self.assertRaises(ValueError):
            collatz_step(-1)
            collatz_step(-2)

    def test_collatz(self):
        # you should probably test the collatz() function against some collatz
        # sequences that you've computed by hand
        raise NotImplementedError() # delete this line before writing tests


class TestExercise2(unittest.TestCase):
    """Testing the validity of

    * homework1.exercise2.gradient_step
    * homework1.exercise2.gradient_descent

    In this problem we give less guidance on what tests you should write but
    the homework assignment document describes what we will be testing you on.
    It's up to you to write some good tests to make sure that your code works
    as intended.

    One simple test is, nonetheless, given for you.

    """
    def test_gradient_step(self):
        # this simple test determines if gradient_step is correctly computed on
        # a simple example: f(x) = x**2 - 1
        f = lambda x: x**2 - 1
        df = lambda x: 2*x
        x0 = 1
        x1 = gradient_step(x0, df, sigma=0.25)
        x1_actual = 0.5 # x0 - sigma*(2*x0)
        self.assertAlmostEqual(x1, x1_actual)


class TestExercise3(unittest.TestCase):
    """Testing the validity of

    * homework1.exercise3.decompose
    * homework1.exercise3.jacobi_step
    * homework1.exercise3.jacobi_iteration
    * homework1.exercise3.gauss_seidel_step
    * homework1.exercise3.gauss_seidel_iteration

    Some simple tests are already given for you but if you look closely they
    may not be sufficient to completely check the validity of your code since
    the example provided is too simple. A good test suite tests simple cases as
    well as more complex cases.

    """
    def test_decompose(self):
        # the test written below only tests if the identity matrix is properly
        # decomposed. this is not sufficient for testing if decompose() works
        # properly but is a good start.
        A = eye(3)
        D, L, U = decompose(A)
        D_actual = eye(3)
        L_actual = zeros((3,3))
        U_actual = zeros((3,3))

        self.assertAlmostEqual(norm(D_actual - D), 0)
        self.assertAlmostEqual(norm(L_actual - L), 0)
        self.assertAlmostEqual(norm(U_actual - U), 0)

    def test_jacobi_step(self):
        # the test written below only tests if jacobi step works in the case
        # when A is the identity matrix. In this case, jacobi_step() should
        # converge immediately the the answer. (Can you see why based on the
        # definition of Jacobi iteration?) This is not sufficient for testing
        # if jacobi_step() works properly but is a good start.
        D = eye(3)
        L = zeros((3,3))
        U = zeros((3,3))
        b = array([1,2,3])
        x0 = ones(3)
        x1 = jacobi_step(D, L, U, b, x0)

        self.assertAlmostEqual(norm(x1-b), 0)

    def test_jacobi_iteration(self):
        # the test written below only tests if jacobi iteration works in the
        # case when A is the identity matrix.
        A = eye(3)
        b = array([1,2,3])
        x0 = ones(3)
        x = jacobi_iteration(A, b, x0)

        self.assertAlmostEqual(norm(x-b), 0)



# The following code is run when this Python module / file is executed as a
# script. This happens when you enter
#
# $ python test_homework1.py
#
# in the terminal.
if __name__ == '__main__':
    unittest.main(verbosity=2) # run the above tests
