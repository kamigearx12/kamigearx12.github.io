# from sqlite3 import Row
import flet as ft

def main(page: ft.Page):
    page.title = "MusDev"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "RobotoBold" : "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    # def theme_changed(e):
    #     page.theme_mode = (
    #         ft.ThemeMode.DARK
    #         if page.theme_mode == ft.ThemeMode.LIGHT
    #         else ft.ThemeMode.LIGHT
    #     )
    #     titlebar[0].content = ft.Row([ft.Switch(thumb_icon=ft.icons.DARK_MODE_OUTLINED if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.DARK_MODE,on_change=theme_changed, active_color='black', active_track_color='white' if page.theme_mode == ft.ThemeMode.DARK else 'black', thumb_color='white' if page.theme_mode == ft.ThemeMode.LIGHT else "black", value=True if page.theme_mode == ft.ThemeMode.DARK else False )], spacing=1, scale=1.5, alignment=ft.MainAxisAlignment.CENTER)
    #     titlebar[0].border.top.color = 'white' if page.theme_mode == ft.ThemeMode.DARK else 'black'#type: ignore
    #     titlebar[0].bgcolor = 'black' if page.theme_mode == ft.ThemeMode.DARK else 'white'
    #     titlebar[0].shadow.color = "white" if page.theme_mode == ft.ThemeMode.DARK else 'black' #type: ignore

    #     titlebar[1].bgcolor = "black" if page.theme_mode == ft.ThemeMode.DARK else 'white'
    #     titlebar[1].shadow.color = "white" if page.theme_mode == ft.ThemeMode.DARK else 'black' #type: ignore
    #     titlebar[1].border.top.color = 'white' if page.theme_mode == ft.ThemeMode.DARK else 'black'#type: ignore

    #     titlebar[2].bgcolor = "black" if page.theme_mode == ft.ThemeMode.DARK else 'white'
    #     titlebar[2].shadow.color = "white" if page.theme_mode == ft.ThemeMode.DARK else 'black' #type: ignore
    #     titlebar[2].border.top.color = 'white' if page.theme_mode == ft.ThemeMode.DARK else 'black'#type: ignore
    #     titlebar[2].content = ft.Row([ft.IconButton(ft.icons.TELEGRAM, 'black' if page.theme_mode == ft.ThemeMode.LIGHT else 'white',expand=False, icon_size=50),ft.IconButton(ft.icons.KEYBOARD_OPTION_KEY_OUTLINED, 'black' if page.theme_mode == ft.ThemeMode.LIGHT else 'white',expand=False, icon_size=50),ft.IconButton(ft.icons.TIKTOK, 'black' if page.theme_mode == ft.ThemeMode.LIGHT else 'white',expand=False, icon_size=50)], spacing=1, alignment=ft.MainAxisAlignment.CENTER)


    #     contents[0].bgcolor = "black" if page.theme_mode == ft.ThemeMode.DARK else 'white'
    #     contents[0].shadow.color = "white" if page.theme_mode == ft.ThemeMode.DARK else 'black' #type: ignore

    #     contents[1].bgcolor = "black" if page.theme_mode == ft.ThemeMode.DARK else 'white'
    #     contents[1].shadow.color = "white" if page.theme_mode == ft.ThemeMode.DARK else 'black' #type: ignore
    #     page.update()

    titlebar = [
        ft.Container(
            # content=ft.Row([ft.Switch(thumb_icon=ft.icons.DARK_MODE_OUTLINED if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.DARK_MODE,on_change=theme_changed, active_color='black', active_track_color='white' if page.theme_mode == ft.ThemeMode.DARK else 'black', thumb_color='white' if page.theme_mode == ft.ThemeMode.LIGHT else "black", value=True if page.theme_mode == ft.ThemeMode.DARK else False )], spacing=1, scale=1.5, alignment=ft.MainAxisAlignment.CENTER),
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
                weight=ft.FontWeight.W_600, 
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
            content=ft.Row([ft.IconButton(ft.icons.TELEGRAM, 'black',expand=False, icon_size=50, tooltip="Telegram channel", on_click=lambda e: page.launch_url("https://t.me/musdev")),ft.IconButton(ft.icons.KEYBOARD_OPTION_KEY_OUTLINED, 'black',expand=False, icon_size=50, tooltip="GitHub", on_click=lambda e: page.launch_url("https://github.com/kamigearx12")),ft.IconButton(ft.icons.TIKTOK, 'black',expand=False, icon_size=50, tooltip="Tik-Tok", on_click=lambda e: page.launch_url("https://www.tiktok.com/@ilovechatrouge_"))], spacing=1, alignment=ft.MainAxisAlignment.CENTER),
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
                            titlebar[1],titlebar[2]
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

    contents = [
        ft.Container(
            content=ft.Column(
                [
                    ft.Row([
                        ft.Text(
                            "TTS to Microphone!", 
                            size=51,
                            weight=ft.FontWeight.W_400, 
                            font_family="RobotoBold",
                            selectable=True, expand=True
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Divider(15,3,'black', opacity=0.5),
                    ft.Row([
                        ft.Text(
                            "Это программа для озвучки текста через виртуальный микрофон.", 
                            size=34,
                            weight=ft.FontWeight.W_300, 
                            font_family="RobotoBold",
                            selectable=True, expand=True
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Divider(15,3,'black', opacity=0.5),
                    ft.Row([ft.IconButton(ft.icons.KEYBOARD_OPTION_KEY_OUTLINED, "black", 60, tooltip="Page on Git", on_click=lambda e: page.launch_url("https://github.com/kamigearx12/TTS-to-Microphone")),ft.IconButton(ft.icons.TELEGRAM, "black", 60, tooltip="In channel", on_click=lambda e: page.launch_url("https://t.me/musdev/41"))], spacing=-5, alignment=ft.MainAxisAlignment.END)
                ]
            ),
            # border=ft.border.all(3, "black"),
            width=600,
            padding=30,
            bgcolor='white',
            border_radius=50,
            opacity=0.7,
            shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,2))
        ),
        ft.Container(
            content=ft.Column(
                [
                    ft.Row([
                        ft.Text(
                            "Mus Telegram Bot", 
                            size=51,
                            weight=ft.FontWeight.W_400, 
                            font_family="RobotoBold",
                            selectable=True, expand=True
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Divider(15,3,'black', opacity=0.5),
                    ft.Row([
                        ft.Text(
                            "Это милый бот, который позволяет использовать действия в группе. Без рекламы и платных подписок!", 
                            size=30,
                            weight=ft.FontWeight.W_300, 
                            font_family="RobotoBold",
                            selectable=True, expand=True
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Divider(15,3,'black', opacity=0.5),
                    ft.Row([ft.IconButton(ft.icons.TELEGRAM, "black", 60, tooltip="Bot", on_click=lambda e: page.launch_url("https://t.me/musmusmusmeow_bot")),ft.IconButton(ft.icons.TELEGRAM, "black", 60, tooltip="In channel",on_click=lambda e: page.launch_url("https://t.me/musdev/20"))], spacing=-5, alignment=ft.MainAxisAlignment.END)
                ]
            ),
            # border=ft.border.all(3, "black"),
            width=600,
            padding=30,
            bgcolor='white',
            border_radius=50,
            opacity=0.7,
            shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,2))
        ),
    ]

    Block2 = ft.Column([
        ft.Divider(50,0,"white"),
        ft.Row(
            [
                ft.Text(
                    "Мои проекты:", 
                    size=51,
                    weight=ft.FontWeight.W_500, 
                    font_family="RobotoBold",
                    selectable=True
                )
            ], alignment=ft.MainAxisAlignment.CENTER, opacity=0.7
        ), 
    ])

    Block3: ft.Container = ft.Container(
        content= ft.Row(
            [
                contents[0],contents[1]
            ], spacing=50, alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=10,
        # border=ft.border.all(5, color='blue'),
    )

    pagelist: ft.ListView = ft.ListView(
        controls=[
            Block1,
            ft.Divider(color='black', height=15, thickness=3, opacity=0.5, leading_indent=450, trailing_indent=450),#Block1    #type: ignore
            Block2,
            Block3,
        ],


    )

    page.add(ft.Column(controls=[pagelist], scroll=ft.ScrollMode.ALWAYS, expand=True, alignment=ft.MainAxisAlignment.START))

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)