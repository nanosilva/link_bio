import reflex as rx
from link_bio.styles.styles import Sizes

def navbar() -> rx.Component:
    return  rx.hstack(
        rx.text(
            "MoureDev"
        ),
        position="sticky",
        bg="black",
        padding_x=Sizes.DEFAULT.value,
        padding_y=Sizes.SMALL.value,
        z_index="999",
        top="0"
    )

       
    
