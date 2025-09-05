import reflex as rx
from proyecto.components.navbar import navbar
from proyecto.components.card import card
from proyecto.components.sidebar import sidebar




def repo():
    return rx.box(
        navbar("/iconos/ybcde.svg"),
        sidebar(),
        rx.vstack(
            rx.text("Repositorio", font_size="40px", font_weight="bold", color="white"),
            rx.grid(
                card("1"),
                card("2"),
                card("3"),
                card("4"),
                card("5"),
                card("6"),
                spacing="6",
                z_index="1",
                position="relative",
                width="100%",
                justify="center",
                style={
        "grid-template-columns": "repeat(auto-fit, minmax(320px, 1fr))",
        "justify-items": "center"
    }
            ),
            spacing="6",
            align="center",
            width="100%",
            max_width="1200px",  # Límite máximo de ancho
            margin="0 auto",  # Centrar el contenido
        ),
        rx.image(
            src="/repo_background.jpg",  # Sin assets/ ni images/
            position="absolute",
            top="0",
            left="0", 
            width="100%",
            height="100%",
            object_fit="cover",
            z_index="-1",
        ),
        padding="0",
        margin="0",
        min_height="100vh",
        width="100%",
        )
