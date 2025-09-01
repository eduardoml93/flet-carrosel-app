import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLACK  # Corrigido de bfcolor e colors
    page.window.resizable = True
    page.title = 'Carrosel Interativo de Fotos'
    
    def move_backward(e):
        carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()

    def move_forward(e):
        carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()

    layout = ft.Container(
        content=ft.Column(
            controls=[
                carousel := ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Image(
                            src=f'https://picsum.photos/400/500?{num}',
                            width=400,
                            height=500,
                            fit=ft.ImageFit.COVER
                        ) for num in range(100)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.Icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
                        ft.IconButton(icon=ft.Icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
                    ]
                )
            ]
        )
    )

    page.add(layout)

if __name__ == '__main__':
    # Executa no navegador
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

