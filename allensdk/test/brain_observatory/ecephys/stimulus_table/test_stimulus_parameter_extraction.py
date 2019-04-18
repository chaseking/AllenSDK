import pytest

from allensdk.brain_observatory.ecephys.stimulus_table import (
    stimulus_parameter_extraction as spe,
)


@pytest.fixture
def stim_repr():
    return "GratingStim(autoDraw=False, autoLog=True, color=array([1., 1., 1.]), colorSpace='rgb', contrast=0.8, depth=0)"


def test_extract_const_params_from_stim_repr(stim_repr):

    expected = {
        "autoDraw": False,
        "autoLog": True,
        "color": [1.0, 1.0, 1.0],
        "colorSpace": "rgb",
        "contrast": 0.8,
        "depth": 0,
    }

    obtained = spe.extract_const_params_from_stim_repr(stim_repr)

    assert len(expected) == len(obtained)
    for key in obtained:
        assert expected[key] == obtained[key]


def test_extract_stim_class_from_repr(stim_repr):

    expected = "GratingStim"
    obtained = spe.extract_stim_class_from_repr(stim_repr)

    assert expected == obtained
