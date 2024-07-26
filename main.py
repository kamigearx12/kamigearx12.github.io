# from msilib.schema import TextStyle
from ctypes import alignment, sizeof
from math import exp
from turtle import color
from typing import Text
# from msilib.schema import ListView
import flet as ft

def main(page: ft.Page):
    page.title = "MusDev"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "RobotoBold" : "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    Block1: ft.Container = ft.Container(
        content=
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Row([
                            ft.Container(
                                content=ft.Text(
                                    "Welcome to MusDev!", 
                                    size=75,
                                    weight=ft.FontWeight.W_500, 
                                    font_family="RobotoBold",
                                    selectable=True
                                ),
                                alignment=ft.alignment.center,
                                padding=page.height / 50, #type: ignore
                                border=ft.border.all(5, color='black'),
                                border_radius=100,
                                expand=False,
                                width=page.width / 2.5, #type: ignore
                                bgcolor='white',
                                shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,5))
                            ),
                            ft.Container(
                                content=ft.Row([ft.IconButton(ft.icons.TELEGRAM, 'black',expand=False, icon_size=50),ft.IconButton(ft.icons.KEYBOARD_OPTION_KEY_OUTLINED, 'black',expand=False, icon_size=50),ft.IconButton(ft.icons.TIKTOK, 'black',expand=False, icon_size=50)], spacing=1),
                                border=ft.border.all(5, 'black'),
                                padding=page.height / 250, #type: ignore
                                expand=False,
                                width=page.width / 10, #type: ignore
                                border_radius=50,
                                bgcolor='white',
                                shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,5))
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER),
                        border=ft.border.all(5, 'black'),
                        opacity=0.7,
                        border_radius=15,
                        bgcolor='white',
                        shadow=ft.BoxShadow(color='black', blur_radius=5,spread_radius=0.5,offset=(0,5)),
                        padding=page.height / 75, #type: ignore
                        width=page.width / 1.79, #type: ignore
                    )
                ], alignment=ft.MainAxisAlignment.CENTER
            ),
        padding=page.height / 50, # type: ignore
        alignment=ft.alignment.center,
        # border=ft.border.all(5, color='blue'),
    )

    pagelist: ft.ListView = ft.ListView(
        controls=[
            Block1,ft.Divider(color='black', height=2, thickness=3, opacity=0.5, leading_indent=page.width / 5, trailing_indent=page.width / 5)#Block1    #type: ignore
        ],


    )

    page.add(ft.Column(controls=[pagelist], scroll=ft.ScrollMode.ALWAYS, expand=True, alignment=ft.MainAxisAlignment.START))

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)