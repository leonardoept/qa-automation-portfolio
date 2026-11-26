# Diario de aprendizaje

Registro de lo que aprendo mientras construyo mi portafolio de QA Automation.

## 2026-11-18 — Preparación del entorno

### Qué hice
- Revisé qué herramientas tenía instaladas con un script de PowerShell.
- Elegí un stack de herramientas oficiales (Playwright, GitHub CLI, Vercel, Codex).
- Creé mi primer CLAUDE.md para que Claude Code sepa cómo trabajar conmigo.

### Qué aprendí
- `Get-Command` sirve para saber si un programa está instalado y dónde.
- Python en `WindowsApps` puede ser el Python de la Microsoft Store o solo un acceso directo; se confirma con `python --version`.
- `winget` instala programas desde el repositorio oficial de Microsoft.
- En PowerShell, un espacio separa argumentos: si repito una ruta, la toma como dos.
- PowerShell 5.1 no lee UTF-8 por defecto: hay que usar `-Encoding UTF8`.
- En Markdown, `\` hace que un símbolo se muestre como texto (`\#` no es un título).

### Errores y cómo los resolví
- `dir $HOME $HOME\...` falló porque escribí la ruta base dos veces.
- Al copiar texto del chat se agregaron `\` delante de `#` y `-`.
- Intenté corregirlo con Ctrl+H, pero el texto de búsqueda también lo copié del chat y venía con el mismo error.
- Solución final: le di a Claude acceso a la carpeta para que escribiera los archivos directamente, sin portapapeles.

### Lección de QA
- Si un arreglo no funciona, revisá también los datos de entrada, no solo los pasos.
- El orden en que aplicás varios cambios puede alterar el resultado.

### Próximo paso
- Instalar Node.js, Bun, GitHub CLI y Claude Code.
