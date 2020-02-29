import pytest
from Tether import Tether


@pytest.mark.parametrize("test_input, deltaT, expected", [("Tether(np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0]),'head', 1, scipy.constants.pi/2, 1., 0., 0. )", 0.1, 0.1)])

def test_update_alpha(test_input, deltaT, expected):
    assert Tether.update_omega(test_input, deltaT) == expected


pytest.main()