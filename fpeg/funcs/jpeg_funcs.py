__all__ = [
  "parse_marker",
  "mq_table",
  "dwt_coeffs",
]


def parse_marker(QCD):
  return int(QCD[:5], 2), int(QCD[5:], 2)


def mq_table():
  import numpy as np

  CXTable = [[4, 0]] + [[0, 0]] * 16 + [[3, 0], [46, 0]]
  QeH = ['5601', '3401', '1801', '0AC1', '0521', '0221', '5601', '5401', '4801', '3801', '3001', '2401', '1C01', '1601', '5601', '5401', '5101', '4801', '3801', '3401', '3001', '2801', '2401', '2201', '1C01', '1801', '1601', '1401', '1201', '1101', '0AC1', '09C1', '08A1', '0521', '0441', '02A1', '0221', '0141', '0111', '0085', '0049', '0025', '0015', '0009', '0005', '0001', '5601']
  Qe = [int(x, 16) for x in QeH]
  NMPS = [1, 2, 3, 4, 5,38, 7, 8, 9, 10, 11, 12, 13, 29, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 45, 46]
  NLPS = [1, 6, 9,12, 29, 33, 6, 14, 14, 14, 17, 18, 20, 21, 14, 14, 15, 16, 17, 18, 19, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,36, 37, 38, 39, 40, 41, 42, 43, 46]
  swit = [0] * 47
  swit[0] = 1
  swit[6] = 1
  swit[14] = 1
  PETTable = np.vstack((NMPS, NLPS, swit, Qe)).transpose()
  
  return PETTable, CXTable


def dwt_coeffs():
  dec_lo97 = [0.6029490182363579, 0.2668641184428723, -0.07822326652898785, -0.01686411844287495, 0.02674875741080976]
  dec_hi97 = [1.115087052456994, -0.5912717631142470, -0.05754352622849957, 0.09127176311424948, 0]
  rec_lo97 = [1.115087052456994, 0.5912717631142470, -0.05754352622849957, -0.09127176311424948, 0]
  rec_hi97 = [0.6029490182363579, -0.2668641184428723, -0.07822326652898785, 0.01686411844287495, 0.02674875741080976]

  db97_coeffs = [dec_lo97, dec_hi97, rec_lo97, rec_hi97]

  dec_lo53 = [6/8, 2/8, -1/8]
  dec_hi53 = [1, -1/2, 0]
  rec_lo53 = [1, 1/2, 0]
  rec_hi53 = [6/8, -2/8, -1/8]

  lg53_coeffs = [dec_lo53, dec_hi53, rec_lo53, rec_hi53]

  return db97_coeffs, lg53_coeffs