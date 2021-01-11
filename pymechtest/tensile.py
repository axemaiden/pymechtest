"""
Tensile class definition.

Author: Tom Fleet
Created: 31/12/20
"""

from dataclasses import dataclass

from pymechtest.base import BaseMechanicalTest


@dataclass
class Tensile(BaseMechanicalTest):
    """
    Tensile test class.

    Args:
        folder (Union[Path, str]): String or Path-like folder containing
            test data.

        id_row (int): Row number of the specimen ID. Most test machines export a
            headed csv file with some metadata like date, test method name etc,
            specimen ID should be contained in this section. Defaults to 0.

        stress_col (str, optional): Name of the column containing stress data.
            If not passed, pymechtest will try to autodetect it from your data.

        strain_col (str, optional): Name of the column containing strain data.
            If not passed, pymechtest will try to autodetect it from your data.

        header (int, optional): 0-indexed row number of the table header
            (i.e. the row containing things like "Stress", "Strain", "Load" etc.).
            Defaults to 0.

        strain1 (float, optional): Lower strain bound for modulus calculation.
            Must be in %. Defaults to 0.05.

        strain2 (float, optional): Upper strain bound for modulus calculation.
            Must be in %. Defaults to 0.15.

        expect_yield (bool, optional): Whether the specimens are expected to be
            elastic to failure (False) or they are expected to have a
            yield strength (True). Defaults to True.
    """

    pass
