<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <button class="close-btn" @click="close">✕</button>
      <div class="modal-body" ref="modalBody">
        <h1 id="title">TÉRMINOS, CONDICIONES Y PRIVACIDAD</h1>
        <p class="last-update">Última actualización: Mayo, 2026</p>
        
        <p>Bienvenida/o a GB-MODA-COMERCIO. Al navegar por nuestro sitio, comentar o compartir contenido con nosotros, aceptas las siguientes reglas básicas:</p>
        
        <h2 id="terminos">1. Propiedad del Contenido</h2>
        <p>Todo el material de este blog (textos, imágenes y logotipos) está protegido por derechos de autor. Puedes leer y compartir los enlaces del contenido con fines personales, pero está prohibida su copia, reproducción o uso comercial sin nuestro permiso por escrito.</p>
        
        <h2>2. Envío de Historias y Colaboraciones</h2>
        <p>Si nos envías una historia para publicar, garantizas que:</p>
        <ul>
          <li>El relato es tuyo (original) o tienes el permiso explícito para contarlo.</li>
          <li>Has cambiado los nombres y datos reales de terceros para proteger su anonimato y privacidad.</li>
          <li>Nos otorgas permiso gratuito para publicar, adaptar el formato y difundir la historia en el blog y sus redes sociales, manteniendo siempre tu autoría.</li>
        </ul>
        
        <h2 id="privacidad">3. Privacidad y Protección de Datos</h2>
        <p>Tu privacidad es fundamental para nosotros. Nos comprometemos a cuidar tus datos bajo las siguientes reglas:</p>
        <ul>
          <li><strong>Recopilación mínima:</strong> Solo recolectamos los datos que tú nos das voluntariamente (como tu nombre/seudónimo y correo al comentar o enviarnos una historia).</li>
          <li><strong>Uso de los datos:</strong> Solo usaremos tu correo para gestionar tus colaboraciones o responder a tus mensajes. Nunca venderemos ni compartiremos tus datos con terceros.</li>
          <li><strong>Tus derechos:</strong> En cualquier momento puedes pedirnos que borremos tu correo de nuestra base de datos o que eliminemos una historia que hayas enviado, escribiéndonos al contacto del blog.</li>
        </ul>
        
        <h2>4. Normas de la Comunidad (Comentarios)</h2>
        <p>Este es un espacio seguro y de apoyo. No toleramos insultos, acoso, spam, discursos de odio ni comentarios discriminatorios. Nos reservamos el derecho de eliminar cualquier mensaje que falte al respeto.</p>
        
        <h2>5. Exención de Responsabilidad</h2>
        <p>Las historias compartidas representan vivencias personales de sus autoras. GB-MODA-COMERCIO no se hace responsable de la veracidad de los relatos. Asimismo, el contenido es meramente narrativo; no sustituye la ayuda ni el asesoramiento de profesionales (psicológicos, legales o médicos).</p>
        
        <h2 id="contacto">6. Contacto</h2>
        <p>Si deseas ejercer tus derechos de privacidad, retirar una historia o tienes dudas, escríbenos a: <a href="mailto:info@grupopenascal.com">info@grupopenascal.com</a>.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue'

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true
  },
  section: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['close'])

const modalBody = ref(null)

const close = () => {
  emit('close')
}

watch(() => props.isOpen, async (newVal) => {
  if (newVal && props.section) {
    await nextTick()
    scrollToSection(props.section)
  }
})

watch(() => props.section, async (newVal) => {
  if (props.isOpen && newVal) {
    await nextTick()
    scrollToSection(newVal)
  }
})

const scrollToSection = (id) => {
  const element = document.getElementById(id)
  if (element && modalBody.value) {
    modalBody.value.scrollTo({
      top: element.offsetTop - 20,
      behavior: 'smooth'
    })
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: var(--color-white);
  width: 90%;
  max-width: 800px;
  height: 80vh;
  border-radius: var(--wf-radius);
  position: relative;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}

.close-btn {
  position: absolute;
  top: 15px;
  right: 15px;
  background: transparent;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--color-red);
}

.modal-body {
  padding: 40px;
  overflow-y: auto;
  flex: 1;
}

.modal-body h1 {
  font-size: 1.8rem;
  color: var(--color-yellow);
  margin-bottom: 5px;
  border-bottom: 2px solid var(--color-red);
  padding-bottom: 10px;
}

.last-update {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 20px;
}

.modal-body h2 {
  font-size: 1.3rem;
  color: var(--color-primary);
  margin-top: 30px;
  margin-bottom: 10px;
}

.modal-body p, .modal-body ul {
  line-height: 1.6;
  margin-bottom: 15px;
  color: #333;
}

.modal-body ul {
  padding-left: 20px;
}

.modal-body li {
  margin-bottom: 8px;
}
</style>
