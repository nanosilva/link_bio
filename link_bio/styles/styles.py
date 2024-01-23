import reflex as rx
from enum import Enum

#Constans
MAX_WIDTH = "600px"

#Sizes
#es un enum
class Sizes(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    BIG="2em"

#Styles
#para todos los botones
BASE_STYLE={
    rx.Button: {
        "width" : "100%",
        "height" : "100%",
        "display" : "block",
        "padding": Sizes.SMALL.value,
        "border_radius": Sizes.DEFAULT.value
    },
    rx.Link:{
        "text_decoration": "none",
        "_hover": {}
    }
}
#estilo personalizado para tamañp fuente boton, es un diccionario
title_style = dict(
    width="100%",
    padding_top=Sizes.DEFAULT.value
)

button_title_style = dict(
    font_size=Sizes.DEFAULT.value
)
button_body_style = dict(
    font_size=Sizes.MEDIUM.value
)

