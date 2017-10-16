layers = {
    "rwpas": {
        "table_name": "rwpas",
        "label_field": "reg_name",
        "carto_css": '#layer {polygon-fill: ramp([letter], (#5F4690, #1D6996, #38A6A5, #0F8554, #73AF48, #EDAD08, #E17C05, #f7604a, #94346E, #6F4070, #94ec67, #842c00, #4cf7ec, #8c8ec4, #ffc0c0, #ffed4a, #666666), ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"), "=");}#layer::outline {line-width: 1;line-color: #FFF;line-opacity: 0.5;}',
        "carto_lbl": '#layer::labels {text-name: [reg_name];text-face-name: "DejaVu Sans Book";text-size: 12;text-fill: #FFFFFF;text-label-position-tolerance: 0;text-halo-radius: 1;text-halo-fill: #6f808d;text-dy: 0;text-allow-overlap: false;text-placement: point;text-placement-type: dummy;}',
        "interactivity": ["letter", "reg_name"]
    },
    "reservoirs": {
        "table_name": "reservoirs",
        "label_field": "res_lbl",
        "carto_css": '#layer{polygon-fill: ramp([story], (#005dff, #acacac), ("enabled", "disabled"), "=");polygon-opacity: 1;}#layer::outline{[story="enabled"]{line-width: 7.5;line-color: #5491f2;line-opacity: 0.5;}[story="disabled"]{line-width: 6;line-color: #515151;line-opacity: 0.2;}}#layer::outline {[story="enabled"]{line-width: 15;line-color: #c4d5f2;line-opacity: 0.5;}}',
        "carto_lbl": '#layer::labels {[story="enabled"]{text-name: [res_lbl];text-face-name: "DejaVu Sans Book";text-size: 12;text-fill: #FFFFFF;text-label-position-tolerance: 0;text-halo-radius: 1;text-halo-fill: #6f808d;text-dy: -10;text-allow-overlap: true;text-placement: point;text-placement-type: dummy;}}',
        "interactivity": ["region", "res_lbl"]
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
