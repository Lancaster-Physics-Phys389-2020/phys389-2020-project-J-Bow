import pytest
import scipy.constants
from Tether import Tether
import numpy as np
import numpy.testing



#@pytest.mark.parametrize("test_input, deltaT, expected", [("Tether(np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0]),'head', 1, scipy.constants.pi/2, 1., 0., 0. )", 0.1, 0.1)])

#def test_update_alpha(test_input, deltaT, expected):
#    assert Tether.update_omega(test_input, deltaT) == expected

@pytest.mark.parametrize("test_input, expected", [(Tether(Position = [-5,-8,0]), -2.129395642138459  +scipy.constants.pi/2 ),(Tether(Position = [5,8,0]), 1.012197011 + scipy.constants.pi/2 ),(Tether([0,1,0]), scipy.constants.pi), (Tether([1,0,0]), scipy.constants.pi/2), (Tether([-1,0,0]), 3*scipy.constants.pi/2), (Tether([0,-1,0]),0)])
def test_set_theta(test_input, expected):
    assert np.allclose(Tether.set_theta(test_input), expected, rtol=1E-5)

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

@pytest.mark.parametrize("test_input, expected", [(Tether(Position = [0,-1,0]), 0 ), (Tether(Position = [1,0,0]), scipy.constants.pi/2)])
def test_update_theta(test_input, expected):
    assert Tether.update_theta(test_input, 0.1) == expected

@pytest.mark.parametrize("test_input, expected", [([Tether(Position = [4,0,0]), 0.1], [1.570796, [0,0,-0.2452900E-6]])])
def test_update_richardson(test_input, expected):
    deltaT = test_input[1]
    theta, omega = Tether.update_richardson(test_input[0], deltaT)
    assert np.allclose(theta, expected[0], rtol = 1E-5)
    assert np.allclose(omega, expected[1], rtol = 1E-5)

@pytest.mark.parametrize("test_input, expected", [(([Tether(Position = [5,0,0], C_d=0.), np.pi/2, 0]), -1.962070477E-6), ([Tether(Position = [0,-4,0], C_d=0.), 0, 0], 0), ([Tether(Position = [1,0,0], C_d=0.), np.pi/2, 0], -9.81E-6)])
def test_temp_alpha(test_input, expected):
    theta = test_input[1]
    omega = test_input[2]
    assert np.allclose(Tether.temp_alpha(test_input[0], 0.1, theta, omega), expected, rtol =5)

@pytest.mark.parametrize("test_input, expected", [(Tether(Position = [0,-1,0]), [0,[0,0,0]] ), (Tether(Position = [1,0,0]), [scipy.constants.pi/2, [0,0,-0.981] ])])
def test_update_RK(test_input, expected):
    theta, omega= Tether.update_RK(test_input, 0.1)
    assert np.allclose(theta, expected[0], rtol = 5)
    assert np.allclose(omega, expected[1], rtol = 5)

@pytest.mark.parametrize("test_input, expected", [(Tether(Position = [0,-1,0]),[0,-1,0] ), (Tether(Position = [1,0,0]), [1,0,0]), (Tether(Position = [5,8,0]), [5,8,0]), (Tether(Position = [-4,2,0]), [-4,2,0]), (Tether(Position = [0,0,0]), [0,0,0])])
def test_update_position(test_input, expected):
    assert np.allclose(Tether.update_position(test_input), expected, rtol = 1E-5)

@pytest.mark.parametrize("test_input, expected", [(Tether(Position = [0,-1,0], Velocity = [1,0,0]),[1,0,0] ), (Tether(Position = [1,0,0], Velocity = [1,0,0]), [0,0,0]), (Tether(Position = [0,-1,0], Velocity = [6,8,0]),[6,0,0] )])
def test_update_velocity(test_input, expected):
    assert np.allclose(Tether.update_velocity(test_input), expected, rtol = 1E-5)

@pytest.mark.parametrize("test_input, expected", [(Tether(Position = [0,-1,0], Velocity = [1,0,0]),0.5 ), (Tether(Position = [1,0,0], Velocity = [1,0,0]), 0), (Tether(Position = [0,-1,0], Velocity = [6,8,0]), 18. )])
def test_KE_angular(test_input, expected):
    assert np.allclose(Tether.KE_angular(test_input), expected, rtol = 1E-5)

@pytest.mark.parametrize("test_input, expected", [(Tether(Position = [0,-1,0]), - 0.062511),(Tether(Position = [0,-1,0], mass = 2.), - 2*0.062511), (Tether(Position = [1,0,0]), -0.06250180), (Tether(Position = [0,-1,0], h = 300), -0.0597 )])
def test_GPE_ang(test_input, expected):
    assert np.allclose(Tether.GPE_ang(test_input), expected, rtol = 1E-5)


@pytest.mark.parametrize("test_input, expected", [(([Tether(Position = [5,0,0], C_d=2. , A=1., h=300, v=7), 0, 2 ]), -1.0252222E-11)])
def test_Drag(test_input, expected):
    theta = test_input[1]
    omega = test_input[2]
    assert np.allclose(Tether.Drag(test_input[0], theta, omega), expected, rtol =5)

#np.allclose


