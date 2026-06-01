import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'
import CreateStoryView from '../views/CreateStoryView.vue'
import StoryDetailView from '../views/StoryDetailView.vue'
import HomeView from '../views/HomeView.vue'
import UserDashboardView from '../views/UserDashboardView.vue'
import AdminDashboardView from '../views/AdminDashboardView.vue'
import { useAuthStore } from '../composables/useAuthStore'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterPage
  },
  {
    path: '/create-story',
    name: 'create-story',
    component: CreateStoryView
  },
  {
    path: '/story-detail/:id',
    name: 'story-detail',
    component: StoryDetailView
  },
  {
    path: '/dashboard',
    name: 'user-dashboard',
    component: UserDashboardView
  },
  {
    path: '/admin',
    name: 'admin-dashboard',
    component: AdminDashboardView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  const publicPages = ['/', '/login', '/register']
  const guestOnlyPages = ['/login', '/register']
  const authRequired = !publicPages.includes(to.path)

  // Auth guard: redirect unauthenticated users to login
  if (authRequired && !authStore.token) {
    next('/login')
  // Admin guard: non-admin users redirected from /admin to /dashboard
  } else if (to.path.startsWith('/admin') && authStore.user?.role !== 'admin') {
    next('/dashboard')
  // Guest guard: redirect logged-in users away from login/register
  } else if (guestOnlyPages.includes(to.path) && authStore.token) {
    next('/')
  } else {
    next()
  }
})

export default router
