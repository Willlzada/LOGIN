import flet as ft


def main(page: ft.Page):

    AZ1 = '#041955'
    AZ2 = '#3450A1'
    AZ3 = '#97B4FF'
    RSA = '#EB06FF'

    page.title = 'Autenticator'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.resizable = False
    page.window.maximized = True

    def logar(e):
        page.remove(register)
        page.add(login)
        page.update()
        
    def registar(e):
        page.remove(login)
        page.add(register)
        page.update()

    login = ft.Column([
        ft.Container(
            bgcolor='#041955',
            width=page.window_width - 10,
            height=page.window_height - 60,
            border_radius=10,

            content=ft.Column([
                ft.Container(
                    bgcolor='#3450A1',
                    width=400,
                    height=320,
                    border_radius=10,

                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),

                            content=ft.Column([
                                ft.Text(
                                    value='Sign In',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Enter your email',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL,
                            ),

                            ft.TextField(
                                hint_text='Enter your password',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                            ),

                            ft.ElevatedButton(
                                text='Register',
                                bgcolor='#041955',
                                on_hover=ft.colors.BLUE_100,
                                width=300,
                                height=40,
                            ),

                            ft.Row([
                                ft.TextButton('Forgot account?'),
                                ft.TextButton(
                                    text='Create account',
                                    on_click=registar
                                    )
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

                        ], spacing=10),

                        ft.Row([
                            ft.IconButton(icon=ft.icons.EMAIL,
                                          icon_color='#041955'),
                            ft.IconButton(icon=ft.icons.FACEBOOK,
                                          icon_color='#041955'),
                            ft.IconButton(icon=ft.icons.TELEGRAM,
                                          icon_color='#041955'),
                        ], alignment='center')

                    ], horizontal_alignment='center')
                )
            ], horizontal_alignment='center', alignment='center')
        )
    ])

    register = ft.Column([
        ft.Container(
            bgcolor='#041955',
            width=page.window_width - 10,
            height=page.window_height - 60,
            border_radius=10,

            content=ft.Column([
                ft.Container(
                    bgcolor='#3450A1',
                    width=400,
                    height=450,
                    border_radius=10,

                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),

                            content=ft.Column([
                                ft.Text(
                                    value='Register',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='First Name',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.NAME,
                            ),

                            ft.TextField(
                                hint_text='Last Name',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.NAME,
                            ),

                            ft.TextField(
                                hint_text='Enter your email',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.EMAIL,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL,
                            ),

                            ft.TextField(
                                hint_text='Enter your number',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PHONE,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.PHONE,
                            ),

                            ft.TextField(
                                hint_text='Enter  password',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                            ),

                            ft.TextField(
                                hint_text='Enter password again',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                            ),

                            ft.ElevatedButton(
                                text='Sing-In',
                                bgcolor='#041955',
                                on_hover=ft.colors.BLUE_100,
                                width=300,
                                height=40,
                            ),

                            ft.Row([
                               # ft.TextButton('Forgot account?'),
                                ft.TextButton(
                                    text='I have a account',
                                    on_click=logar
                                    )
                            ], width=300, alignment='center')

                        ],spacing=8)


                    ], horizontal_alignment='center')
                )
            ], horizontal_alignment='center', alignment='center')
        )
    ])

    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)
