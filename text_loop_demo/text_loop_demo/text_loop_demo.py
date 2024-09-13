"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

from reflex_text_loop import TextLoop

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    animation: str = "tween"

    @rx.var
    def loop_animation(self) -> str:
        return self.animation


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.text(
                "Welcome to ",
                TextLoop(
                    "Reflex!",
                    "Réflexe!",
                    "Reflejo!",
                    "Reflexo!",
                    "Odruch!",
                    "Αντανάκλαση!",
                    "Riflesso!",
                    "Рефлекс!",
                    "Refleks!",
                    animation=State.loop_animation,
                ),
                font_weight="600",
                size="9",
            ),
            rx.text("Select animation type", size="2"),
            rx.hstack(
                rx.button("Tween", size="2", on_click=State.set_animation("tween")),
                rx.button("Spring", size="2", on_click=State.set_animation("spring")),
                rx.button("Inertia", size="2", on_click=State.set_animation("inertia")),
                rx.button("Keyframes", size="2", on_click=State.set_animation("keyframes")),
                rx.button("Just", size="2", on_click=State.set_animation("just")),
                spacing="0.5em",

            ),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
