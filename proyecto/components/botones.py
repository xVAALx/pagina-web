import reflex as rx


def links(text: str, url: str , image: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(src=image,
                        margin="5px",
                        height="1.5em",
                        alt=text,
                        ),
                rx.text(
                    text,
                    text_align="start",
                    ml="8px",
                    overflow="hidden",
                    text_overflow="ellipsis",
                    white_space="nowrap",
                    flex="1",  # El texto ocupa el espacio restante
                ),
                color="white",
                width="100%",
                align="center",
            ),
            display="flex",
            width="250px",      # Ancho fijo para todos los botones
            height="48px",      # Alto fijo para todos los botones
        ),
        width="250px",          # El link también tiene el mismo ancho
        height="48px",          # El link también tiene el mismo alto
        href=url,
        is_external=True,
        text_decoration="none",
        background_color="#FFFFFF00",
        border_radius="none",
        border="none",
    )