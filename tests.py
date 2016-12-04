import pytest
import numpy as np
import pandas as pd

from main import (
    entropy,
    info_gain,
    info_gain_ratio
)


@pytest.fixture
def data():

    # load data & format into matrices
    df = pd.read_csv("iris.csv", index_col=[0])
    X = df.drop("Species", axis=1).values
    y = pd.get_dummies(df["Species"]).values

    return X, y


def test_entropy(data):

    # dataset
    X, y = data

    # pure set
    assert entropy(y[:50]) == 0

    # two classes
    assert entropy(y[:100]) == 1

    # three classes
    assert np.isclose(entropy(y), [1.58496250072])
