from math import sqrt, sin, cos, atan, log


def lest_geo(x: float, y: float) -> (float, float):
    """
    Covert L-EST97 coordinate to WGS84. Based on converter provided by Estonian Land Board, see
        php: http://www.maaamet.ee/rr/geo-lest/files/geo-lest_function_php.txt
        vba: http://www.maaamet.ee/rr/geo-lest/files/geo-lest_function_vba.txt
    :param x: float, L-Est coordinate X, e.g. 6474000.12
    :param y: float, L-Est coordinate Y, e.g. 660999.421
    :return: tuple(float(WSG84_X), float(WSG84_Y)), e.g. (58.37674943306914, 26.7525562205706)
    """
    a = 6378137
    F = 1 / 298.257222100883
    ESQ = F + F - F * F
    B0 = (57 + 31 / 60 + 3.194148 / 3600) / 57.2957795130823
    L0 = 24 / 57.2957795130823
    FN = 6375000
    FE = 500000
    B2 = (59 + 20 / 60) / 57.2957795130823
    B1 = 58 / 57.2957795130823
    xx = x - FN
    yy = y - FE
    t0 = sqrt((1 - sin(B0)) / (1 + sin(B0)) * ((1 + sqrt(ESQ) * sin(B0)) / (1 - sqrt(ESQ) * sin(B0))) ** sqrt(ESQ))
    t1 = sqrt((1 - sin(B1)) / (1 + sin(B1)) * ((1 + sqrt(ESQ) * sin(B1)) / (1 - sqrt(ESQ) * sin(B1))) ** sqrt(ESQ))
    t2 = sqrt((1 - sin(B2)) / (1 + sin(B2)) * ((1 + sqrt(ESQ) * sin(B2)) / (1 - sqrt(ESQ) * sin(B2))) ** sqrt(ESQ))
    m1 = cos(B1) / (1 - ESQ * sin(B1) * sin(B1)) ** 0.5
    m2 = cos(B2) / (1 - ESQ * sin(B2) * sin(B2)) ** 0.5
    n1 = (log(m1) - log(m2)) / (log(t1) - log(t2))
    FF = m1 / (n1 * t1 ** n1)
    p0 = a * FF * t0 ** n1
    p = (yy * yy + (p0 - xx) * (p0 - xx)) ** 0.5
    t = (p / (a * FF)) ** (1 / n1)
    FII = atan(yy / (p0 - xx))
    LON = FII / n1 + L0
    u = (3.14159265358979 / 2) - (2 * atan(t))
    LAT = (u + (ESQ / 2 + (5 * ESQ ** 2 / 24) + (ESQ ** 3 / 12) + (13 * ESQ ** 4 / 360)) * sin(2 * u) +
           ((7 * ESQ ** 2 / 48) + (29 * ESQ ** 3 / 240) + (811 * ESQ ** 4 / 11520)) * sin(4 * u) +
           ((7 * ESQ ** 3 / 120) + (81 * ESQ ** 4 / 1120)) * sin(6 * u) + (4279 * ESQ ** 4 / 161280) * sin(8 * u))
    LAT = LAT * 57.2957795130823
    LON = LON * 57.2957795130823

    return LAT, LON
