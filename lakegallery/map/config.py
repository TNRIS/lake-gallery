layers = {
    "rwpas": {
        "table_name": "rwpas",
        "label_field": "reg_name",
        "carto_css": '#layer {polygon-fill: ramp([letter], (#5F4690, #1D6996, #38A6A5, #0F8554, #73AF48, #EDAD08, #E17C05, #f7604a, #94346E, #6F4070, #94ec67, #842c00, #4cf7ec, #8c8ec4, #ffc0c0, #ffed4a, #666666), ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"), "=");}#layer::outline {line-width: 1;line-color: #FFF;line-opacity: 0.5;}',
        "interactivity": ["letter", "reg_name"]
    },
    "reservoirs": {
        "table_name": "reservoirs",
        "label_field": "res_lbl",
        "carto_css": '#layer {polygon-fill: #007ffc;polygon-opacity: 1;}#layer::outline {line-color: #FFF;line-opacity: 0.5;}',
        "interactivity": ["region", "res_lbl"]
    }
}
