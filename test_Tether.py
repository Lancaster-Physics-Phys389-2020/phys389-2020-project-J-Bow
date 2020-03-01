import pytest
import scipy.constants
from Tether import Tether



#@pytest.mark.parametrize("test_input, deltaT, expected", [("Tether(np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0]),'head', 1, scipy.constants.pi/2, 1., 0., 0. )", 0.1, 0.1)])

#def test_update_alpha(test_input, deltaT, expected):
#    assert Tether.update_omega(test_input, deltaT) == expected

@pytest.mark.parametrize("test_input, expected", [(Tether([0,1,0]), scipy.constants.pi), (Tether([1,0,0]), scipy.constants.pi/2), (Tether([-1,0,0]), 3*scipy.constants.pi/2), (Tether([0,-1,0]),0)])
def test_set_theta(test_input, expected):
    assert Tether.set_theta(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [])


pytest.main()