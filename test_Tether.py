import pytest
import scipy.constants
from Tether import Tether
import numpy as np



#@pytest.mark.parametrize("test_input, deltaT, expected", [("Tether(np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0]),'head', 1, scipy.constants.pi/2, 1., 0., 0. )", 0.1, 0.1)])

#def test_update_alpha(test_input, deltaT, expected):
#    assert Tether.update_omega(test_input, deltaT) == expected

@pytest.mark.parametrize("test_input, expected", [(Tether([0,1,0]), scipy.constants.pi), (Tether([1,0,0]), scipy.constants.pi/2), (Tether([-1,0,0]), 3*scipy.constants.pi/2), (Tether([0,-1,0]),0)])
def test_set_theta(test_input, expected):
    assert Tether.set_theta(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(Tether([0,1,0]), 1.),(Tether([3,4,0]), 5.), (Tether([3,-4,0]), 5.), (Tether([2.5, 6.5, 0]), 6.96419413859206)  ] )
def test_set_length(test_input, expected):
    assert Tether.set_length(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(Tether(Position=[0,1,0], Velocity=[0,0,0], Length = 1), [0,0,0]),(Tether(Position=[3,4,0], Velocity=[0,1,0], Length = 5.), [0,0,0.12]), (Tether(Position=[0,0,0], Velocity=[0,1,0], Length = 0.), [0,0,0])])
def test_set_omega(test_input, expected):
        assert np.allclose(Tether.set_omega(test_input), expected, rtol = 1E-10)

@pytest.mark.parametrize("test_input, expected", [((Tether(Position=[0,0,0], Theta=scipy.constants.pi/2)), [0.,0.,0.]), ((Tether(Position=[0,1000.,0], Theta=scipy.constants.pi)), [0.,0.,0.])] )
def test_update_alpha(test_input, expected):
    assert np.allclose(Tether.update_alpha(test_input, 0.1), expected, rtol = 1E-10)

@pytest.mark.parametrize("test_input, expected", [(Tether(Position = [1,0,0], Velocity=np.array([0,4,0]), alpha=np.array([0,0,5])), [0,0,4.5]), (Tether(Position = [1,0,0]), [0,0,0])])
def test_update_omega(test_input, expected):
    assert np.allclose(Tether.update_omega(test_input, 0.1), expected, rtol = 1E-10)


#zero error if set at [0,1,0]

#np.allclose

