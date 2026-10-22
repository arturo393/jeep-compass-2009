import os
import json
import urllib.parse

CHAT_DIR = "WhatsApp Chat - Mecanico Mauricio"

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Control de Mantenimiento Automotriz - Jeep Compass 2009 & Suzuki Alto 800</title>
  <style>
    :root {
      --bg-primary: #0f172a;
      --bg-secondary: #1e293b;
      --bg-card: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent-jeep: #f59e0b;
      --accent-jeep-light: #fef3c7;
      --accent-alto: #10b981;
      --accent-alto-light: #d1fae5;
      --accent-moto: #ec4899;
      --accent-blue: #38bdf8;
      --border-color: #475569;
      --badge-success: #059669;
      --badge-warning: #d97706;
      --badge-danger: #dc2626;
      --radius: 12px;
      --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    body {
      background-color: var(--bg-primary);
      color: var(--text-main);
      padding: 20px;
      line-height: 1.5;
    }

    .container {
      max-width: 1300px;
      margin: 0 auto;
    }

    /* Header */
    header {
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 24px 30px;
      margin-bottom: 24px;
      box-shadow: var(--shadow);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
    }

    .header-title h1 {
      font-size: 1.8rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .header-title p {
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-top: 4px;
    }

    .vehicle-pills {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }

    .v-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 9999px;
      font-size: 0.88rem;
      font-weight: 600;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .v-pill.jeep {
      background-color: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border-color: rgba(245, 158, 11, 0.4);
    }

    .v-pill.alto {
      background-color: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.4);
    }

    .v-pill.moto {
      background-color: rgba(236, 72, 153, 0.15);
      color: #f472b6;
      border-color: rgba(236, 72, 153, 0.4);
    }

    /* Tabs Bar */
    .tabs-nav {
      display: flex;
      gap: 8px;
      border-bottom: 2px solid var(--border-color);
      margin-bottom: 24px;
      overflow-x: auto;
      padding-bottom: 4px;
    }

    .tab-btn {
      background: none;
      border: none;
      color: var(--text-muted);
      padding: 12px 20px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      border-radius: 8px 8px 0 0;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      white-space: nowrap;
    }

    .tab-btn:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.05);
    }

    .tab-btn.active {
      color: #fff;
      border-bottom: 3px solid var(--accent-blue);
      background: rgba(56, 189, 248, 0.1);
    }

    .tab-btn.jeep.active {
      border-bottom-color: var(--accent-jeep);
      color: #fbbf24;
    }

    .tab-btn.alto.active {
      border-bottom-color: var(--accent-alto);
      color: #34d399;
    }

    /* Tab Content Panels */
    .tab-panel {
      display: none;
      animation: fadeIn 0.3s ease;
    }

    .tab-panel.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* KPIs Grid */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .kpi-card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 18px 20px;
      box-shadow: var(--shadow);
    }

    .kpi-label {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 6px;
    }

    .kpi-value {
      font-size: 1.4rem;
      font-weight: 700;
      color: #fff;
    }

    .kpi-sub {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    /* Cards & Sections */
    .section-card {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow);
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .section-header h2 {
      font-size: 1.3rem;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* Badges */
    .badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
    }

    .badge-success { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
    .badge-warning { background: rgba(245, 158, 11, 0.2); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); }
    .badge-info { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
    .badge-danger { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }

    /* Timeline */
    .timeline {
      position: relative;
      padding-left: 28px;
      margin-top: 10px;
    }

    .timeline::before {
      content: "";
      position: absolute;
      top: 0;
      bottom: 0;
      left: 8px;
      width: 2px;
      background-color: var(--border-color);
    }

    .timeline-item {
      position: relative;
      margin-bottom: 28px;
    }

    .timeline-item:last-child {
      margin-bottom: 0;
    }

    .timeline-dot {
      position: absolute;
      left: -28px;
      top: 4px;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--bg-primary);
      border: 3px solid var(--accent-blue);
    }

    .timeline-dot.jeep { border-color: var(--accent-jeep); }
    .timeline-dot.alto { border-color: var(--accent-alto); }
    .timeline-dot.moto { border-color: var(--accent-moto); }

    .timeline-card {
      background: rgba(51, 65, 85, 0.6);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 18px 20px;
      transition: transform 0.2s, border-color 0.2s;
    }

    .timeline-card:hover {
      border-color: #64748b;
      transform: translateY(-2px);
    }

    .timeline-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
      flex-wrap: wrap;
      margin-bottom: 8px;
    }

    .timeline-date {
      font-size: 0.85rem;
      font-weight: 700;
      color: #94a3b8;
    }

    .timeline-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
    }

    .timeline-cost {
      font-weight: 700;
      color: #38bdf8;
      font-size: 1rem;
      background: rgba(56, 189, 248, 0.1);
      padding: 2px 10px;
      border-radius: 6px;
    }

    .timeline-desc {
      color: #cbd5e1;
      font-size: 0.93rem;
      margin-bottom: 12px;
    }

    .media-previews {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 12px;
      padding-top: 12px;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }

    .thumb-wrapper {
      position: relative;
      cursor: pointer;
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid var(--border-color);
      width: 110px;
      height: 75px;
      background: #000;
    }

    .thumb-wrapper img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.2s;
    }

    .thumb-wrapper:hover img {
      transform: scale(1.08);
    }

    .media-pill-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-color);
      border-radius: 6px;
      font-size: 0.82rem;
      color: #38bdf8;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s;
    }

    .media-pill-link:hover {
      background: rgba(56, 189, 248, 0.15);
      color: #fff;
    }

    /* Tables */
    .table-responsive {
      overflow-x: auto;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.92rem;
    }

    th {
      background: rgba(15, 23, 42, 0.8);
      color: var(--text-muted);
      font-weight: 600;
      padding: 12px 14px;
      border-bottom: 2px solid var(--border-color);
      text-transform: uppercase;
      font-size: 0.78rem;
      letter-spacing: 0.05em;
    }

    td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-color);
      color: #e2e8f0;
    }

    tr:hover td {
      background: rgba(255, 255, 255, 0.03);
    }

    /* Audio Player Component */
    .audio-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 14px 18px;
      margin-bottom: 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .audio-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
    }

    .audio-sender {
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .audio-date {
      color: var(--text-muted);
    }

    .audio-context {
      font-size: 0.88rem;
      color: #cbd5e1;
      font-style: italic;
      background: rgba(0, 0, 0, 0.25);
      padding: 6px 10px;
      border-radius: 6px;
      border-left: 3px solid var(--accent-blue);
    }

    audio {
      width: 100%;
      height: 38px;
      outline: none;
    }

    /* Modal / Lightbox */
    .modal {
      display: none;
      position: fixed;
      z-index: 9999;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.9);
      align-items: center;
      justify-content: center;
      padding: 20px;
      flex-direction: column;
    }

    .modal.active {
      display: flex;
    }

    .modal-content {
      max-width: 90%;
      max-height: 80vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 0 30px rgba(0,0,0,0.8);
    }

    .modal-caption {
      color: #fff;
      font-size: 1rem;
      margin-top: 14px;
      text-align: center;
      max-width: 800px;
    }

    .modal-close {
      position: absolute;
      top: 20px;
      right: 25px;
      font-size: 2rem;
      color: #fff;
      cursor: pointer;
      background: rgba(255, 255, 255, 0.1);
      width: 44px;
      height: 44px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      border: none;
    }

    /* Search Box */
    .search-box {
      margin-bottom: 20px;
      position: relative;
    }

    .search-input {
      width: 100%;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 14px 20px 14px 45px;
      font-size: 0.95rem;
      color: #fff;
      outline: none;
      transition: border-color 0.2s;
    }

    .search-input:focus {
      border-color: var(--accent-blue);
    }

    .search-icon {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
    }

    /* Grid for Gallery */
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 16px;
    }

    .gallery-item {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.2s, border-color 0.2s;
    }

    .gallery-item:hover {
      transform: translateY(-3px);
      border-color: var(--accent-blue);
    }

    .gallery-thumb {
      width: 100%;
      height: 140px;
      object-fit: cover;
      display: block;
    }

    .gallery-info {
      padding: 10px 12px;
    }

    .gallery-title {
      font-size: 0.85rem;
      font-weight: 600;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .gallery-date {
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 3px;
    }

    /* Footer */
    footer {
      text-align: center;
      padding: 30px 0;
      color: var(--text-muted);
      font-size: 0.85rem;
      border-top: 1px solid var(--border-color);
      margin-top: 40px;
    }
  </style>
</head>
<body>

<div class="container">
  <!-- Header -->
  <header>
    <div class="header-title">
      <h1>🛠️ Historial Automotriz & Bitácora de Taller</h1>
      <p>Registro consolidado con WhatsApp Mecánico Mauricio (2023 - 2026): Audios, Boletas, Fotos y Trabajos</p>
    </div>
    <div class="vehicle-pills">
      <div class="v-pill jeep" onclick="switchTab('tab-jeep')">
        <span>🚗</span>
        <div>
          <div>Jeep Compass 2009</div>
          <small style="opacity: 0.8;">~235,000 km</small>
        </div>
      </div>
      <div class="v-pill alto" onclick="switchTab('tab-alto')">
        <span>🚙</span>
        <div>
          <div>Suzuki Alto 800</div>
          <small style="opacity: 0.8;">~120,000 km</small>
        </div>
      </div>
      <div class="v-pill moto" onclick="switchTab('tab-moto')">
        <span>🏍️</span>
        <div>
          <div>Moto Honda</div>
          <small style="opacity: 0.8;">Operativa</small>
        </div>
      </div>
    </div>
  </header>

  <!-- Navigation Tabs -->
  <div class="tabs-nav">
    <button class="tab-btn jeep active" onclick="switchTab('tab-jeep', this)">🚗 Jeep Compass 2.4</button>
    <button class="tab-btn alto" onclick="switchTab('tab-alto', this)">🚙 Suzuki Alto 800</button>
    <button class="tab-btn moto" onclick="switchTab('tab-moto', this)">🏍️ Moto Honda</button>
    <button class="tab-btn" onclick="switchTab('tab-costos', this)">💰 Resumen de Costos y Facturas</button>
    <button class="tab-btn" onclick="switchTab('tab-audios', this)">🎧 Notas de Voz (200 Audios)</button>
    <button class="tab-btn" onclick="switchTab('tab-galeria', this)">📸 Galería de Imágenes & Respaldo</button>
  </div>

  <!-- Search Filter -->
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" id="searchInput" class="search-input" placeholder="Buscar por palabra clave (ej: correa, embrague, aceite, compresor, frenos, pastillas, $)..." onkeyup="filterItems()">
  </div>

  <!-- ================= TAB: JEEP COMPASS ================= -->
  <div id="tab-jeep" class="tab-panel active">
    <!-- KPIs Grid -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">Kilometraje Actual</div>
        <div class="kpi-value">246,855 km</div>
        <div class="kpi-sub">Motor 2.4L Dual VVT</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Estado General</div>
        <div class="kpi-value" style="color: #fbbf24;">Operativo (A/C off)</div>
        <div class="kpi-sub">Correa Mopar instalada Jun 2026</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Inversión Documentada</div>
        <div class="kpi-value" style="color: #fbbf24;">$676.000+ CLP</div>
        <div class="kpi-sub">Mano de obra + Repuestos Viña/Santiago</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Próximo Cambio Aceite</div>
        <div class="kpi-value" style="color: #38bdf8;">256,855 km</div>
        <div class="kpi-sub">Mobil 10W-40 (+10.000 km)</div>
      </div>
    </div>

    <!-- Status Overview Table -->
    <div class="section-card">
      <div class="section-header">
        <h2>📋 Matriz de Estado de Sistemas - Jeep Compass</h2>
        <span class="badge badge-success">Actualizado 2026</span>
      </div>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Sistema</th>
              <th>Estado</th>
              <th>Última Intervención</th>
              <th>Detalles y Próxima Acción</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Correa Serpentina Accesorios</strong></td>
              <td><span class="badge badge-success">OK / Solucionado</span></td>
              <td>Junio 2026</td>
              <td>Correa elástica <strong>Mopar Original</strong> instalada por Mauricio. Se eliminó problema de desalineación post-compresor.</td>
            </tr>
            <tr>
              <td><strong>Aire Acondicionado (A/C)</strong></td>
              <td><span class="badge badge-danger">❌ No Funciona</span></td>
              <td>Octubre 2026</td>
              <td><strong>INOPERATIVO (Exclusivo Jeep Compass):</strong> Dejó de enfriar nuevamente. Requiere test de fugas de gas R134a y revisión de compresor/embrague. *(El Suzuki Alto enfría súper bien).*</td>
            </tr>
            <tr>
              <td><strong>Aceite y Filtro de Motor</strong></td>
              <td><span class="badge badge-success">Cambiado (Al día)</span></td>
              <td>11 Marzo 2026</td>
              <td><strong>Realizado a los 246.855 km</strong> con aceite Mobil 10W-40. Próximo cambio en +10.000 km (a los <strong>256.855 km</strong>). Monitoreo semanal de varilla.</td>
            </tr>
            <tr>
              <td><strong>Sistema Eléctrico & Tablero</strong></td>
              <td><span class="badge badge-success">Reparado</span></td>
              <td>Enero 2026</td>
              <td>Desarme completo de consola y tablero central por cortocircuito de encendedor; cableado saneado. Cenicero nuevo.</td>
            </tr>
            <tr>
              <td><strong>Caja de Cambios CVT</strong></td>
              <td><span class="badge badge-success">Mantención OK</span></td>
              <td>Noviembre 2025</td>
              <td>Cambio completo de aceite CVT específico y filtros. Funcionamiento suave y sin tirones.</td>
            </tr>
            <tr>
              <td><strong>Tren Trasero (Bandejas/Tensores)</strong></td>
              <td><span class="badge badge-success">Reconstruido</span></td>
              <td>Noviembre 2025</td>
              <td>4 bandejas cambiadas (2 inferiores + 2 superiores) y 2 tensores reguladores. Adiós ruido 'catre viejo'.</td>
            </tr>
            <tr>
              <td><strong>Tren Delantero & Suspensión</strong></td>
              <td><span class="badge badge-success">Alineado</span></td>
              <td>Enero 2026</td>
              <td>Bieletas delanteras nuevas + Bandeja izquierda nueva. Alineación computarizada en taller Neumaval.</td>
            </tr>
            <tr>
              <td><strong>Sistema de Refrigeración (Termostatos)</strong></td>
              <td><span class="badge badge-warning">Pendiente Preventivo</span></td>
              <td>-</td>
              <td>Kit de termostatos duales DORMAN 902319 pendiente de instalación para optimizar temperatura.</td>
            </tr>
            <tr>
              <td><strong>Consumo de Aceite Motor</strong></td>
              <td><span class="badge badge-warning">En Monitoreo</span></td>
              <td>Semanal</td>
              <td>Monitorear varilla semanalmente. No descarbonizar motor (Mauricio indica que la carbonilla sella juegos de anillos).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Timeline of Interventions -->
    <div class="section-card">
      <div class="section-header">
        <h2>⏱️ Cronología Completa de Intervenciones - Jeep Compass</h2>
      </div>
      <div class="timeline">
        <!-- Event 0 (Current Alert) -->
        <div class="timeline-item filterable">
          <div class="timeline-dot jeep" style="border-color: var(--badge-danger);"></div>
          <div class="timeline-card" style="border-left: 4px solid var(--badge-danger);">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">Octubre 2026</span>
                <h3 class="timeline-title">Falla Activa: Sistema de Aire Acondicionado (A/C) Inoperativo</h3>
                <span class="badge badge-danger">Falla Activa</span>
                <span class="badge badge-warning">Climatización</span>
              </div>
              <div class="timeline-cost" style="color: #f87171; background: rgba(239, 68, 68, 0.1);">Diagnóstico Pendiente</div>
            </div>
            <p class="timeline-desc">
              El sistema de aire acondicionado del Jeep Compass ha dejado de enfriar nuevamente. Se requiere realizar prueba de presión con nitrógeno y vacío para verificar si hubo fuga de refrigerante R134a en mangueras, condensador u O-rings, o si la falla proviene del compresor alternativo / bobina de embrague.
            </p>
          </div>
        </div>

        <!-- Event 1 (Correa) -->
        <div class="timeline-item filterable">
          <div class="timeline-dot jeep"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">18 - 19 Junio 2026</span>
                <h3 class="timeline-title">Instalación Definitiva de Correa Serpentina Mopar Original</h3>
                <span class="badge badge-success">Solución Definitiva</span>
                <span class="badge badge-info">Motor & Accesorios</span>
              </div>
              <div class="timeline-cost">~$55.000 CLP</div>
            </div>
            <p class="timeline-desc">
              Arturo compró la correa serpentina original Mopar para motor 2.4L. Mauricio la instaló en 15 minutos en su taller. El vehículo fue probado en ruta y no volvió a presentar desviaciones, vibraciones ni chirridos, cerrando de forma definitiva la dificultad con la correa tras el cambio de compresor.
            </p>
            <div class="media-previews">
              <span class="media-pill-link" onclick="openAudioModal('00003072-PHOTO-2026-06-18-18-51-59.jpg', 'Revisión en chat de mantenciones previas y coordinación de instalación de correa')">
                🖼️ Ver Detalle Chat (18-06-2026)
              </span>
            </div>
          </div>
        </div>

        <!-- Event 1.5 (Oil Change 246k km) -->
        <div class="timeline-item filterable">
          <div class="timeline-dot jeep" style="border-color: #34d399;"></div>
          <div class="timeline-card" style="border-left: 4px solid #34d399;">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">11 Marzo 2026 (246.855 km)</span>
                <h3 class="timeline-title">Cambio de Aceite de Motor (Mobil 10W-40)</h3>
                <span class="badge badge-success">Al Día</span>
                <span class="badge badge-info">Mantenimiento Periódico</span>
              </div>
              <div class="timeline-cost" style="color: #34d399; background: rgba(52, 211, 153, 0.1);">Próximo: 256.855 km</div>
            </div>
            <p class="timeline-desc">
              Cambio de aceite de motor realizado a los 246.855 km con aceite Mobil 10W-40. Próximo cambio programado a los 256.855 km (intervalo de 10.000 km).
            </p>
          </div>
        </div>

        <!-- Event 2 -->
        <div class="timeline-item filterable">
          <div class="timeline-dot jeep"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">30 Enero 2026</span>
                <h3 class="timeline-title">Gran Reparación Eléctrica, Bandeja Izquierda, Foco, Alineación Neumaval y Carga A/C</h3>
                <span class="badge badge-danger">Reparación Crítica</span>
                <span class="badge badge-info">Eléctrico / Chasis / Clima</span>
              </div>
              <div class="timeline-cost">$140.000 CLP</div>
            </div>
            <p class="timeline-desc">
              <strong>Incidente eléctrico:</strong> Cortocircuito en cenicero/12V quemó cables del ramal bajo la consola central y palanca selectora. Mauricio desarmó casi por completo el tablero central, reemplazó cables derretidos, instaló cenicero nuevo, instaló foco delantero y cambió bandeja delantera izquierda. Además niveló el compresor con golillas espaciadoras, renovó O-rings de cañerías, cargó el gas R134a ($60k) y alineó en Neumaval ($20k). Mano de obra: $60k.
            </p>
            <div class="media-previews">
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002484-PHOTO-2026-01-30-23-13-18.jpg', 'Recomendación de Mauricio: No dejar cargadores chinos conectados fijo al encendedor')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00002484-PHOTO-2026-01-30-23-13-18.jpg" alt="Consejo tablero">
              </div>
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002428-PHOTO-2026-01-30-11-03-59.jpg', 'O-rings y cañerías de compresor de aire acondicionado')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00002428-PHOTO-2026-01-30-11-03-59.jpg" alt="O-rings">
              </div>
              <span class="media-pill-link" onclick="playAudioDirect('WhatsApp Chat - Mecanico Mauricio/00002313-AUDIO-2026-01-27-17-18-04.opus', 'Mauricio informando avance de desarme de tablero central y cables')">
                🔊 Escuchar Nota de Voz (27-01-2026)
              </span>
            </div>
          </div>
        </div>

        <!-- Event 3 -->
        <div class="timeline-item filterable">
          <div class="timeline-dot jeep"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">18 Noviembre 2025</span>
                <h3 class="timeline-title">Adaptación Polea de Compresor A/C con Silverio, Flexible Nuevo y Recarga</h3>
                <span class="badge badge-warning">Climatización</span>
                <span class="badge badge-info">Aire Acondicionado</span>
              </div>
              <div class="timeline-cost">$130.000 CLP</div>
            </div>
            <p class="timeline-desc">
              El compresor alternativo traía la polea plástica fracturada. Mauricio coordinó con el tornero/especialista Silverio Aire para transplantar la polea y embrague del compresor anterior. Se fabricó manguera flexible superior a medida ($30.000), carga y pruebas de estanqueidad ($60.000) y mano de obra ($40.000).
            </p>
            <div class="media-previews">
              <span class="media-pill-link" onclick="playAudioDirect('WhatsApp Chat - Mecanico Mauricio/00001042-AUDIO-2025-11-07-21-40-10.opus', 'Audio de Mauricio explicando tema de la polea y Silverio')">
                🔊 Escuchar Nota de Voz: Polea y Embrague
              </span>
            </div>
          </div>
        </div>

        <!-- Event 4 -->
        <div class="timeline-item filterable">
          <div class="timeline-dot jeep"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">05 Noviembre 2025</span>
                <h3 class="timeline-title">Overhaul de Caja CVT, Reconstrucción de Tren Trasero y Bieletas Delanteras</h3>
                <span class="badge badge-success">Intervención Mayor</span>
                <span class="badge badge-info">Transmisión & Suspensión</span>
              </div>
              <div class="timeline-cost">$286.001 CLP</div>
            </div>
            <p class="timeline-desc">
              <strong>Mantenimiento integral:</strong> Mantención caja CVT con vaciado completo, cambio de aceite CVT y filtros ($120.000). Reemplazo de par de bieletas delanteras ($20.000). Reemplazo completo de 4 bandejas traseras (superiores e inferiores) y 2 tensores reguladores traseros ($90.000). Se eliminó por completo el ruido a catre viejo. Boleta de repuestos en Repuestos Express Viña ($56.001). Total mano de obra: $230.000 CLP (liquidado con anticipo $109k y transferencia Santander $122k).
            </p>
            <div class="media-previews">
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00001003-PHOTO-2025-11-05-13-38-47.jpg', 'Boleta Repuestos Express Viña (San Antonio 1275) - $56.001 CLP')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00001003-PHOTO-2025-11-05-13-38-47.jpg" alt="Boleta Repuestos Express">
              </div>
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00001004-PHOTO-2025-11-05-13-39-39.jpg', 'Transferencia Banco Santander a Mauricio Cortez - $56.000 CLP')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00001004-PHOTO-2025-11-05-13-39-39.jpg" alt="Transferencia anticipo">
              </div>
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00001019-PHOTO-2025-11-05-20-14-25.jpg', 'Transferencia Banco Santander Liquidación Final - $122.000 CLP')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00001019-PHOTO-2025-11-05-20-14-25.jpg" alt="Transferencia saldo">
              </div>
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00000454-PHOTO-2025-10-18-11-44-58.jpg', 'Revisando aceites de caja CVT y Mobil en mostrador')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00000454-PHOTO-2025-10-18-11-44-58.jpg" alt="Aceites">
              </div>
            </div>
          </div>
        </div>

        <!-- Event 5 -->
        <div class="timeline-item filterable">
          <div class="timeline-dot jeep"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">Mayo - Junio 2023</span>
                <h3 class="timeline-title">Diagnóstico de Tirones, Bujías de Platino, Bobina y Monitoreo de Aceite</h3>
                <span class="badge badge-info">Motor & Encendido</span>
              </div>
              <div class="timeline-cost">~$65.000 CLP</div>
            </div>
            <p class="timeline-desc">
              El vehículo experimentaba tirones. Se diagnosticaron bujías desgastadas y bobina defectuosa. Se compraron bujías NGK/Mopar de platino y bobina nueva (instaladas con dado de 16 mm largo). Mauricio recomendó controlar estrictamente el nivel de la varilla de aceite y desaconsejó descarbonizar el motor con aditivos abrasivos porque la carbonilla protege holguras en motores con más de 200k km.
            </p>
            <div class="media-previews">
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00000036-PHOTO-2023-05-01-18-54-57.jpg', 'Varilla de aceite del Jeep Compass en marca inferior (SAFE)')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00000036-PHOTO-2023-05-01-18-54-57.jpg" alt="Varilla de aceite">
              </div>
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00000213-PHOTO-2023-05-31-12-23-16.jpg', 'Bobina de encendido nueva')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00000213-PHOTO-2023-05-31-12-23-16.jpg" alt="Bobina">
              </div>
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00000229-PHOTO-2023-06-09-16-51-01.jpg', 'Dado 16 largo con extensión para bujías')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00000229-PHOTO-2023-06-09-16-51-01.jpg" alt="Dado bujías">
              </div>
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00000294-PHOTO-2023-07-08-11-35-46.jpg', 'Filtro de aire y polen Mopar')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00000294-PHOTO-2023-07-08-11-35-46.jpg" alt="Filtros Mopar">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= TAB: SUZUKI ALTO ================= -->
  <div id="tab-alto" class="tab-panel">
    <!-- KPIs Grid -->
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">Kilometraje Actual</div>
        <div class="kpi-value">~120,000 km</div>
        <div class="kpi-sub">Motor F8D 0.8L (3 Cilindros)</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Estado Técnico</div>
        <div class="kpi-value" style="color: #34d399;">Excelente ✅</div>
        <div class="kpi-sub">"Medios inmortales" - Mauricio</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Inversión Documentada</div>
        <div class="kpi-value" style="color: #34d399;">$221.449+ CLP</div>
        <div class="kpi-sub">Distribución, embrague, suspensión, frenos</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Pastillas de Freno</div>
        <div class="kpi-value" style="color: #fbbf24;">40% Restante</div>
        <div class="kpi-sub">Próxima revisión a los 130.000 km</div>
      </div>
    </div>

    <!-- Status Overview Table -->
    <div class="section-card">
      <div class="section-header">
        <h2>📋 Matriz de Mantenimiento - Suzuki Alto 800</h2>
        <span class="badge badge-success">Chequeado Julio 2026</span>
      </div>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Componente / Sistema</th>
              <th>Estado</th>
              <th>Última Intervención</th>
              <th>Detalle Realizado</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Kit de Distribución & Tensor</strong></td>
              <td><span class="badge badge-success">Nuevo / Al día</span></td>
              <td>19 Ago 2025 (~110k km)</td>
              <td>Correa distribución 106x25 y tensor GT-90610 nuevos (Factura $124.699).</td>
            </tr>
            <tr>
              <td><strong>Kit de Embrague Completo</strong></td>
              <td><span class="badge badge-success">Nuevo / Al día</span></td>
              <td>19 Ago 2025 (~110k km)</td>
              <td>Prensa, disco Exedy India y rodamiento RCT 283 nuevos. Suavidad total de acople.</td>
            </tr>
            <tr>
              <td><strong>Termostato de Refrigeración</strong></td>
              <td><span class="badge badge-success">Nuevo</span></td>
              <td>19 Ago 2025 (~110k km)</td>
              <td>Termostato excéntrico W-44-SC-82 reemplazado preventivamente.</td>
            </tr>
            <tr>
              <td><strong>Bujías de Encendido</strong></td>
              <td><span class="badge badge-success">Inspeccionadas OK</span></td>
              <td>Julio 2026</td>
              <td>3 bujías XU-22EPR-U colocadas a los 110k km, revisadas limpias y con buena calibración.</td>
            </tr>
            <tr>
              <td><strong>Amortiguadores Traseros</strong></td>
              <td><span class="badge badge-success">Buen Estado</span></td>
              <td>Octubre 2024</td>
              <td>Par de amortiguadores traseros nuevos comprados en RC Repuestocenter MercadoLibre.</td>
            </tr>
            <tr>
              <td><strong>Tren Trasero (Bujes / Bieletas / Bandejas)</strong></td>
              <td><span class="badge badge-success">Cero Holguras</span></td>
              <td>Julio 2026</td>
              <td>Inspección exhaustiva de tren rodaje por Mauricio; bujes y anclajes en perfecto estado.</td>
            </tr>
            <tr>
              <td><strong>Tren Delantero & Dirección</strong></td>
              <td><span class="badge badge-success">Sin Juego</span></td>
              <td>Julio 2026</td>
              <td>Bandejas, rótulas y terminales firmes. Rodaje suave.</td>
            </tr>
            <tr>
              <td><strong>Pastillas de Freno Delanteras</strong></td>
              <td><span class="badge badge-warning">40% Vida Útil</span></td>
              <td>Julio 2026</td>
              <td>Pastillas DG-12257 instaladas en Ago 2025; desgastadas a un 60%, aguantan hasta 130k km.</td>
            </tr>
            <tr>
              <td><strong>Aire Acondicionado (A/C)</strong></td>
              <td><span class="badge badge-success">✅ Funciona Súper Bien</span></td>
              <td>Al día</td>
              <td><strong>100% Operativo:</strong> Enfría excelente, compresor silencioso y sin pérdidas de gas. *(A diferencia del Jeep, el Alto no presenta fallas de A/C).*</td>
            </tr>
            <tr>
              <td><strong>Tubo de Escape</strong></td>
              <td><span class="badge badge-success">Reparado</span></td>
              <td>Mayo 2026</td>
              <td>Soldadura en toma de gases y reemplazo de gomas de sujeción dañadas por lomos de toro.</td>
            </tr>
            <tr>
              <td><strong>Tapiz y Limpieza Interior</strong></td>
              <td><span class="badge badge-success">Impecable</span></td>
              <td>Julio 2026</td>
              <td>Lavado integral de tapiz en taller de Mauricio ("quedó joyita").</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Alto Timeline -->
    <div class="section-card">
      <div class="section-header">
        <h2>⏱️ Cronología de Trabajos Realizados - Suzuki Alto 800</h2>
      </div>
      <div class="timeline">
        <!-- Event 0 (Current Alert) -->
        <div class="timeline-item filterable">
          <div class="timeline-dot jeep" style="border-color: var(--badge-danger);"></div>
          <div class="timeline-card" style="border-left: 4px solid var(--badge-danger);">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">Octubre 2026</span>
                <h3 class="timeline-title">Falla Activa: Sistema de Aire Acondicionado (A/C) Inoperativo</h3>
                <span class="badge badge-danger">Falla Activa</span>
                <span class="badge badge-warning">Climatización</span>
              </div>
              <div class="timeline-cost" style="color: #f87171; background: rgba(239, 68, 68, 0.1);">Diagnóstico Pendiente</div>
            </div>
            <p class="timeline-desc">
              El sistema de aire acondicionado del Jeep Compass ha dejado de enfriar nuevamente. Se requiere realizar prueba de presión con nitrógeno y vacío para verificar si hubo fuga de refrigerante R134a en mangueras, condensador u O-rings, o si la falla proviene del compresor alternativo / bobina de embrague.
            </p>
          </div>
        </div>

        <!-- Event 1 -->
        <div class="timeline-item filterable">
          <div class="timeline-dot alto"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">01 - 14 Julio 2026 (~120,000 km)</span>
                <h3 class="timeline-title">Inspección Exhaustiva de Suspensión, Chasis, Frenos y Lavado de Tapiz</h3>
                <span class="badge badge-success">Puesta a Punto Completa</span>
                <span class="badge badge-info">Chasis & Suspensión</span>
              </div>
              <div class="timeline-cost">$80.000 CLP (Mano de Obra)</div>
            </div>
            <p class="timeline-desc">
              Arturo dejó el auto con Mauricio ante ruidos y dudas de amortiguación (Mauricio le prestó su Suzuki Aerio mientras duraba el trabajo). Mauricio realizó un peritaje completo:
              <br>• <strong>Tren trasero:</strong> bandejas, bujes, estabilizadores, bieletas y amortiguadores firmes sin juego.
              <br>• <strong>Tren delantero:</strong> 100% operativo sin holguras.
              <br>• <strong>Frenos:</strong> pastillas delanteras al 40% de vida útil restante.
              <br>• <strong>Motor:</strong> bujías y filtros revisados limpios y operativos.
              <br>• <strong>Estética:</strong> lavado profundo de tapiz y carrocería.
              <br><em>Veredicto de Mauricio: "Tiene todo bueno ese auto, anda súper bien... me sigo convenciendo que los Suzukis son mal negocio para los mecánicos: son medios inmortales."</em>
            </p>
            <div class="media-previews">
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00003172-PHOTO-2026-06-19-15-19-38.jpg', 'Recepción del Suzuki Alto en el taller de Mauricio (19-Jun-2026)')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00003172-PHOTO-2026-06-19-15-19-38.jpg" alt="Taller Mauricio">
              </div>
              <span class="media-pill-link" onclick="playAudioDirect('WhatsApp Chat - Mecanico Mauricio/00003252-AUDIO-2026-07-02-17-34-04.opus', 'Mauricio informando que el Suzuki Alto está listo y en perfecto estado')">
                🔊 Audio: Reporte de Tren Trasero y Rodaje
              </span>
              <span class="media-pill-link" onclick="playAudioDirect('WhatsApp Chat - Mecanico Mauricio/00003254-AUDIO-2026-07-02-17-37-14.opus', 'Mauricio coordinando entrega y felicitando el estado del Alto')">
                🔊 Audio: Coordinación de Entrega
              </span>
            </div>
          </div>
        </div>

        <!-- Event 2 -->
        <div class="timeline-item filterable">
          <div class="timeline-dot alto"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">25 - 26 Mayo 2026</span>
                <h3 class="timeline-title">Reparación de Tubo de Escape por Lomos de Toro y Chequeo de Historial</h3>
                <span class="badge badge-warning">Escape</span>
                <span class="badge badge-info">Escape / Soportes</span>
              </div>
              <div class="timeline-cost">Taller Local Santiago</div>
            </div>
            <p class="timeline-desc">
              En Santiago, el tubo de escape se desprendió tras cruzar lomos de toro. Se cortaron las gomas de soporte; se soldó la toma de gases y se cambiaron las gomas de sujeción. Arturo consultó a Mauricio para recordar qué se le había hecho preventivamente al llegar a los 100k km. Mauricio revisó su archivo de respaldos y le confirmó que la distribución y embrague ya estaban hechos el año anterior (evitando gastos duplicados innecesarios).
            </p>
            <div class="media-previews">
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002895-PHOTO-2026-05-26-19-50-37.jpg', 'Compra anterior de amortiguadores traseros en Mercado Libre')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00002895-PHOTO-2026-05-26-19-50-37.jpg" alt="Amortiguadores Alto">
              </div>
            </div>
          </div>
        </div>

        <!-- Event 3 -->
        <div class="timeline-item filterable">
          <div class="timeline-dot alto"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">19 Agosto 2025 (~110,000 km)</span>
                <h3 class="timeline-title">Gran Overhaul: Kit Distribución, Embrague Exedy, Termostato, Bujías y Pastillas</h3>
                <span class="badge badge-success">Overhaul Mayor</span>
                <span class="badge badge-info">Motor & Transmisión</span>
              </div>
              <div class="timeline-cost">$141.449 CLP (Repuestos)</div>
            </div>
            <p class="timeline-desc">
              Mantenimiento mayor que dejó el tren motriz impecable:
              <br>• <strong>Factura 1 ($124.699 CLP):</strong> Correa Distribución 106x25 ($12.185), Tensor GT-90610 ($12.269), Termostato W-44-SC-82 ($10.756), 3 Bujías XU-22EPR-U ($10.083), Kit Prensa y Disco Embrague Exedy India ($44.538), Rodamiento Embrague RCT 283 ($14.958) + IVA ($19.910).
              <br>• <strong>Factura 2 ($16.750 CLP):</strong> Juego de pastillas de freno delantero DG-12257 ($14.076 + IVA $2.674).
            </p>
            <div class="media-previews">
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002908-PHOTO-2026-05-26-20-04-50.jpg', 'Factura Oficial: Kit Distribución, Embrague Exedy, Termostato y Bujías ($124.699)')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00002908-PHOTO-2026-05-26-20-04-50.jpg" alt="Factura Distribución y Embrague">
              </div>
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002909-PHOTO-2026-05-26-20-04-51.jpg', 'Factura Oficial: Juego de Pastillas de Freno Delantero ($16.750)')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00002909-PHOTO-2026-05-26-20-04-51.jpg" alt="Factura Pastillas Alto">
              </div>
            </div>
          </div>
        </div>

        <!-- Event 4 -->
        <div class="timeline-item filterable">
          <div class="timeline-dot alto"></div>
          <div class="timeline-card">
            <div class="timeline-top">
              <div>
                <span class="timeline-date">29 Octubre 2024</span>
                <h3 class="timeline-title">Compra de Par de Amortiguadores Traseros Nuevos</h3>
                <span class="badge badge-info">Suspensión</span>
              </div>
              <div class="timeline-cost">Compra MercadoLibre</div>
            </div>
            <p class="timeline-desc">
              Compra en la tienda oficial RC Repuestocenter del par de amortiguadores traseros para Suzuki Alto 800 (años 2013-2019) para sustituir las piezas originales fatigadas.
            </p>
            <div class="media-previews">
              <div class="thumb-wrapper" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002895-PHOTO-2026-05-26-19-50-37.jpg', 'Comprobante de compra en Mercado Libre')">
                <img src="WhatsApp Chat - Mecanico Mauricio/00002895-PHOTO-2026-05-26-19-50-37.jpg" alt="Compra Shocks">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= TAB: MOTO HONDA ================= -->
  <div id="tab-moto" class="tab-panel">
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-label">Vehículo</div>
        <div class="kpi-value">Moto Honda</div>
        <div class="kpi-sub">Baja cilindrada</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Estado</div>
        <div class="kpi-value" style="color: #34d399;">Operativa ✅</div>
        <div class="kpi-sub">Ajustes de chasis y ruedas</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-label">Inversión Documentada</div>
        <div class="kpi-value" style="color: #ec4899;">$85.000 CLP</div>
        <div class="kpi-sub">Escape, llanta, cámara, pernos</div>
      </div>
    </div>

    <div class="section-card">
      <div class="section-header">
        <h2>🏍️ Mantenimiento Moto Honda - 17 Noviembre 2025</h2>
        <span class="badge badge-success">Finalizado</span>
      </div>
      <p style="margin-bottom: 16px; color: #cbd5e1;">
        Mauricio realizó una mantención integral de seguridad y ciclística para la moto Honda:
      </p>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Ítem de Trabajo</th>
              <th>Detalle Técnico</th>
              <th>Costo (CLP)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Regulación de Rayos Llanta</strong></td>
              <td>Enviado a taller especializado de llantas por desviación excesiva de rayos.</td>
              <td>$20.000</td>
            </tr>
            <tr>
              <td><strong>Desmontaje & Montaje Neumático</strong></td>
              <td>Desarme de rueda para cambio de cámara y centrado.</td>
              <td>$5.000</td>
            </tr>
            <tr>
              <td><strong>Cámara Nueva</strong></td>
              <td>Sustitución de cámara quemada / dañada por roce.</td>
              <td>$8.000</td>
            </tr>
            <tr>
              <td><strong>Empaquetadura de Escape</strong></td>
              <td>Reparación de fuga de escape, nueva empaquetadura y centrado del tubo.</td>
              <td>$2.000</td>
            </tr>
            <tr>
              <td><strong>Chasis, Transmisión & Pernos</strong></td>
              <td>Reapriete pernos basculante suelto, cambio completo de pernos de catalina, regulación eje rueda trasera y chequeo de balatas y cadena.</td>
              <td>-</td>
            </tr>
            <tr>
              <td><strong>Mano de Obra Mecánico Mauricio</strong></td>
              <td>Ajustes generales, desarme, centrado y puesta a punto.</td>
              <td>$50.000</td>
            </tr>
            <tr style="font-weight: 700; background: rgba(255, 255, 255, 0.05);">
              <td colspan="2">TOTAL INVERSIÓN MOTO HONDA</td>
              <td style="color: #38bdf8;">$85.000 CLP</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="section-card">
      <div class="section-header">
        <h2>🛠️ Limpieza de Carburador - 05 Enero 2026</h2>
      </div>
      <p style="margin-bottom: 16px; color: #cbd5e1;">
        Limpieza de carburador, chiclés de baja y alta, y verificación de paso en llave de combustible del estanque.
      </p>
      <div class="gallery-grid">
        <div class="gallery-item" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00001927-PHOTO-2026-01-05-18-04-56.jpg', 'Desarme y limpieza de carburador')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00001927-PHOTO-2026-01-05-18-04-56.jpg" alt="Carburador">
          <div class="gallery-info">
            <div class="gallery-title">Limpieza de Carburador</div>
            <div class="gallery-date">05 Enero 2026</div>
          </div>
        </div>
        <div class="gallery-item" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00001930-PHOTO-2026-01-05-18-11-09.jpg', 'Revisión paso de combustible y conductos')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00001930-PHOTO-2026-01-05-18-11-09.jpg" alt="Conductos admisión">
          <div class="gallery-info">
            <div class="gallery-title">Admisión & Mangueras</div>
            <div class="gallery-date">05 Enero 2026</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= TAB: COSTOS Y FACTURAS ================= -->
  <div id="tab-costos" class="tab-panel">
    <div class="section-card">
      <div class="section-header">
        <h2>💰 Consolidado General de Inversiones (2023 - 2026)</h2>
      </div>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Vehículo</th>
              <th>Detalle del Trabajo / Repuesto</th>
              <th>Tipo</th>
              <th>Monto (CLP)</th>
              <th>Comprobante</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Jun 2026</td>
              <td><span class="badge badge-warning">Jeep Compass</span></td>
              <td>Correa serpentina elástica Mopar original + Instalación</td>
              <td>Repuesto + Mano Obra</td>
              <td>~$55.000</td>
              <td>Chat Wsp</td>
            </tr>
            <tr>
              <td>Jul 2026</td>
              <td><span class="badge badge-success">Suzuki Alto</span></td>
              <td>Revisión completa tren trasero/delantero, frenos, bujías + lavado tapiz</td>
              <td>Mano de Obra</td>
              <td>$80.000</td>
              <td>Cobro Mauricio</td>
            </tr>
            <tr>
              <td>Ene 2026</td>
              <td><span class="badge badge-warning">Jeep Compass</span></td>
              <td>Reparación eléctrica tablero, bandeja izq, foco, alineación Neumaval y carga A/C</td>
              <td>Reparación Completa</td>
              <td>$140.000</td>
              <td>Carga A/C + Neumaval</td>
            </tr>
            <tr>
              <td>Nov 2025</td>
              <td><span class="badge badge-warning">Jeep Compass</span></td>
              <td>Adaptación polea compresor A/C con Silverio, flexible nuevo y carga A/C</td>
              <td>A/C Especializado</td>
              <td>$130.000</td>
              <td>Cobro Mauricio</td>
            </tr>
            <tr>
              <td>Nov 2025</td>
              <td><span class="badge badge-warning">Jeep Compass</span></td>
              <td>Mantención caja CVT, bieletas delanteras, 4 bandejas y 2 tensores traseros</td>
              <td>Mano de Obra</td>
              <td>$230.000</td>
              <td>Transferencias Santander</td>
            </tr>
            <tr>
              <td>Oct 2025</td>
              <td><span class="badge badge-warning">Jeep Compass</span></td>
              <td>Repuestos Express Viña (San Antonio 1275) - Bieletas / Fluidos</td>
              <td>Repuestos</td>
              <td>$56.001</td>
              <td>Boleta 004776</td>
            </tr>
            <tr>
              <td>Nov 2025</td>
              <td><span class="badge badge-danger">Moto Honda</span></td>
              <td>Reparación escape, centrado llanta, cámara nueva, pernos catalina</td>
              <td>Mano Obra + Repuestos</td>
              <td>$85.000</td>
              <td>Detalle Mauricio</td>
            </tr>
            <tr>
              <td>Ago 2025</td>
              <td><span class="badge badge-success">Suzuki Alto</span></td>
              <td>Kit distribución, tensor, termostato, 3 bujías, kit embrague Exedy India</td>
              <td>Repuestos Oficiales</td>
              <td>$124.699</td>
              <td>Factura con Voucher</td>
            </tr>
            <tr>
              <td>Ago 2025</td>
              <td><span class="badge badge-success">Suzuki Alto</span></td>
              <td>Juego pastillas de freno delantero DG-12257</td>
              <td>Repuestos Oficiales</td>
              <td>$16.750</td>
              <td>Factura Oficial</td>
            </tr>
            <tr>
              <td>Oct 2024</td>
              <td><span class="badge badge-success">Suzuki Alto</span></td>
              <td>Par amortiguadores traseros Suzuki Alto 800 (RC Repuestocenter)</td>
              <td>Repuestos Online</td>
              <td>~$40.000</td>
              <td>MercadoLibre</td>
            </tr>
            <tr>
              <td>May 2023</td>
              <td><span class="badge badge-warning">Jeep Compass</span></td>
              <td>Bujías platino NGK / Mopar y bobina de encendido</td>
              <td>Repuestos + Mano Obra</td>
              <td>~$65.000</td>
              <td>MercadoLibre</td>
            </tr>
            <tr style="font-size: 1.05rem; font-weight: 800; background: rgba(56, 189, 248, 0.1);">
              <td colspan="4">TOTAL INVERSIONES ACUMULADAS EN TALLER MAURICIO</td>
              <td style="color: #38bdf8;" colspan="2">~$1.022.450+ CLP</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- ================= TAB: AUDIOS ================= -->
  <div id="tab-audios" class="tab-panel">
    <div class="section-card">
      <div class="section-header">
        <h2>🎧 Registro de Notas de Voz WhatsApp con Mecánico Mauricio</h2>
        <span class="badge badge-info">200 Audios Registrados</span>
      </div>
      <p style="margin-bottom: 18px; color: #cbd5e1;">
        Reproductor integrado de audios de WhatsApp (.opus). Haz clic en 'Reproducir' para escuchar directamente las explicaciones técnicas de Mauricio y de Arturo:
      </p>

      <div id="audioList">
        <!-- Audio 1 -->
        <div class="audio-card filterable">
          <div class="audio-header">
            <span class="audio-sender">👨‍🔧 Mecánico Mauricio</span>
            <span class="audio-date">02 Julio 2026 (17:34) - Suzuki Alto</span>
          </div>
          <div class="audio-context">
            "Arturo, te cuento del auto: ya revisé todo el tren trasero y delantero, quedó impecable, pastillas al 40%, tapiz lavado..."
          </div>
          <audio controls preload="none">
            <source src="WhatsApp Chat - Mecanico Mauricio/00003252-AUDIO-2026-07-02-17-34-04.opus" type="audio/ogg">
            <source src="WhatsApp Chat - Mecanico Mauricio/00003252-AUDIO-2026-07-02-17-34-04.opus" type="audio/opus">
            Tu navegador no soporta el audio directo.
          </audio>
        </div>

        <!-- Audio 2 -->
        <div class="audio-card filterable">
          <div class="audio-header">
            <span class="audio-sender">👨‍🔧 Mecánico Mauricio</span>
            <span class="audio-date">02 Julio 2026 (17:37) - Suzuki Alto</span>
          </div>
          <div class="audio-context">
            "Coordinación para retirar el Suzuki Alto del taller y feedback de la prueba en calle..."
          </div>
          <audio controls preload="none">
            <source src="WhatsApp Chat - Mecanico Mauricio/00003254-AUDIO-2026-07-02-17-37-14.opus" type="audio/ogg">
            <source src="WhatsApp Chat - Mecanico Mauricio/00003254-AUDIO-2026-07-02-17-37-14.opus" type="audio/opus">
          </audio>
        </div>

        <!-- Audio 3 -->
        <div class="audio-card filterable">
          <div class="audio-header">
            <span class="audio-sender">👨‍🔧 Mecánico Mauricio</span>
            <span class="audio-date">03 Julio 2026 (16:06) - Suzuki Alto</span>
          </div>
          <div class="audio-context">
            "Confirmación de horario y disponibilidad del auto guardado sin problemas en el taller..."
          </div>
          <audio controls preload="none">
            <source src="WhatsApp Chat - Mecanico Mauricio/00003255-AUDIO-2026-07-03-16-06-28.opus" type="audio/ogg">
            <source src="WhatsApp Chat - Mecanico Mauricio/00003255-AUDIO-2026-07-03-16-06-28.opus" type="audio/opus">
          </audio>
        </div>

        <!-- Audio 4 -->
        <div class="audio-card filterable">
          <div class="audio-header">
            <span class="audio-sender">👨‍🔧 Mecánico Mauricio</span>
            <span class="audio-date">27 Enero 2026 (17:18) - Jeep Compass</span>
          </div>
          <div class="audio-context">
            "Mauricio reportando el desarme del tablero central, los cables dañados por el cargador y la bandeja izquierda..."
          </div>
          <audio controls preload="none">
            <source src="WhatsApp Chat - Mecanico Mauricio/00002313-AUDIO-2026-01-27-17-18-04.opus" type="audio/ogg">
            <source src="WhatsApp Chat - Mecanico Mauricio/00002313-AUDIO-2026-01-27-17-18-04.opus" type="audio/opus">
          </audio>
        </div>

        <!-- Audio 5 -->
        <div class="audio-card filterable">
          <div class="audio-header">
            <span class="audio-sender">👨‍🔧 Mecánico Mauricio</span>
            <span class="audio-date">07 Noviembre 2025 (21:40) - Jeep Compass</span>
          </div>
          <div class="audio-context">
            "Explicación del compresor con la polea rota y la coordinación con Silverio para cambiar la polea al nuevo compresor..."
          </div>
          <audio controls preload="none">
            <source src="WhatsApp Chat - Mecanico Mauricio/00001042-AUDIO-2025-11-07-21-40-10.opus" type="audio/ogg">
            <source src="WhatsApp Chat - Mecanico Mauricio/00001042-AUDIO-2025-11-07-21-40-10.opus" type="audio/opus">
          </audio>
        </div>

        <!-- Audio 6 -->
        <div class="audio-card filterable">
          <div class="audio-header">
            <span class="audio-sender">👨‍🔧 Mecánico Mauricio</span>
            <span class="audio-date">18 Mayo 2023 (17:51) - Jeep Compass</span>
          </div>
          <div class="audio-context">
            "Evaluación de síntomas graves de motor, temperatura, compresión y recomendaciones de enfriamiento..."
          </div>
          <audio controls preload="none">
            <source src="WhatsApp Chat - Mecanico Mauricio/00000098-AUDIO-2023-05-18-17-51-03.opus" type="audio/ogg">
            <source src="WhatsApp Chat - Mecanico Mauricio/00000098-AUDIO-2023-05-18-17-51-03.opus" type="audio/opus">
          </audio>
        </div>

        <!-- Audio 7 -->
        <div class="audio-card filterable">
          <div class="audio-header">
            <span class="audio-sender">👨‍🔧 Mecánico Mauricio</span>
            <span class="audio-date">26 Abril 2023 (18:25) - Consejos de Motor</span>
          </div>
          <div class="audio-context">
            "Recomendaciones de revoluciones de motor, uso de aceites sintéticos y cuidado de cilindrada..."
          </div>
          <audio controls preload="none">
            <source src="WhatsApp Chat - Mecanico Mauricio/00000011-AUDIO-2023-04-26-18-25-31.opus" type="audio/ogg">
            <source src="WhatsApp Chat - Mecanico Mauricio/00000011-AUDIO-2023-04-26-18-25-31.opus" type="audio/opus">
          </audio>
        </div>
      </div>
    </div>
  </div>

  <!-- ================= TAB: GALERIA FOTOGRAFICA ================= -->
  <div id="tab-galeria" class="tab-panel">
    <div class="section-card">
      <div class="section-header">
        <h2>📸 Archivo Fotográfico y Boletas</h2>
        <span class="badge badge-info">Haz clic para agrandar</span>
      </div>
      <div class="gallery-grid">
        <!-- Item 1 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002908-PHOTO-2026-05-26-20-04-50.jpg', 'Factura Oficial Suzuki Alto: Distribución, Tensor, Termostato, Bujías y Embrague ($124.699)')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00002908-PHOTO-2026-05-26-20-04-50.jpg" alt="Factura Distribución">
          <div class="gallery-info">
            <div class="gallery-title">Factura Embrague & Distribución</div>
            <div class="gallery-date">19-Ago-2025 | Suzuki Alto</div>
          </div>
        </div>

        <!-- Item 2 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002909-PHOTO-2026-05-26-20-04-51.jpg', 'Factura Oficial Suzuki Alto: Pastillas Freno Delanteras DG-12257 ($16.750)')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00002909-PHOTO-2026-05-26-20-04-51.jpg" alt="Factura Pastillas">
          <div class="gallery-info">
            <div class="gallery-title">Factura Pastillas de Freno</div>
            <div class="gallery-date">19-Ago-2025 | Suzuki Alto</div>
          </div>
        </div>

        <!-- Item 3 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00001003-PHOTO-2025-11-05-13-38-47.jpg', 'Boleta Getnet: Repuestos Express Viña San Antonio 1275 ($56.001 CLP)')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00001003-PHOTO-2025-11-05-13-38-47.jpg" alt="Boleta Repuestos Express">
          <div class="gallery-info">
            <div class="gallery-title">Boleta Repuestos Express Viña</div>
            <div class="gallery-date">28-Oct-2025 | Jeep Compass</div>
          </div>
        </div>

        <!-- Item 4 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00001019-PHOTO-2025-11-05-20-14-25.jpg', 'Transferencia Liquidación Santander a Mauricio Cortez ($122.000 CLP)')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00001019-PHOTO-2025-11-05-20-14-25.jpg" alt="Transferencia Mano de Obra">
          <div class="gallery-info">
            <div class="gallery-title">Transferencia Saldo Mano de Obra</div>
            <div class="gallery-date">05-Nov-2025 | Jeep Compass</div>
          </div>
        </div>

        <!-- Item 5 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00000036-PHOTO-2023-05-01-18-54-57.jpg', 'Varilla de aceite del Jeep Compass e información de carga R-134a')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00000036-PHOTO-2023-05-01-18-54-57.jpg" alt="Varilla Jeep">
          <div class="gallery-info">
            <div class="gallery-title">Varilla Aceite Jeep Compass</div>
            <div class="gallery-date">01-May-2023 | Jeep Compass</div>
          </div>
        </div>

        <!-- Item 6 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00003172-PHOTO-2026-06-19-15-19-38.jpg', 'Recepción de autos en taller Mauricio: Iron Maiden y chelas')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00003172-PHOTO-2026-06-19-15-19-38.jpg" alt="Taller">
          <div class="gallery-info">
            <div class="gallery-title">Recepción en Taller Mauricio</div>
            <div class="gallery-date">19-Jun-2026 | Taller</div>
          </div>
        </div>

        <!-- Item 7 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00002895-PHOTO-2026-05-26-19-50-37.jpg', 'Compra Mercado Libre: Amortiguadores Traseros Par Suzuki Alto 800')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00002895-PHOTO-2026-05-26-19-50-37.jpg" alt="Amortiguadores Alto">
          <div class="gallery-info">
            <div class="gallery-title">Compra Amortiguadores Traseros</div>
            <div class="gallery-date">29-Oct-2024 | Suzuki Alto</div>
          </div>
        </div>

        <!-- Item 8 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00000454-PHOTO-2025-10-18-11-44-58.jpg', 'Selección de aceites de transmisión CVT y motor')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00000454-PHOTO-2025-10-18-11-44-58.jpg" alt="Aceites CVT">
          <div class="gallery-info">
            <div class="gallery-title">Selección Aceite CVT & Mobil</div>
            <div class="gallery-date">18-Oct-2025 | Jeep Compass</div>
          </div>
        </div>

        <!-- Item 9 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00000213-PHOTO-2023-05-31-12-23-16.jpg', 'Bobina de encendido nueva para Jeep Compass')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00000213-PHOTO-2023-05-31-12-23-16.jpg" alt="Bobina Jeep">
          <div class="gallery-info">
            <div class="gallery-title">Bobina de Encendido Jeep</div>
            <div class="gallery-date">31-May-2023 | Jeep Compass</div>
          </div>
        </div>

        <!-- Item 10 -->
        <div class="gallery-item filterable" onclick="openImageModal('WhatsApp Chat - Mecanico Mauricio/00001927-PHOTO-2026-01-05-18-04-56.jpg', 'Limpieza de carburador y piezas de moto Honda')">
          <img class="gallery-thumb" src="WhatsApp Chat - Mecanico Mauricio/00001927-PHOTO-2026-01-05-18-04-56.jpg" alt="Carburador Moto">
          <div class="gallery-info">
            <div class="gallery-title">Carburador Moto Honda</div>
            <div class="gallery-date">05-Ene-2026 | Moto Honda</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer>
    <p>Historial y Bitácora de Mantenimiento Automotriz • Datos extraídos directamente de WhatsApp Chat - Mecanico Mauricio</p>
    <p style="margin-top: 6px;">Archivos enlazados directamente: Imágenes, Videos, Notas de Voz (.opus) y VCF Contacts</p>
  </footer>
</div>

<!-- Modal / Lightbox -->
<div id="imageModal" class="modal" onclick="closeModal()">
  <button class="modal-close" onclick="closeModal()">&times;</button>
  <img id="modalImg" class="modal-content" src="" alt="Ampliación" onclick="event.stopPropagation()">
  <div id="modalCaption" class="modal-caption" onclick="event.stopPropagation()"></div>
</div>

<script>
  // Tab Switching
  function switchTab(tabId, el) {
    document.querySelectorAll('.tab-panel').forEach(panel => {
      panel.classList.remove('active');
    });
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.classList.remove('active');
    });
    
    const target = document.getElementById(tabId);
    if (target) target.classList.add('active');

    if (el) {
      el.classList.add('active');
    } else {
      // Find matching button
      const matchedBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => {
        return (tabId.includes('jeep') && b.innerText.includes('Jeep')) ||
               (tabId.includes('alto') && b.innerText.includes('Alto')) ||
               (tabId.includes('moto') && b.innerText.includes('Moto')) ||
               (tabId.includes('costos') && b.innerText.includes('Costos')) ||
               (tabId.includes('audios') && b.innerText.includes('Audios')) ||
               (tabId.includes('galeria') && b.innerText.includes('Galería'));
      });
      if (matchedBtn) matchedBtn.classList.add('active');
    }
  }

  // Image Modal
  function openImageModal(src, caption) {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    const modalCaption = document.getElementById('modalCaption');
    modalImg.src = src;
    modalCaption.innerText = caption || '';
    modal.classList.add('active');
  }

  function closeModal() {
    document.getElementById('imageModal').classList.remove('active');
  }

  // Direct Audio Play
  function playAudioDirect(src, title) {
    switchTab('tab-audios');
    alert('Reproduciendo: ' + title);
    // Find audio element with matching src or create temporary
    let found = Array.from(document.querySelectorAll('audio')).find(a => a.querySelector('source') && a.querySelector('source').src.includes(encodeURI(src)));
    if (found) {
      found.play();
    } else {
      const audio = new Audio(src);
      audio.play();
    }
  }

  // Live Filter Search
  function filterItems() {
    const query = document.getElementById('searchInput').value.toLowerCase().trim();
    const items = document.querySelectorAll('.filterable');
    items.forEach(it => {
      const text = it.innerText.toLowerCase();
      if (!query || text.includes(query)) {
        it.style.display = '';
      } else {
        it.style.display = 'none';
      }
    });
  }

  // Close modal on escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
  });
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html created successfully!")
