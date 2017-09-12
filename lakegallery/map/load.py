import os
from django.contrib.gis.utils import LayerMapping
from .models import MajorReservoirs, RWPAs

majorreservoirs_mapping = {
    'res_name': 'RES_NAME',
    'type': 'TYPE',
    'status': 'STATUS',
    'res_lbl': 'RES_LBL',
    'region': 'Region',
    'geom': 'MULTIPOLYGON25D',
}

majorreservoirs_shp = os.path.abspath(
    os.path.join(os.path.dirname(
                 __file__), 'data',
                 '2017_Major_Reservoirs_With_Regions_WGS84.shp'),
)

rwpas_mapping = {
    'objectid': 'OBJECTID',
    'reg_name': 'REG_NAME',
    'letter': 'LETTER',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

rwpas_shp = os.path.abspath(
    os.path.join(os.path.dirname(
                 __file__), 'data',
                 'RWPAs_WGS84.shp'),
)


def run(verbose=True):
    lm = LayerMapping(
        MajorReservoirs, majorreservoirs_shp, majorreservoirs_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

    lm = LayerMapping(
        RWPAs, rwpas_shp, rwpas_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
