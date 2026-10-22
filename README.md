# 🚗 Sistema de Gestión y Mantenimiento Automotriz

**Vehículos Registrados:**
1. **Jeep Compass 2009 2.4L 4x4 CVT** (246,855 km) — Patente: `BSGG93` | VIN: `1J8FFF7W88D780073`
2. **Suzuki Alto 800 0.8L** (~120,000 km) — Motor F8D 3 Cilindros
3. **Moto Honda** (Baja cilindrada) — Mantenimiento integral

> 🌐 **Dashboard Visual Interactivo:** Abre [`index.html`](file:///home/arturo/development/jeep-compass-2009/index.html) en tu navegador para ver la bitácora visual con pestañas por vehículo, reproductor de notas de voz (.opus), galería de fotos, boletas y buscador en tiempo real.

---

## 📊 Resumen Rápido por Vehículo

| Vehículo | Kilometraje | Estado General | Última Intervención | Inversión Estimada | Archivo Detallado |
|----------|-------------|----------------|---------------------|--------------------|-------------------|
| **Jeep Compass 2009** | 246,855 km | 🟡 Operativo (A/C off) | 11 Mar 2026 (Aceite 10W40) / Jun 2026 (Correa) | ~$676.000+ CLP | [`HISTORIAL.md`](file:///home/arturo/development/jeep-compass-2009/HISTORIAL.md) |
| **Suzuki Alto 800** | ~120,000 km | ✅ Excelente (A/C 100%) | Jul 2026 (Revisión integral trenes) | ~$221.449+ CLP | [`HISTORIAL-SUZUKI-ALTO.md`](file:///home/arturo/development/jeep-compass-2009/HISTORIAL-SUZUKI-ALTO.md) |
| **Moto Honda** | - | ✅ Operativa | Ene 2026 (Carburador y escape) | $85.000 CLP | [`index.html`](file:///home/arturo/development/jeep-compass-2009/index.html) |

---

## 📁 Estructura del Repositorio

```
jeep-compass-2009/
├── index.html                               # 🌟 Dashboard interactivo (HTML + Audio + Fotos)
├── docker-compose.yml                       # 🐳 Servicio permanente en contenedor (Nginx + Cloudflare)
├── README.md                                # Visión general unificada
├── HISTORIAL.md                             # Historial detallado del Jeep Compass 2009
├── HISTORIAL-SUZUKI-ALTO.md                 # Historial detallado del Suzuki Alto 800
├── WhatsApp Chat - Mecanico Mauricio/       # Respaldo completo de chat, audios, fotos y videos
│   ├── _chat.txt                            # Registro completo de 3,477 líneas (2023 - 2026)
│   ├── *.opus                               # 200 notas de voz de WhatsApp con Mauricio
│   ├── *.jpg                                # 119 fotos (facturas, piezas, varillas, reparaciones)
│   ├── *.mp4                                # 28 videos de funcionamiento y diagnósticos
│   └── *.vcf                                # Contactos de proveedores y especialistas
├── docs/                                    # Diagnósticos técnicos y especificaciones
│   ├── mantenimiento/
│   ├── problemas/
│   └── compras/
```

---

## 🛠️ Estado Técnico por Vehículo

### 1. Jeep Compass 2009 (2.4L Dual VVT CVT)
- **Aceite y Filtro de Motor:** ✅ **Al día**. Cambiado el **11/03/2026 a los 246,855 km** con aceite Mobil **10W-40**. Próximo cambio programado en +10,000 km (a los **256,855 km**).
- **Correa Serpentina:** ✅ **Solucionado**. Correa Mopar original instalada en Junio 2026; sin desviaciones ni ruidos.
- **Climatización (A/C):** ❌ **NO FUNCIONA (INOPERATIVO - Falla Activa)**. El sistema dejó de enfriar en Octubre 2026. Requiere prueba de presión/vacío para descartar fuga o falla definitiva de compresor.
- **Transmisión CVT:** ✅ Mantenimiento integral a los 220k km con cambio de filtros y aceite CVT.
- **Tren Trasero:** ✅ Reconstrucción completa de 4 bandejas y 2 tensores reguladores traseros (eliminó ruido a 'catre viejo').
- **Tren Delantero:** ✅ Bieletas delanteras nuevas, bandeja izquierda nueva y alineación láser en Neumaval.
- **Eléctrico:** ✅ Tablero central y palanca reparados tras cortocircuito en encendedor (Ene 2026).
- **Pendiente:** Kit de termostatos duales DORMAN 902319 y control semanal de varilla de aceite.

### 2. Suzuki Alto 800 (0.8L)
- **Climatización (A/C):** ✅ **FUNCIONA SÚPER BIEN**. Sistema de enfriamiento y aire acondicionado al 100% de eficiencia, sin fugas ni anomalías.
- **Kit de Distribución & Embrague:** ✅ Realizado a los ~110k km (19 Ago 2025): Correa dentada, tensor GT-90610, termostato W-44, 3 bujías y kit de embrague completo Exedy India (Factura $124.699).
- **Frenos Delanteros:** 🟡 Pastillas al 40% de vida útil evaluadas en Julio 2026 (Factura previa $16.750).
- **Suspensión & Chasis:** ✅ Amortiguadores traseros nuevos (Oct 2024). Inspección completa en Julio 2026 determinó cero holguras en bujes, bandejas y bieletas.
- **Escape:** ✅ Reparado y soldado en Mayo 2026 tras daño por lomos de toro en Santiago.
- **Dictamen del Mecánico Mauricio:** *"Tiene todo bueno ese auto, anda súper bien... Salieron buenos esos autos, son medios inmortales"*.
- **Kit de Distribución & Embrague:** ✅ Realizado a los ~110k km (19 Ago 2025): Correa dentada, tensor GT-90610, termostato W-44, 3 bujías y kit de embrague completo Exedy India (Factura $124.699).
- **Frenos Delanteros:** 🟡 Pastillas al 40% de vida útil evaluadas en Julio 2026 (Factura previa $16.750).
- **Suspensión & Chasis:** ✅ Amortiguadores traseros nuevos (Oct 2024). Inspección completa en Julio 2026 determinó cero holguras en bujes, bandejas y bieletas.
- **Escape:** ✅ Reparado y soldado en Mayo 2026 tras daño por lomos de toro en Santiago.
- **Dictamen del Mecánico Mauricio:** *"Tiene todo bueno ese auto, anda súper bien... Salieron buenos esos autos, son medios inmortales"*.

---

## 📞 Proveedores y Contactos de Confianza

- **Mecánico Principal:** Mauricio Del Tránsito Wilson Cortez (Banco Santander Cta Cte: `000076030448`).
- **Especialista A/C:** Silverio Aire ([`00000412-Silverio Aire.vcf`](file:///home/arturo/development/jeep-compass-2009/WhatsApp%20Chat%20-%20Mecanico%20Mauricio/00000412-Silverio%20Aire.vcf)).
- **Repuestos Viña del Mar:** Comercializadora Repuestos Express Limitada, Calle San Antonio 1275, Viña del Mar ([`00000737-Repuestos Express Viña.vcf`](file:///home/arturo/development/jeep-compass-2009/WhatsApp%20Chat%20-%20Mecanico%20Mauricio/00000737-Repuestos%20Express%20Vin%CC%83a.vcf)).
- **Alineación:** Neumaval (Alineación computarizada).
- **Amortiguadores:** Rep. Amortiguadores San Antonio con 12 Norte ([`00000508-Rep Amortiguadores San Anton Con 12 Norte A La Vuelta.vcf`](file:///home/arturo/development/jeep-compass-2009/WhatsApp%20Chat%20-%20Mecanico%20Mauricio/00000508-Rep%20Amortiguadores%20San%20Anton%20Con%2012%20Norte%20A%20La%20Vuelta.vcf)).
