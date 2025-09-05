import reflex as rx

def icon()->rx.Component:
    return 

def sidebar()->rx.Component:
    return rx.box(
        # Contenido de la sidebar
        rx.vstack(
            # Logo/Icono principal
            rx.box(
                rx.icon("home", size=24),
                rx.text("Inicio", class_name="sidebar-text"),
                class_name="sidebar-item",
                cursor="pointer",
            ),
            rx.box(
                rx.icon("folder", size=24),
                rx.text("Proyectos", class_name="sidebar-text"),
                class_name="sidebar-item",
                cursor="pointer",
            ),
            rx.box(
                rx.icon("code", size=24),
                rx.text("Repositorios", class_name="sidebar-text"),
                class_name="sidebar-item",
                cursor="pointer",
            ),
            rx.box(
                rx.icon("user", size=24),
                rx.text("Perfil", class_name="sidebar-text"),
                class_name="sidebar-item",
                cursor="pointer",
            ),
            rx.box(
                rx.icon("settings", size=24),
                rx.text("Configuración", class_name="sidebar-text"),
                class_name="sidebar-item",
                cursor="pointer",
            ),
            spacing="2",
            position="fixed",
            width="120px",
            padding="4",
            padding_top="120px",
            padding_bottom="240px",
        ),
        # Estilos de la sidebar
        class_name="sidebar",
        position="fixed",
        left="0",
        bottom="0",
        width="120px",
        top="115px",  # 🔥 CLAVE: Altura de tu navbar
        height="calc(100vh)",  # 🔥 CLAVE: Resta navbar
        z_index="100",  # Menor que navbar
        overflow="hidden",
        # Hover effect
        background="#00000000",  # Transparente inicial
        transition="all 1s ease",  # Incluye background
        padding_right="0px",
        _hover={
            "width": "200px",
            "background": "#2C282842",  # Sólido al hover
            "backdrop_filter": "blur(2px)",  # Quita el blur
},
        # CSS personalizado
        style={
            ".sidebar-text": {
                "margin-left": "16px",
                "color": "white",
                "font-size": "14px",
                "opacity": "0",
                "transition": "opacity 0.3s ease 0.1s",  # Delay para suavidad
            },
        },
    )