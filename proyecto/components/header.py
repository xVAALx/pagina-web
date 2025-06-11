import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            name="valentin avila",
            size="7",
            src="https://avatars.githubusercontent.com/u/153142685?u=207430a8bb2da51294ed4adfdac839f82f536824&v=4",
            z_index="3",
            margin="10px",
        ),
        rx.hstack(
            rx.text("@valentin avila ",font_size="2xl", text_align="center",),
            rx.text("🇦🇷",size="7", line_height="1",
        ),
            ),
        rx.text(
            "Menu de navegación",
            text_decoration="underline #048B2C81",  
            font_family="courier",
            font_size="30px",
            weight="bold",
            ),
        align_items="center",
        color="white",
    )   