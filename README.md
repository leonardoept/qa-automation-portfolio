# 🧪 QA Automation Portfolio – Playwright + Pytest

Proyecto de automatización de pruebas end-to-end sobre [SauceDemo](https://www.saucedemo.com/), una aplicación de e-commerce de práctica.
Forma parte de mi transición de QA manual a **QA Automation**, aplicando buenas prácticas de diseño de casos de prueba que uso desde hace años en testing funcional.

## 🛠️ Tecnologías
- **Python 3**
- **Playwright** (API síncrona) – automatización de navegador
- **Pytest** + **pytest-playwright** – ejecución, fixtures y parametrización
- **Git / GitHub** – control de versiones

## ✅ Casos automatizados

| Test | Tipo | Qué valida |
|---|---|---|
| `test_login_exitoso` | Positivo | Login con usuario válido redirige a la página de productos |
| `test_login_fallido[usuario_bloqueado]` | Negativo | Usuario bloqueado muestra el mensaje de error correspondiente |
| `test_login_fallido[password_incorrecta]` | Negativo | Credenciales inválidas no permiten el acceso |
| `test_login_fallido[usuario_vacio]` | Negativo | Validación de campo obligatorio: usuario |
| `test_login_fallido[password_vacia]` | Negativo | Validación de campo obligatorio: contraseña |

Los casos negativos usan `@pytest.mark.parametrize`: un único test ejecutado con distintos conjuntos de datos (técnica de partición de equivalencias).

## 📁 Estructura
```
qa-automation-portfolio/
├── pages/          # Page Objects (en construcción)
├── tests/
│   └── test_login.py
├── requirements.txt
└── README.md
```

## ▶️ Cómo ejecutarlo
```bash
git clone https://github.com/leonardoept/qa-automation-portfolio.git
cd qa-automation-portfolio
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
playwright install
pytest -v
```

Para ver el navegador durante la ejecución:
```bash
pytest -v --headed
```

## 💡 Buenas prácticas aplicadas
- Localizadores estables (`data-test`, roles y placeholders) en lugar de XPath frágiles
- Validaciones positivas **y negativas** (`to_have_url` / `not_to_have_url`)
- Esperas automáticas de Playwright (sin `sleep`)
- Casos identificados con `ids` legibles para un reporte claro
- Commits con convención (`test:`, `docs:`, `chore:`)

## 🗺️ Próximos pasos
- [ ] Page Object Model
- [ ] Tests de API con `requests`
- [ ] Validaciones de datos con SQL (PostgreSQL)
- [ ] Integración continua con GitHub Actions
- [ ] Reportes con Allure

## 👤 Autor
**Leonardo Pérez** – QA Engineer | Córdoba, Argentina

[LinkedIn](https://www.linkedin.com/in/leonardopereztesterqa)