import flet as ft

def main(page: ft.Page):
    page.title = "MusDev"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "RobotoBold" : "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        titlebar[0].content = ft.Row([ft.Switch(thumb_icon=ft.icons.DARK_MODE_OUTLINED if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.DARK_MODE,on_change=theme_changed, active_color='black', active_track_color='white' if page.theme_mode == ft.ThemeMode.DARK else 'black', thumb_color='white' if page.theme_mode == ft.ThemeMode.LIGHT else "black", value=True if page.theme_mode == ft.ThemeMode.DARK else False )], spacing=1, scale=1.5, alignment=ft.MainAxisAlignment.CENTER)
        titlebar[0].border.top.color = 'white' if page.theme_mode == ft.ThemeMode.DARK else 'black'#type: ignore
        titlebar[0].bgcolor = 'black' if page.theme_mode == ft.ThemeMode.DARK else 'white'
        titlebar[0].shadow.color = "white" if page.theme_mode == ft.ThemeMode.DARK else 'black' #type: ignore

        titlebar[1].bgcolor = "black" if page.theme_mode == ft.ThemeMode.DARK else 'white'
        titlebar[1].shadow.color = "white" if page.theme_mode == ft.ThemeMode.DARK else 'black' #type: ignore
        titlebar[1].border.top.color = 'white' if page.theme_mode == ft.ThemeMode.DARK else 'black'#type: ignore

        titlebar[2].bgcolor = "black" if page.theme_mode == ft.ThemeMode.DARK else 'white'
        titlebar[2].shadow.color = "white" if page.theme_mode == ft.ThemeMode.DARK else 'black' #type: ignore
        titlebar[2].border.top.color = 'white' if page.theme_mode == ft.ThemeMode.DARK else 'black'#type: ignore
        titlebar[2].content = ft.Row([ft.IconButton(ft.icons.TELEGRAM, 'black' if page.theme_mode == ft.ThemeMode.LIGHT else 'white',expand=False, icon_size=50),ft.IconButton(ft.icons.KEYBOARD_OPTION_KEY_OUTLINED, 'black' if page.theme_mode == ft.ThemeMode.LIGHT else 'white',expand=False, icon_size=50),ft.IconButton(ft.icons.TIKTOK, 'black' if page.theme_mode == ft.ThemeMode.LIGHT else 'white',expand=False, icon_size=50)], spacing=1, alignment=ft.MainAxisAlignment.CENTER)
        page.update()

    titlebar = [
        ft.Container(
            content=ft.Row([ft.Switch(thumb_icon=ft.icons.DARK_MODE_OUTLINED if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.DARK_MODE,on_change=theme_changed, active_color='black', active_track_color='white' if page.theme_mode == ft.ThemeMode.DARK else 'black', thumb_color='white' if page.theme_mode == ft.ThemeMode.LIGHT else "black", value=True if page.theme_mode == ft.ThemeMode.DARK else False )], spacing=1, scale=1.5, alignment=ft.MainAxisAlignment.CENTER),
            border=ft.border.all(3, 'black'),
            padding=13, #type: ignore
            expand=False,
            width=100, #type: ignore
            border_radius=50,
            bgcolor='white',
            shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,2))
        ),

        ft.Container(
            content=ft.Text(
                "Welcome to MusDev!", 
                size=51,
                weight=ft.FontWeight.W_500, 
                font_family="RobotoBold",
                selectable=True
            ),
            alignment=ft.alignment.center,
            padding=25, #type: ignore
            border=ft.border.all(3, color='black'),
            border_radius=100,
            expand=False,
            width=600, #type: ignore
            bgcolor='white',
            shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,2))
        ),

        ft.Container(
            content=ft.Row([ft.IconButton(ft.icons.TELEGRAM, 'black',expand=False, icon_size=50),ft.IconButton(ft.icons.KEYBOARD_OPTION_KEY_OUTLINED, 'black',expand=False, icon_size=50),ft.IconButton(ft.icons.TIKTOK, 'black',expand=False, icon_size=50)], spacing=1, alignment=ft.MainAxisAlignment.CENTER),
            border=ft.border.all(3, 'black'),
            padding=page.height / 250, #type: ignore
            expand=False,
            width=220, #type: ignore
            border_radius=50,
            bgcolor='white',
            shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,2))
        )
    ]

    Block1: ft.Container = ft.Container(
        content=
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row([
                            titlebar[0],titlebar[1],titlebar[2]
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=25),
                        # border=ft.border.all(5, 'black'),
                        opacity=0.7,
                        border_radius=15,
                        # bgcolor='white',
                        # shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,5)),
                        padding=2, #type: ignore
                        # width=page.width, #type: ignore
                        expand=True
                    )
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
        padding=page.height / 50, # type: ignore
        alignment=ft.alignment.center,
        # border=ft.border.all(5, color='blue'),
    )

    pagelist: ft.ListView = ft.ListView(
        controls=[
            Block1,
            ft.Divider(color='black', height=2, thickness=3, opacity=0.5, leading_indent=450, trailing_indent=450)#Block1    #type: ignore
        ],


    )

    page.add(ft.Column(controls=[pagelist], scroll=ft.ScrollMode.ALWAYS, expand=True, alignment=ft.MainAxisAlignment.START))

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)