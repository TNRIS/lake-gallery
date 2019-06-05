import os
from django.contrib.gis.utils import LayerMapping
from .models import (MajorReservoirs, RWPAs, BoatRamps, ChannelMarkers,
                     Hazards, Parks)

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

boatramps_mapping = {
    'lake': {'res_lbl': 'Lake'},
    'name': 'NAME',
    'operator': 'Operator',
    'geom': 'POINT',
}

boatramps_shp = os.path.abspath(
    os.path.join(os.path.dirname(
                 __file__), 'data', 'points_of_interest',
                 'lake_boat_ramps.shp'),
)

channelmarkers_mapping = {
    'lake': {'res_lbl': 'Lake'},
    'odd': 'ODD',
    'marker_id': 'MarkerID',
    'year': 'Year',
    'geom': 'POINT',
}

channelmarkers_shp = os.path.abspath(
    os.path.join(os.path.dirname(
                 __file__), 'data', 'points_of_interest',
                 'lake_channel_markers.shp'),
)

hazards_mapping = {
    'lake': {'res_lbl': 'Lake'},
    'hazard_type': 'TYPE',
    'num_buoys': 'NUM_BUOYS',
    'geom': 'POLYGON',
}

hazards_shp = os.path.abspath(
    os.path.join(os.path.dirname(
                 __file__), 'data', 'points_of_interest',
                 'lake_hazards.shp'),
)

parks_mapping = {
    'lake': {'res_lbl': 'Lake'},
    'park_type': 'TYPE',
    'name': 'NAME',
    'acres': 'ACRES',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'geom': 'POLYGON',
}

parks_shp = os.path.abspath(
    os.path.join(os.path.dirname(
                 __file__), 'data', 'points_of_interest',
                 'lake_parks.shp'),
)


def run(verbose=True):
    # lm = LayerMapping(
    #     MajorReservoirs, majorreservoirs_shp, majorreservoirs_mapping,
    #     transform=False, encoding='iso-8859-1',
    # )
    # lm.save(strict=True, verbose=verbose)

    # lm = LayerMapping(
    #     RWPAs, rwpas_shp, rwpas_mapping,
    #     transform=False, encoding='iso-8859-1',
    # )
    # lm.save(strict=True, verbose=verbose)

    lm = LayerMapping(
        BoatRamps, boatramps_shp, boatramps_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

    lm = LayerMapping(
        ChannelMarkers, channelmarkers_shp, channelmarkers_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

    lm = LayerMapping(
        Hazards, hazards_shp, hazards_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

    lm = LayerMapping(
        Parks, parks_shp, parks_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
