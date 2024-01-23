import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2014-{datetime.date.today().year} MoureDev by Brais Moure v3.",
            href="https://mouredev.com",
            is_external=True
        ),
        rx.text("BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.")
        )
        

      