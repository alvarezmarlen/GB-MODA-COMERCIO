<template>
  <div class="wireframe-container map-section-container">
    <div class="section-header">
      <h2 class="section-title">Mapa de Historias y Oficios</h2>
      <p class="section-subtitle">
        Explora los relatos tradicionales haciendo clic en las diferentes regiones del mapa.
      </p>
    </div>

    <!-- 70% / 30% Grid Layout -->
    <div class="map-grid">
      <!-- Left (70%): Interactive SVG Map -->
      <div class="map-visual-box">
        <svg viewBox="0 0 800 400" class="interactive-world-map" xmlns="http://www.w3.org/2000/svg">
          <!-- Background grids for wireframe style -->
          <defs>
            <pattern id="wireframe-grid" width="20" height="20" patternUnits="userSpaceOnUse">
              <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f0f0f0" stroke-width="1" />
            </pattern>
          </defs>
          <rect width="100%" height="100%" fill="url(#wireframe-grid)" />

          <!-- Path 1: Europa & África -->
          <path id="Europa-Africa"
                :class="{ 'active-region': selectedRegion === 'Europa-Africa', 'hovered-region': hoveredRegion === 'Europa-Africa' }"
                @click="selectRegion('Europa-Africa')"
                @mouseenter="hoveredRegion = 'Europa-Africa'"
                @mouseleave="hoveredRegion = null"
                d="M352.346,231.706l7.955-0.378c2.06-0.099,3.976-0.979,5.394-2.48l8.351-8.842c2.28-2.414,2.815-6.032,1.329-9.003
                l-5.843-11.564l12.973-7.983c1.674-1.03,2.901-2.637,3.456-4.521l5.253-17.86c1.133-3.855-0.797-7.955-4.49-9.538l-7.879-3.326
                l1.049-6.1l9.008-3.793c2.151-0.904,3.788-2.7,4.491-4.927l1.269-4.014l10.367,12.253c1.516,1.791,3.712,2.818,6.026,2.818
                c4.398,0,7.976-3.565,7.976-7.948l-0.001-13.994l-0.322-15.146c-0.214-10.079-8.578-18.279-18.645-18.279
                c-0.747,0-1.504,0.045-2.25,0.135l-77.435,9.292l0.531-1.442c0.876-2.378,0.558-5.056-0.852-7.161
                c-1.409-2.106-3.763-3.422-6.294-3.519l-9.848-0.379c-2.599-0.09-5.105,1.101-6.658,3.17l-24.181,32.253l-21.325,10.69
                l-17.579-9.057c-1.12-0.576-2.376-0.881-3.634-0.881c-2.187,0-4.3,0.915-5.794,2.51l-16.302,17.388
                c-2.068,2.206-2.704,5.34-1.658,8.177l2.943,7.884l-10.435,9.887l-9.946,5.759c-2.84,1.645-4.361,4.805-3.873,8.051l0.831,5.539
                c0.578,3.856,3.955,6.766,7.854,6.765c1.125,0,2.221-0.236,3.257-0.702l8.502-3.827l10.604-4.494l10.86,7.602
                c0.921,0.646,1.948,1.081,3.047,1.292l16.603,3.165v4.104l-34.356-5.153c-1.383-0.212-2.799-0.047-4.097,0.466l-22.403,8.843
                c-2.456,0.97-4.263,3.087-4.835,5.664l-4.38,19.712c-0.621,2.791,0.314,5.713,2.439,7.624l10.325,9.294
                c1.665,1.498,3.893,2.222,6.122,1.996l19.936-2.109l0.574,29.839c0.014,0.731,0.129,1.455,0.34,2.151l3.636,12
                c2.232,7.368,8.905,12.318,16.604,12.318c6.49,0,12.385-3.575,15.385-9.33l27.542-52.836c1.64-3.145,0.978-7.037-1.61-9.464
                l-3.589-3.364l5.584-1.861c2.629-0.877,4.58-3.012,5.216-5.709c0.637-2.697-0.153-5.479-2.113-7.438l-8.196-8.117l0.544-0.688
                l17.154,11.061l13.818,19.96c1.483,2.143,3.921,3.421,6.523,3.421c2.989,0,5.696-1.649,7.064-4.304l6.159-12.105l13.825,9.823
                c1.362,0.968,2.948,1.48,4.585,1.48c2.357-0.001,4.585-1.043,6.114-2.861c1.498-1.781,2.126-4.133,1.723-6.452L352.346,231.706z"/>

          <!-- Path 2: Oceanía -->
          <path id="Oceania"
                :class="{ 'active-region': selectedRegion === 'Oceania', 'hovered-region': hoveredRegion === 'Oceania' }"
                @click="selectRegion('Oceania')"
                @mouseenter="hoveredRegion = 'Oceania'"
                @mouseleave="hoveredRegion = null"
                d="M422.31,296.3l-9.319-17.706c-1.377-2.616-4.071-4.241-7.03-4.241c-2.629,0-5.073,1.293-6.558,3.468l-2.432-3.04
                c-1.515-1.894-3.775-2.979-6.202-2.979c-1.437,0-2.849,0.391-4.083,1.132l-22.045,13.227c-2.104,1.261-3.526,3.47-3.805,5.907
                l-1.877,16.424c-0.256,2.246,0.459,4.5,1.962,6.185c1.726,1.935,4.28,2.921,6.912,2.594l18.67-2.377l2.958,7.025
                c1.242,2.952,4.114,4.859,7.316,4.859c0,0,0,0,0.001,0c0.455,0,0.913-0.04,1.362-0.118l10.25-1.782
                c2.514-0.435,4.678-2.068,5.79-4.365l8.253-17.056C423.524,301.198,423.479,298.522,422.31,296.3z"/>

          <!-- Path 3: América -->
          <path id="America"
                :class="{ 'active-region': selectedRegion === 'America', 'hovered-region': hoveredRegion === 'America' }"
                @click="selectRegion('America')"
                @mouseenter="hoveredRegion = 'America'"
                @mouseleave="hoveredRegion = null"
                d="M153.469,265.01l-37.698-24.424c-2.067-1.339-4.459-2.047-6.916-2.047c-3.966,0-7.648,1.844-10.051,4.947l-8.455-4.733
                l-15.1-21.496h7.702c1.836,0,3.627-0.642,5.043-1.807l28.637-23.547l15.938-9.032c1.94-1.1,3.336-2.977,3.829-5.151
                c0.494-2.175,0.045-4.471-1.231-6.301l-14.111-20.227c-1.531-2.193-4.057-3.468-6.713-3.395
                c-2.673,0.067-5.115,1.462-6.532,3.729l-7.273,11.782l-8.339-9.378l16.573-12.187c3.068-2.257,4.102-6.388,2.459-9.822
                l-4.086-8.545c-0.953-1.992-2.709-3.509-4.818-4.161c-2.11-0.653-4.415-0.391-6.323,0.715l-7.224,4.21l-32.646-13.813
                L32.686,97.102c-2.844-1.604-6.443-1.283-8.957,0.795L11.31,108.156c-1.091,0.901-1.923,2.08-2.405,3.408l-8.429,23.181
                c-0.871,2.393-0.534,5.079,0.9,7.185c1.435,2.105,3.811,3.4,6.358,3.467l17.89,0.422l11.355,28.074l-1.854,27.803
                c-0.112,1.684,0.327,3.394,1.238,4.814l15.267,23.815c0.919,1.435,2.248,2.517,3.845,3.131l29.367,11.24
                c0.266,0.254,0.562,0.465,0.876,0.633l8.586,4.807l-4.611,6.916c-1.646,2.469-1.782,5.619-0.355,8.222l9.663,17.604
                l-1.26,42.85c-0.054,1.834,0.534,3.643,1.658,5.096l7.795,10.067c1.52,1.963,3.793,3.089,6.239,3.089
                c2.157,0,4.255-0.882,5.756-2.419c1.485-1.521,2.274-3.552,2.222-5.719l-0.358-14.23l29.281-28.035
                c1.052-1.008,1.806-2.283,2.18-3.689l4.311-16.166C157.713,270.388,156.365,266.888,153.469,265.01z"/>

          <!-- Path 4: Groenlandia -->
          <path id="Groenlandia"
                :class="{ 'active-region': selectedRegion === 'Groenlandia', 'hovered-region': hoveredRegion === 'Groenlandia' }"
                @click="selectRegion('Groenlandia')"
                @mouseenter="hoveredRegion = 'Groenlandia'"
                @mouseleave="hoveredRegion = null"
                d="M136.06,107.943l4.304,3.261v39.436c0,4.382,3.567,7.947,7.951,7.947c1.535,0,3.034-0.45,4.335-1.302l27.258-17.822
                c1.707-1.116,2.906-2.823,3.378-4.806l9.091-38.182c0.678-2.85-0.261-5.828-2.45-7.773l-8.403-7.47
                c-2.229-1.982-5.52-2.545-8.282-1.414l-35.365,14.468c-2.666,1.09-4.485,3.446-4.865,6.301
                C132.632,103.442,133.771,106.192,136.06,107.943z"/>
        </svg>

        <!-- Hover visual tooltip inside the map box -->
        <div class="map-tooltip" v-if="hoveredRegion || selectedRegion">
          <span>Región: </span>
          <strong>{{ getRegionDisplayName(hoveredRegion || selectedRegion) }}</strong>
        </div>
        <div class="map-tooltip" v-else>
          <span>Haz clic en una región para explorar</span>
        </div>
      </div>

      <!-- Right (30%): Detailed Information Panel & Filter options -->
      <div class="map-details-box">
        <div class="details-header">
          <div class="details-title-tag">REGIÓN DEL MAPA</div>
          <h3 class="details-region-name">{{ getRegionDisplayName(selectedRegion) }}</h3>
        </div>

        <div class="details-content">
          <p class="details-description">
            {{ getRegionDescription(selectedRegion) }}
          </p>

          <!-- Predefined Aligned Selectable Countries (España, Pais Vasco, Marruecos, Africa, America Central, otro) -->
          <div class="associated-countries-section">
            <span class="associated-label">Seleccionar País / Territorio:</span>
            <div class="countries-tag-list">
              <button
                v-for="country in getAssociatedCountries(selectedRegion)"
                :key="country.value"
                class="wireframe-button country-filter-btn"
                :class="{ 'selected-country-btn': activeCountryFilter === country.value }"
                @click="toggleCountryFilter(country.value)"
              >
                [ {{ country.label }} ]
              </button>
            </div>
          </div>

          <!-- Mapped stories result container (ready to connect to backend) -->
          <div class="stories-indicator-box">
            <div class="stories-count-label">
              <span>Crónicas encontradas: </span>
              <strong class="ready-badge">Listo para BD</strong>
            </div>
            
            <div class="stories-list-placeholder">
              <div v-if="filteredStories.length === 0" class="no-stories-msg">
                <span>-- Ninguna crónica cargada --</span>
                <p>Las historias creadas con origen en esta región se listarán automáticamente aquí al conectar la base de datos.</p>
              </div>
              <div v-else class="stories-wireframe-cards">
                <div 
                  v-for="story in filteredStories" 
                  :key="story.id" 
                  class="story-mini-card"
                >
                  <div class="mini-card-header">
                    <span class="story-profession-tag">{{ story.profession }}</span>
                    <span class="story-age-tag">{{ story.ageRange }}</span>
                  </div>
                  <h4 class="mini-card-title">{{ story.title }}</h4>
                  <p class="mini-card-excerpt">{{ truncateText(story.description, 95) }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedRegion = ref('Europa-Africa')
const hoveredRegion = ref(null)
const activeCountryFilter = ref('todos')

// Exactly the user's requested selectable countries: España, Pais Vasco, Marruecos, Africa, America Central, y Otro.
const getAssociatedCountries = (region) => {
  switch (region) {
    case 'Europa-Africa':
      return [
        { label: 'Todos', value: 'todos' },
        { label: 'España', value: 'España' },
        { label: 'Pais Vasco', value: 'Pais Vasco' },
        { label: 'Marruecos', value: 'Marruecos' },
        { label: 'Africa', value: 'Africa' },
        { label: 'Otro', value: 'Otro' }
      ]
    case 'America':
      return [
        { label: 'Todos', value: 'todos' },
        { label: 'America Central', value: 'America Central' },
        { label: 'Otro', value: 'Otro' }
      ]
    default:
      return [
        { label: 'Todos', value: 'todos' },
        { label: 'Otro', value: 'Otro' }
      ]
  }
}

const getRegionDisplayName = (region) => {
  if (!region) return 'Ninguna'
  switch (region) {
    case 'Europa-Africa':
      return 'Europa y África'
    case 'America':
      return 'América'
    case 'Oceania':
      return 'Oceanía'
    case 'Groenlandia':
      return 'Groenlandia'
    default:
      return region
  }
}

const getRegionDescription = (region) => {
  switch (region) {
    case 'Europa-Africa':
      return 'Zona que conecta los territorios históricos de España, el País Vasco y el continente africano. Alberga un legado inestimable en oficios tradicionales.'
    case 'America':
      return 'Territorio del continente americano. Reúne crónicas de América Central y el resto del continente, desde telares tradicionales hasta orfebrería.'
    case 'Oceania':
      return 'Región de islas y archipiélagos. Representa los oficios del Pacífico.'
    case 'Groenlandia':
      return 'Zona ártica del norte. Reúne los oficios milenarios adaptados a climas helados.'
    default:
      return 'Haz clic en el mapa interactivo para ver su descripción.'
  }
}

const selectRegion = (region) => {
  selectedRegion.value = region
  activeCountryFilter.value = 'todos' // Reset filter
}

const toggleCountryFilter = (value) => {
  activeCountryFilter.value = value
}

// Truncate helper
const truncateText = (text, limit) => {
  if (!text) return ''
  if (text.length <= limit) return text
  return text.substring(0, limit) + '...'
}

// High-fidelity Mock Stories to show everything functioning perfectly
const mockStories = [
  {
    id: 1,
    title: 'El Telar de Alada y el cáñamo de Guipúzcoa',
    profession: 'Industria',
    ageRange: '46 - 60 años',
    country: 'Pais Vasco',
    region: 'Europa-Africa',
    description: 'Crónica dedicada a recuperar la hilatura tradicional de fibras vegetales en el País Vasco, un oficio que definió la vestimenta local durante siglos.'
  },
  {
    id: 2,
    title: 'La alfarería roja del Rif marroquí',
    profession: 'Campo',
    ageRange: 'Más de 60',
    country: 'Marruecos',
    region: 'Europa-Africa',
    description: 'El modelado a mano de arcilla sin torno, cocido al aire libre por mujeres artesanas en aldeas de Marruecos. Un legado vivo transmitido de madres a hijas.'
  },
  {
    id: 3,
    title: 'Últimos sastres artesanos de Madrid',
    profession: 'Limpieza',
    ageRange: '36 - 45 años',
    country: 'España',
    region: 'Europa-Africa',
    description: 'Sastrería tradicional de corte de patrón en papel y cosido a mano con hilo de seda. El arte del detalle que resiste al fast-fashion.'
  },
  {
    id: 4,
    title: 'Curtido tradicional de cuero en Fez',
    profession: 'Industria',
    ageRange: '46 - 60 años',
    country: 'Africa',
    region: 'Europa-Africa',
    description: 'El laborioso proceso de curtido y tinte natural de pieles en las famosas cubas de piedra de la medina de Fez.'
  },
  {
    id: 5,
    title: 'Tejido del Huipil tradicional en Guatemala',
    profession: 'Casa',
    ageRange: '26 - 35 años',
    country: 'America Central',
    region: 'America',
    description: 'El arte del telar de cintura usado por mujeres mayas en Guatemala para tejer huipiles con intrincados diseños geométricos.'
  },
  {
    id: 6,
    title: 'Tallado en piedra volcánica en Antigua',
    profession: 'Campo',
    ageRange: '36 - 45 años',
    country: 'Otro',
    region: 'America',
    description: 'Elaboración tradicional de morteros (molcajetes) tallados pacientemente a partir de rocas volcánicas locales.'
  }
]

const filteredStories = computed(() => {
  return mockStories.filter(story => {
    // Check region match
    if (story.region !== selectedRegion.value) return false
    
    // Check sub country filter match
    if (activeCountryFilter.value !== 'todos') {
      return story.country === activeCountryFilter.value
    }
    
    return true
  })
})
</script>

<style scoped>
.map-section-container {
  margin-top: var(--wf-spacing-lg);
  padding: var(--wf-spacing-lg);
  background: var(--wf-bg);
  border-width: 2px;
}

.section-header {
  border-bottom: 2px solid var(--wf-border);
  padding-bottom: var(--wf-spacing-sm);
  margin-bottom: var(--wf-spacing-lg);
}

.section-title {
  font-size: 1.5rem;
  font-weight: bold;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.section-subtitle {
  font-size: 0.9rem;
  color: #555555;
  margin-top: 4px;
}

/* 70% / 30% Screen Grid Layout */
.map-grid {
  display: grid;
  grid-template-columns: 7fr 3fr; /* 70% / 30% Split */
  gap: var(--wf-spacing-lg);
  align-items: stretch;
}

/* Map visual styling */
.map-visual-box {
  border: 2px solid var(--wf-border);
  background: #fcfcfc;
  padding: var(--wf-spacing-md);
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 480px; /* Made the map significantly larger visually */
  overflow: hidden;
  transition: all 0.3s ease;
}

.interactive-world-map {
  width: 95%;
  height: auto;
  max-height: 440px;
}

/* Map Paths styling matching the premium wireframe sketch style */
path {
  cursor: pointer;
  transition: all 0.3s ease;
  opacity: 0.85;
}

path:hover {
  opacity: 1;
  stroke: var(--wf-border) !important;
  stroke-width: 3.5 !important;
  filter: drop-shadow(0px 4px 8px rgba(0,0,0,0.15));
}

.active-region {
  opacity: 1 !important;
  stroke: var(--wf-border) !important;
  stroke-width: 3.5 !important;
  fill-opacity: 0.95;
}

/* High fidelity region color schemes */
#Europa-Africa {
  fill: #80c2f7;
  stroke: #2563eb;
}
#Europa-Africa.active-region, #Europa-Africa:hover {
  fill: #3b82f6;
}

#Oceania {
  fill: #a7f3d0;
  stroke: #059669;
}
#Oceania.active-region, #Oceania:hover {
  fill: #10b981;
}

#America {
  fill: #fef08a;
  stroke: #ca8a04;
}
#America.active-region, #America:hover {
  fill: #eab308;
}

#Groenlandia {
  fill: #fecaca;
  stroke: #dc2626;
}
#Groenlandia.active-region, #Groenlandia:hover {
  fill: #ef4444;
}

.map-tooltip {
  position: absolute;
  bottom: 16px;
  left: 16px;
  background: var(--wf-bg);
  border: 2px solid var(--wf-border);
  padding: 6px 12px;
  font-size: 0.85rem;
  font-family: monospace;
  z-index: 10;
  box-shadow: 3px 3px 0px var(--wf-border);
}

/* Details Box Panel (30% column) styling */
.map-details-box {
  border: 2px solid var(--wf-border);
  background: var(--wf-bg);
  display: flex;
  flex-direction: column;
  padding: var(--wf-spacing-lg);
  transition: all 0.3s ease;
  min-height: 480px;
}

.map-details-box:hover {
  box-shadow: 4px 4px 0px var(--wf-border);
  transform: translate(-2px, -2px);
}

.details-header {
  border-bottom: 2px solid var(--wf-border);
  padding-bottom: var(--wf-spacing-sm);
  margin-bottom: var(--wf-spacing-md);
}

.details-title-tag {
  font-size: 0.75rem;
  font-weight: bold;
  letter-spacing: 1px;
  color: #777777;
}

.details-region-name {
  font-size: 1.4rem;
  font-weight: bold;
  text-transform: uppercase;
}

.details-description {
  font-size: 0.85rem;
  line-height: 1.5;
  margin-bottom: var(--wf-spacing-md);
  text-align: justify;
  color: #333333;
}

.associated-countries-section {
  margin-bottom: var(--wf-spacing-md);
}

.associated-label {
  display: block;
  font-size: 0.78rem;
  font-weight: bold;
  margin-bottom: 8px;
  text-transform: uppercase;
}

.countries-tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.country-filter-btn {
  font-size: 0.72rem;
  padding: 4px 6px;
  background: var(--wf-button-bg);
  border: 1px solid var(--wf-border);
}

.selected-country-btn {
  background: var(--wf-border) !important;
  color: var(--wf-bg) !important;
}

/* Stories section */
.stories-indicator-box {
  border-top: 1px dashed var(--wf-border);
  padding-top: var(--wf-spacing-sm);
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.stories-count-label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.78rem;
  margin-bottom: 10px;
}

.ready-badge {
  background: #f0fdf4;
  color: #166534;
  border: 1px solid #bbf7d0;
  padding: 2px 6px;
  font-size: 0.68rem;
  text-transform: uppercase;
}

.stories-list-placeholder {
  background: #fafafa;
  border: 1px solid var(--wf-border);
  padding: var(--wf-spacing-sm);
  min-height: 120px;
  flex-grow: 1;
  overflow-y: auto;
}

.no-stories-msg {
  color: #777777;
  font-size: 0.78rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: var(--wf-spacing-sm);
}

.stories-wireframe-cards {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.story-mini-card {
  border: 1px solid var(--wf-border);
  background: var(--wf-bg);
  padding: 8px;
  transition: all 0.2s ease;
}

.story-mini-card:hover {
  background: #fcfcfc;
  transform: translateX(3px);
  box-shadow: 2px 2px 0 var(--wf-border);
}

.mini-card-header {
  display: flex;
  justify-content: space-between;
  font-size: 0.68rem;
  color: #666666;
  margin-bottom: 2px;
}

.story-profession-tag {
  font-weight: bold;
}

.mini-card-title {
  font-size: 0.85rem;
  font-weight: bold;
  margin-bottom: 2px;
  line-height: 1.2;
}

.mini-card-excerpt {
  font-size: 0.78rem;
  color: #444444;
  line-height: 1.3;
}

/* Responsive grid for map */
@media (max-width: 900px) {
  .map-grid {
    grid-template-columns: 1fr;
  }
  .map-visual-box {
    min-height: 380px;
  }
}
</style>
