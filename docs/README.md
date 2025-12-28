# docs/

Directorio para almacenar documentación técnica del Jeep Compass 2009.

## 📄 Contenido Actual

### Manuales
- ✅ **2009-compass.pdf** (11.9 MB) - Manual del propietario original Chrysler LLC
  - 430+ páginas
  - Especificaciones completas del vehículo
  - Cronogramas de mantenimiento oficiales
  - Instrucciones de operación
  - Información de seguridad

### Extractos en Markdown
Ver archivo raíz del repositorio:
- [MANUAL-PROPIETARIO.md](../MANUAL-PROPIETARIO.md) - Información clave extraída

---

## 📋 Contenido Planificado

### Facturas y Recibos
Organizar por año:
```
docs/
├── facturas/
│   ├── 2024/
│   │   ├── 2024-12-12-radiador-bomba.pdf
│   │   └── 2024-xx-xx-nombre-servicio.pdf
│   └── 2025/
│       └── 2025-01-xx-termostatos.pdf
```

### Fotos del Vehículo
```
docs/
├── fotos/
│   ├── exteriores/
│   ├── interiores/
│   ├── motor/
│   └── reparaciones/
```

### Diagramas Técnicos
- `engine-diagram.pdf` - Diagrama del motor 2.4L
- `cooling-system.pdf` - Sistema de enfriamiento detallado
- `belt-routing.pdf` - Ruteo de correa serpentina
- `wiring-diagram.pdf` - Diagrama eléctrico

---

## 🔧 Cómo Agregar Documentos

### Desde Computadora

```bash
cd /Users/arturo/development/lumina/jeep-compass-2009
cp /ruta/archivo.pdf docs/facturas/2025/
git add docs/
git commit -m "docs: Add factura servicio [descripción]"
git push
```

### Desde Móvil (GitHub App)

1. Abrir repositorio en GitHub app
2. Navegar a carpeta `docs/`
3. Tap en "+" para agregar archivo
4. Seleccionar foto/archivo desde galería
5. Agregar mensaje de commit
6. Confirmar

---

## 📝 Convenciones de Nombres

**Facturas:**
- Formato: `YYYY-MM-DD-descripcion.pdf`
- Ejemplo: `2024-12-12-cambio-radiador.pdf`

**Fotos:**
- Formato: `YYYY-MM-DD-componente-descripcion.jpg`
- Ejemplo: `2024-12-28-motor-termostatos-viejos.jpg`

**Diagramas:**
- Descriptivos y específicos
- Ejemplo: `2009-compass-cooling-system-diagram.pdf`

---

## 🔍 Búsqueda de Documentos

Para encontrar documentos específicos:

```bash
# Buscar por palabra clave
find docs/ -name "*radiador*"

# Listar todo
ls -lR docs/

# Buscar dentro de PDFs (si pdfgrep instalado)
pdfgrep "termostato" docs/**/*.pdf
```

---

**Última Actualización:** 28 de Diciembre, 2024
