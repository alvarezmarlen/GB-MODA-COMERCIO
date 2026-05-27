# Tests del Frontend (Idioma)

## Stack de testing
- **Vitest** — test runner
- **@vue/test-utils** — montar componentes Vue
- **happy-dom** — entorno DOM simulado

## Ejecutar tests

```bash
cd frontend
npm test              # una sola ejecución
npm run test:watch    # modo vigilancia (se re-ejecuta al guardar)
```

## Archivos de test

```
tests/
├── i18n/
│   ├── locales.test.js    → verifica que los 5 JSON tengan las mismas claves
│   └── index.test.js      → verifica la instancia de i18n (locale, fallback, localStorage)
└── components/
    └── BaseNavbar.test.js → verifica el selector de idioma en el navbar
```

## Funcionalidad testeada (idioma)
- 5 idiomas: español, inglés, euskera, francés, rumano
- Selector de idioma en el navbar
- Persistencia en localStorage
- Fallback a español si no hay locale guardado

## Cómo agregar nuevos tests
1. Crear el archivo dentro de `tests/` con la misma estructura de carpetas que en `src/`
2. Usar `describe`, `it`, `expect` de `vitest`
3. Ejecutar `npm test` para verificar

Ejemplo mínimo:
```js
import { describe, it, expect } from 'vitest'

describe('Mi funcionalidad', () => {
  it('debería funcionar', () => {
    expect(1 + 1).toBe(2)
  })
})
```
