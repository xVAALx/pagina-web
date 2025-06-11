import reflex as rx
from proyecto.components.navbar import navbar
from proyecto.components.canvas import canvas
from proyecto.components.header import header
from proyecto.components.botones import links
from proyecto.components.footer import footer
from proyecto.repo import repo




def index() -> rx.Component:
    return rx.box(
        navbar("iconos/ybcde.svg"),
        canvas(),
        rx.center(
            rx.vstack(
                header(),
                links("YouTube", "https://www.youtube.com/@valentinavila629", "iconos/youtube.svg"),
                links("Proyectos", "/repo", "iconos/project.svg"),
                links("Discord", "/2", "iconos/discord.svg"),
                links("GitHub", "https://github.com/xVAALx", "iconos/github.svg"),
                max_width="600px",
                width="100%",
                align="center",
                justify="center",
                margin_y="2em",
            ),
        ),
        footer(),  # Footer component
    )


app = rx.App(
    stylesheets=["/global.css"],
    style={
        rx.button: {"cursor": "pointer",
            "background_color" :"#2C282800",
            "border":"2px solid #048B2C81 ",
            "variant":"outline",
            "backdrop_filter": "blur(2px)",
            "_hover": {
                "background_color" :"#373B3775",
                },
            },
        "fontFamily": "courier",
    }
)

app.add_page(index)
app.add_page(repo)
