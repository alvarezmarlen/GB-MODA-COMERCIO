import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'
import CreateStoryView from '../views/CreateStoryView.vue'
import StoryDetailView from '../views/StoryDetailView.vue'
import HomeView from '../views/HomeView.vue'
import UserDashboardView from '../views/UserDashboardView.vue'
import AdminDashboardView from '../views/AdminDashboardView.vue'

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
    path: '/story-detail',
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
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
