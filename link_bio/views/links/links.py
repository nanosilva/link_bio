import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Directos de lunes a viernes",
            "https://twitch.tv/mouredev"
            ),
        link_button(
            "YouTube",
            "Tutoriales semanales", 
            "https://youtube.com/@mouredev"
            ),
        link_button(
            "Youtube (canal secundario)",
            "Tutoriale semanales", 
            "https://youtube.com/@mouredev"
            ),
        link_button(
            "Discord",
            "El chat de la comunidad",
            "https://discord.gg/@mouredev"),
       
    
        title("Comunidad"),
        link_button(
            "Twitch",
            "Directos de lunes a viernes",
            "https://twitch.tv/mouredev"
            ),
        link_button(
            "YouTube",
            "Tutoriales semanales", 
            "https://youtube.com/@mouredev"
            ),
        link_button(
            "Youtube (canal secundario)",
            "Tutoriale semanales", 
            "https://youtube.com/@mouredev"
            ),
        link_button(
            "Discord",
            "El chat de la comunidad",
            "https://discord.gg/@mouredev"),
        width="100%"
    )
    