import flet
from flet import *
from GUI import Index

if __name__ == '__main__':
    
    def main(page: Page):
        
        page.fonts = {
            "Allura": "../assets/fonts/Allura-Regular.ttf",
            "Poppins": "../assets/fonts/Poppins-Regular.ttf"
        }
        
        page.window_title_bar_hidden = True
        page.window_prevent_close = True
        page.window_maximized = True
        page.auto_scroll = True
        page.theme_mode = flet.ThemeMode.DARK
        page.window_center()
        
        app = Index(page)
        page.add(app.app_content)
        
        page.update()
    
    flet.app(target=main)
