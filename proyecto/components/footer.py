import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.el.footer(
        rx.text(
            f"© {datetime.date.today().year} Valentin Avila. Todos los derechos reservados.",
            font_size="sm",
            text_align="center",
            color="gray.500",
            width="100%",
        ),
        z_index="4",
        position="absolute",
        bottom="0",
        width="100%",
        display="flex",
    )