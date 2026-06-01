import { beforeAll, afterEach, vi } from 'vitest'

// Mock global fetch
global.fetch = vi.fn()

// Mock global localStorage
const localStorageMock = (() => {
  let store = {}
  return {
    getItem: vi.fn(key => store[key] || null),
    setItem: vi.fn((key, value) => {
      store[key] = value.toString()
    }),
    removeItem: vi.fn(key => {
      delete store[key]
    }),
    clear: vi.fn(() => {
      store = {}
    })
  }
})()

Object.defineProperty(window, 'localStorage', {
  value: localStorageMock
})

// Alert is used in some composables, mock it to prevent errors in tests
global.alert = vi.fn()

beforeAll(() => {
  // Any global setup
})

afterEach(() => {
  // Clear mocks after each test to ensure test isolation
  vi.clearAllMocks()
  localStorage.clear()
})
