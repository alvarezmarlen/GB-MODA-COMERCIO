<template>
  <div class="interactive-map-wrapper">
    <div class="map-content">
      <div class="map-visual-box">
        <svg viewBox="0 0 800 400" class="world-svg" xmlns="http://www.w3.org/2000/svg">
          <path
            id="Norteamerica"
            class="continent hover-red"
            d="m 111,171.26 35.79,-29.42 19.92,-11.29 A 9.93,9.93 0 0 0 170,116.22 L 152.32,90.94 a 9.92,9.92 0 0 0 -16.56,0.42 L 126.67,106.09 116.25,94.37 137,79.13 a 9.93,9.93 0 0 0 3,-12.29 L 134.89,56.16 A 9.92,9.92 0 0 0 121,51.84 L 112,57.1 71.17,39.84 41.86,23.33 a 10,10 0 0 0 -11.2,1 L 15.14,37.14 a 9.92,9.92 0 0 0 -3,4.26 L 1.6,70.4 a 9.93,9.93 0 0 0 9.07,13.31 l 22.33,0.51 14.19,35.09 -2.32,34.75 z"
          />
          <path
            id="Suramerica"
            class="continent hover-yellow"
            d="m 118.88,214.62 -5.76,8.64 a 9.9,9.9 0 0 0 -0.44,10.28 l 12.08,22 -1.58,53.56 a 10,10 0 0 0 2.07,6.37 l 9.75,12.59 a 9.81,9.81 0 0 0 7.8,3.86 10.11,10.11 0 0 0 7.19,-3 9.8,9.8 0 0 0 2.78,-7.15 l -0.45,-17.79 36.6,-35 a 9.92,9.92 0 0 0 2.72,-4.61 L 197,244.1 a 9.91,9.91 0 0 0 -4.19,-10.89 l -47.12,-30.53 a 15.87,15.87 0 0 0 -21.21,3.63 z"
          />
          <path
            id="Centroamerica"
            class="continent hover-red"
            d="m 124.5,206.31 -10.57,-5.92 -18.87,-26.87 h 9.63 a 10,10 0 0 0 6.3,-2.26 L 44.91,154.07 a 10,10 0 0 0 1.55,6 l 19.08,29.77 a 9.87,9.87 0 0 0 4.81,3.91 l 36.7,14.09 a 5,5 0 0 0 1.09,0.79 l 10.73,6 z"
          />
          <path
            id="Otros 1"
            class="continent hover-yellow"
            d="m 171.07,36.84 5.38,4.08 v 49.29 a 9.91,9.91 0 0 0 15.36,8.31 l 34.07,-22.28 a 9.88,9.88 0 0 0 4.22,-6 l 11.37,-47.7 a 9.91,9.91 0 0 0 -3.06,-9.7 L 227.91,3.5 A 10.05,10.05 0 0 0 217.56,1.73 l -44.21,18.11 a 9.93,9.93 0 0 0 -2.28,17 z"
          />
          <path
            id="Asia"
            class="continent hover-red"
            d="m 345.62,168.35 21.44,13.83 17.27,25 a 9.92,9.92 0 0 0 17,-1.1 l 7.7,-15.13 17.28,12.28 a 9.85,9.85 0 0 0 5.73,1.85 10,10 0 0 0 7.64,-3.58 9.87,9.87 0 0 0 2.15,-8.06 l -0.4,-1.8 9.94,-0.47 a 9.89,9.89 0 0 0 6.74,-3.1 l 10.44,-11.05 a 10,10 0 0 0 1.66,-11.25 l -7.3,-14.45 16.22,-10 a 9.92,9.92 0 0 0 4.32,-5.65 L 490,113.29 a 9.93,9.93 0 0 0 -5.61,-11.92 l -9.85,-4.16 1.31,-7.63 11.28,-4.74 a 9.9,9.9 0 0 0 5.61,-6.16 l 1.59,-5 13,15.32 a 9.92,9.92 0 0 0 17.5,-6.41 V 65.08 l -0.4,-18.93 A 23.32,23.32 0 0 0 498.31,23.47 l -96.84,11.61 0.66,-1.8 A 9.93,9.93 0 0 0 393.2,19.93 l -12.31,-0.47 a 10,10 0 0 0 -8.32,4 L 342.35,63.74 315.69,77.1 Z"
          />
          <path
            id="Europa"
            class="continent hover-yellow"
            d="m 315.69,77.1 -22,-11.32 a 9.92,9.92 0 0 0 -11.79,2 l -20.38,21.74 a 9.87,9.87 0 0 0 -2.07,10.22 l 3.68,9.86 -13,12.36 -12.43,7.2 a 9.87,9.87 0 0 0 -4.84,10.06 l 1,6.92 a 10,10 0 0 0 9.82,8.46 9.86,9.86 0 0 0 4.07,-0.88 l 10.63,-4.78 13.26,-5.62 13.58,9.5 a 9.82,9.82 0 0 0 3.81,1.62 l 20.75,4 35.83,9.93 Z"
          />
          <path
            id="Africa"
            class="continent hover-red"
            d="m 309.79,158.42 v 5.13 l -42.95,-6.44 a 9.88,9.88 0 0 0 -5.12,0.58 l -28,11.05 a 9.91,9.91 0 0 0 -6,7.08 l -5.48,24.64 a 9.93,9.93 0 0 0 3,9.53 l 12.91,11.62 a 10,10 0 0 0 7.65,2.49 l 24.92,-2.64 0.72,37.3 a 9.93,9.93 0 0 0 0.42,2.69 l 4.55,15 a 21.69,21.69 0 0 0 40,3.74 l 34.43,-66 a 10,10 0 0 0 -2,-11.83 l -4.49,-4.2 7,-2.33 a 9.93,9.93 0 0 0 3.88,-16.43 l -10.25,-10.15 0.68,-0.86 Z"
          />
          <path
            id="Otros 2"
            class="continent hover-yellow"
            d="m 528.89,272.32 -11.65,-22.13 a 9.93,9.93 0 0 0 -17,-1 l -3,-3.8 a 9.92,9.92 0 0 0 -12.86,-2.31 l -27.58,16.57 a 10,10 0 0 0 -4.76,7.38 l -2.35,20.53 a 9.92,9.92 0 0 0 11.09,11 l 23.34,-3 3.7,8.78 a 9.9,9.9 0 0 0 9.15,6.07 v 0 a 10,10 0 0 0 1.7,-0.15 l 12.81,-2.23 a 10,10 0 0 0 7.24,-5.46 L 529,281.27 a 10,10 0 0 0 -0.11,-8.95 z"
          />
        </svg>
      </div>

      <!-- Right text section -->
      <div class="map-text-box">
        <h2 class="map-quote">"Historias que cruzan muchas fronteras"</h2>
      </div>
    </div>
  </div>
</template>

<script setup>
// Map logic component
</script>

<style scoped>
.interactive-map-wrapper {
  background-color: #48C5B6;
  width: 100%;
  padding: 40px 0; /* Increased vertical padding to make map appear lower and centered */
}

.map-content {
  display: flex;
  align-items: center;
  justify-content: center;
  max-width: 1200px;
  margin: 0 auto;
  gap: 40px;
  padding: 0 40px;
}

.map-visual-box {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

.world-svg {
  width: 100%;
  height: auto;
  max-width: 800px;
  min-height: 300px;
}

.continent {
  fill: #ffffff;
  stroke: transparent;
  transition: fill 0.3s ease, transform 0.3s ease;
  cursor: pointer;
  transform-origin: center;
}

/* Hover effects */
.continent.hover-red:hover {
  fill: #E93C44;
}

.continent.hover-yellow:hover {
  fill: #FCD015;
}

.continent:hover {
  transform: scale(1.01);
}

.map-text-box {
  flex: 0 0 0; /* Reduced from 35% to give more space to the map */
}

.map-quote {
  font-family: var(--font-title);
  font-size: clamp(2rem, 3vw, 3.5rem);
  line-height: 1.3;
  font-weight: 400;
  color: var(--color-blanco);
}

/* Responsive */
@media (max-width: 900px) {
  .map-content {
    flex-direction: column;
    text-align: center;
    gap: 20px;
  }
  
  .map-text-box {
    margin-bottom: 40px;
  }
}
</style>
