import reflex as rx

avatar="https://avatars.githubusercontent.com/u/153142685?u=207430a8bb2da51294ed4adfdac839f82f536824&v=4"
def card(name:str)-> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src=avatar,
                width="100%",
                height="220px",  # Altura fija como YouTube
                object_fit="cover",  # Mantiene proporción
            ),
            side="top",
            pb="current",
        ),
        rx.text(name, font_weight="500", font_size="14px",align="center", padding="10px"),
        width="320px",  # Ancho similar a YouTube
        height="280px",  # Altura total fija
        spacing="2",
        padding="3",
        background_color="#22222249",
        border_radius="10px",
        cursor="pointer",
        _hover={"transform": "scale(1.02)", "transition": "0.2s"},
    )
