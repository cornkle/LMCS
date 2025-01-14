import os


def _create_dic(dx, dist, start, nb):

    dic = {}
    dic['dx'] = dx
    dic['dist'] = dist
    dic['start'] = start
    dic['nb'] = nb

    return dic


############ Frequently used DATASET SETUPS.
# Defines surface thresholds, data resolution and (number of) scales
# _create_dic entries as follows:
#
# (1) resolution, (2) distance between scales, (3) start scale, (4) number of scales

NAMES = {
    'SM5k': _create_dic(5, 0.25, 5, 40),  # to avoid bias in full wavelet reconstruction, (2) = 0.25 and a minimum of 35 scales is needed.
    'T_CP4': _create_dic(4.4, 1, 10, 6)
}

########## Test case data

TESTDATA = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'testdata' + os.sep + 'sm_testfile.nc'
TESTDATA_TEMP = os.path.abspath(os.path.dirname(__file__)) + os.sep + 'testdata' + os.sep + 't2_testfile.nc'
