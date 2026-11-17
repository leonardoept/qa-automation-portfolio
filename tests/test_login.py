import re
from playwright.sync_api import Page, expect


def test_login_exitoso(page: Page):
    # 1.Abrir la página de login
    page.goto("https://www.saucedemo.com/")

    # 2. Completar usuario y contraseña
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")    

    # 3. Hacer click en "Login"
    page.get_by_role("button", name="Login").click()

    # 4. Validar que llegamos a la página de productos
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.get_by_text("Products")).to_be_visible()