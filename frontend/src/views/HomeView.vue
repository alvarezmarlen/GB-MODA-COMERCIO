<template>
  <div class="home-view-container">
    <!-- Hero Section -->
    <div class="hero-section">
      <img src="../assets/Logo.jpg" alt="Logo Mujeres Trabajadoras" class="hero-logo-centered" />
      <h1 class="hero-title-centered">GB-MODA-COMERCIO</h1>
      <p class="hero-paragraph-centered">
        “Mujeres trabajadoras de nuestras vidas” son un conjunto de relatos biográficos que pretenden realzar y poner en valor el trabajo diario que desempeñan las mujeres de nuestro entorno. Dar a conocer sus historias de vida y agradecer el trabajo que han realizado tanto fuera como dentro del hogar.
      </p>
    </div>

    <!-- Map Section -->
    <InteractiveMap />

    <!-- Chronicles / Filters Section -->
    <ChronicleList />
  </div>
</template>

<script setup>
import InteractiveMap from '../components/organisms/InteractiveMap.vue'
import ChronicleList from '../components/organisms/ChronicleList.vue'
</script>

<style scoped>
.home-view-container {
  /* Color Palette */
  --color-principal: #2D6A8B; /* Azul Pizarra */
  --color-rojo: #E93C44;
  --color-amarillo: #FCD015;
  --color-verde: #48C5B6;
  --color-blanco: #FFFFFF;

  padding: var(--wf-spacing-md);
  animation: fadeIn 0.4s ease-out;
  
  /* Solid background color */
  background-color: var(--color-principal);
  min-height: 100vh;
}

.hero-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 40px 20px 60px 20px;
  max-width: 900px;
  margin: 0 auto;
}

.hero-logo-centered {
  max-width: 350px;
  width: 100%;
  height: auto;
  object-fit: contain;
  margin-bottom: 30px;
  filter: drop-shadow(0 8px 16px rgba(0,0,0,0.2));
  border-radius: 8px; /* Opcional, por si la imagen se ve mejor con bordes redondeados */
}

.hero-title-centered {
  font-size: 2.5rem;
  font-weight: bold;
  letter-spacing: 2px;
  margin-bottom: 24px;
  text-transform: uppercase;
  color: var(--color-amarillo); /* El amarillo resalta excelente sobre el fondo azul oscuro */
  border-bottom: 4px solid var(--color-rojo);
  padding-bottom: 12px;
  display: inline-block;
}

.hero-paragraph-centered {
  font-size: 1.25rem;
  line-height: 1.7;
  color: var(--color-blanco); /* Texto blanco para máxima legibilidad sobre azul */
  margin: 0;
  font-weight: 500;
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Responsive */
@media (max-width: 800px) {
  .hero-logo-centered {
    max-width: 250px;
  }
  
  .hero-title-centered {
    font-size: 1.8rem;
  }
  
  .hero-paragraph-centered {
    font-size: 1.05rem;
  }
}
</style>
