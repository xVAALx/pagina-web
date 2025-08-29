import reflex as rx

def canvas() -> rx.Component:
    return rx.box(
        rx.el.canvas(
            id="c",
            width="100%",
            height="100%",
            z_index="-9999",
            style={
                "position": "fixed",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                "background": "black",
                "z-index": "-99",
                "display": "block"
            }
        ),
        rx.script(src="/matrix.js"),
    ) 