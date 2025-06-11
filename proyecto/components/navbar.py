import reflex as rx

def navbar(image: str) -> rx.Component:
    return rx.hstack(
        rx.box(
        rx.el.span(
                rx.image(
                src=image,
                height="40px",
            ),
            ),
        rx.el.span("              "),
        rx.el.span("x", color="green"),
        rx.el.span("VAAL", color="white"),
        rx.el.span("x", color="green"),
        font_family="Bebas-Neue",
        font_weight="medium",
        font_size="50px",
        width="100%",
        ),
        rx.text(
            font_size="25px",
            height="40px",
            width="100vw",
            text_align="end",
            font_family="monospace",
            color="white",
        ),
        width="100vw",
        background="#2C282842",
        position="sticky",
        z_index="999",
        padding_x="20px",
        padding_y="20px",
        style={"backdrop_filter": "blur(2px)"},
    )