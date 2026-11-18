import re
import pytest
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


@pytest.mark.parametrize(
    "usuario, password, mensaje_esperado",
    [
        ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
        ("standard_user", "clave_mala", "Epic sadface: Username and password do not match any user in this service"),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
    ],
    ids=["usuario_bloqueado", "password_incorrecta", "usuario_vacio", "password_vacia"],
)
def test_login_fallido(page: Page, usuario, password, mensaje_esperado):
    # 1. Abrir la página de login
    page.goto("https://www.saucedemo.com/")

    # 2. Completar con los datos de cada caso
    page.get_by_placeholder("Username").fill(usuario)
    page.get_by_placeholder("Password").fill(password)

    # 3. Intentar loguearse
    page.get_by_role("button", name="Login").click()

    # 4. Validar el mensaje de error y que NO pasamos a productos
    expect(page.locator('[data-test="error"]')).to_have_text(mensaje_esperado)
    expect(page).not_to_have_url(re.compile(r".*/inventory\.html"))