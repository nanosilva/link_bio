import reflex as rx

def header() ->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Brais Moure", literal="xl"),
            rx.vstack(
                rx.heading("Brais Moure", size="lg"),
                rx.text(
                    "@mouredev",
                    margin_top="0px !important" #sobreescribe el margin
                ),
                align_items="start"
            )
        ),
        rx.text("""Soy ingeniero de software y actualmente trabajo como freelance full-stack developer iOS y Android.
         Además, creo contenido formativo sobre programación en redes. 
         Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!"""),
         align_items="start"
         )
         
       
    
