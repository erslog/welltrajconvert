import unittest
from welltrajconvert.wellbore_trajectory import *


def compare_arrays(array_a, array_b):
    """compare array a and array b values"""
    comparison = array_a == np.array(array_b)
    return comparison.all()

class TestWellboreTrajectoryCalcLatLonPoints(unittest.TestCase):

    def test_wellbore_trajectory_calc_lat_lon_points(self):
        well_dict = {
            "wellId": "well_A",
            "md": [5000.0, 5200.0, 5400.0, 5600.55, 5800.0, 5900.0],
            "inc": [70.97, 75.88, 80.15, 85.03, 89.91, 90.97],
            "azim": [28.78, 28.53, 29.28, 27.59, 26.69, 26.72],
            "surface_latitude": 29.90829444,
            "surface_longitude": 47.68852083
        }
        # get wellbore trajectory object
        dev_obj = WellboreTrajectory(well_dict)
        dev_obj.calculate_horizontal()

        array_a = dev_obj.deviation_survey_obj.isHorizontal
        array_b = ['Vertical', 'Vertical', 'Vertical', 'Vertical', 'Horizontal','Horizontal']
        self.assertEqual(compare_arrays(array_a, array_b), True, 'isHorizontal arrays are not equal')






if __name__ == '__main__':
    unittest.main()