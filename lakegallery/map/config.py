layers = {
    "reservoirs_pt": {
        "table_name": "reservoirs",
        "label_field": "res_lbl",
        "carto_css": '#layer [story="enabled"] {marker-width: 10; marker-fill: #1556d7; marker-fill-opacity: 0.9; marker-allow-overlap: true; marker-line-width: 1; marker-line-color: #FFFFFF; marker-line-opacity: 1;}',
        "carto_lbl": '#layer::labels {[story="enabled"]{text-name: [res_lbl]; text-face-name: "DejaVu Sans Book";text-size: 12; text-fill: #FFFFFF; text-label-position-tolerance: 0; text-halo-radius: 1; text-halo-fill: #6f808d;text-dy: -10;text-allow-overlap: true;text-placement: point;text-placement-type: dummy;}}',
        "interactivity": ["res_lbl"],
        "carto_story_css": '#layer{[story="enabled"]{polygon-fill: #5491f2; polygon-opacity: 0.25;}[story="disabled"]{polygon-fill: #acacac;polygon-opacity: 1;}}#layer::outline{[story="enabled"]{line-width: 2;line-color: #5491f2;line-opacity: 0.4;}[story="disabled"]{line-width: 2;line-color: #515151;line-opacity: 0.2;}}'
    },
    "reservoirs": {
        "table_name": "reservoirs",
        "label_field": "res_lbl",
        "carto_css": '#layer [story="enabled"] {polygon-fill: ramp([story], (#005dff, #acacac), ("enabled", "disabled"), "="); polygon-opacity: 1;}#layer::outline{[story="enabled"]{line-width: 7.5; line-color: #5491f2; line-opacity: 0.5;}}#layer::outline {[story="enabled"]{line-width: 15;line-color: #c4d5f2;line-opacity: 0.5;}}',
        "carto_lbl": '#layer::labels {[story="enabled"]{text-name: [res_lbl]; text-face-name: "DejaVu Sans Book"; text-size: 12; text-fill: #FFFFFF; text-label-position-tolerance: 0; text-halo-radius: 1; text-halo-fill: #6f808d;text-dy: -10;text-allow-overlap: true;text-placement: point;text-placement-type: dummy;}}',
        "interactivity": ["res_lbl"],
        "carto_story_css": '#layer{[story="enabled"]{polygon-fill: #5491f2; polygon-opacity: 0.25;}[story="disabled"]{polygon-fill: #acacac; polygon-opacity: 1;}}#layer::outline{[story="enabled"]{line-width: 2;line-color: #5491f2;line-opacity: 0.4;}[story="disabled"]{line-width: 2;line-color: #515151;line-opacity: 0.2;}}'
    }
}
# overlays dict key name must equal key[toc_label] which must also equal
# the name in overlay_order
overlay_order = ["Parks", "Hazards", "Channel Markers", "Boat Ramps"]
overlays = {
    "Boat Ramps": {
        "table_name": "boatramps",
        "toc_label": "Boat Ramps",
        "carto_css": '#layer {marker-width: 7;marker-fill: #cb53ff;marker-fill-opacity: 1;marker-allow-overlap: true;marker-line-width: 1;marker-line-color: #FFFFFF;marker-line-opacity: 1;}',
        "carto_lbl": '#layer::labels {text-name: [name];text-face-name: "DejaVu Sans Book";text-size: 10;text-fill: #FFFFFF;text-label-position-tolerance: 0;text-halo-radius: 1;text-halo-fill: #6F808D;text-dy: -10;text-allow-overlap: false;text-placement: point;text-placement-type: dummy;}'
    },
    "Channel Markers": {
        "table_name": "channelmarkers",
        "toc_label": "Channel Markers",
        "carto_css": '#layer {marker-width: 7;marker-fill: #ffffff;marker-fill-opacity: 0.9;marker-allow-overlap: true;marker-line-width: 1;marker-line-color: #969696;marker-line-opacity: 1;}'
    },
    "Hazards": {
        "table_name": "hazards",
        "toc_label": "Hazards",
        "carto_css": '#layer {polygon-fill: ramp([hazard_type], (#ffcbef, #f7d27a, #e1f4a4, #c1c1c1), ("Hazard", "No Boats", "No Wake", "Rocks"), "=");polygon-opacity: 0.66;}#layer::outline {line-width: 1;line-color: #bfbfbf;line-opacity: 0.76;}'
    },
    "Parks": {
        "table_name": "parks",
        "toc_label": "Parks",
        "carto_css": '#layer {polygon-fill: #d4ffaf;polygon-opacity: 0.7;}#layer::outline {line-width: 1;line-color: #3dff4a;line-opacity: 0.5;}',
        "carto_lbl": '#layer::labels {text-name: [name];text-face-name: "DejaVu Sans Book";text-size: 10;text-fill: #FFFFFF;text-label-position-tolerance: 0;text-halo-radius: 1;text-halo-fill: #6F808D;text-dy: -10;text-allow-overlap: false;text-placement: point;text-placement-type: dummy;}'
    }
}
