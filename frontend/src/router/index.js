import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import Login from '@/views/Login.vue'
import Projects from '@/views/projects/Projects.vue'
import ProjectsCreate from '@/views/projects/ProjectCreate.vue'
import GuideProducts from '@/views/guide/Products.vue'
import CreateGuideProduct from '@/views/guide/ProductCreate.vue'
import EditGuideProduct from '@/views/guide/ProductEdit.vue'
import GuidePartners from '@/views/guide/Partners.vue'
import GuideProviders from '@/views/guide/Providers.vue'
import GuideSpecifications from '@/views/guide/Specifications.vue'

import { getItem } from '@/tools/persistanceStorage.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/projects',
      name: 'projects',
      component: Projects,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/projects/create',
      name: 'project-create',
      component: ProjectsCreate,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/guide/products',
      name: 'guide-products',
      component: GuideProducts,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/guide/products/create',
      name: 'guide-products-create',
      component: CreateGuideProduct,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/guide/products/:id/edit',
      name: 'guide-products-edit',
      component: EditGuideProduct,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/guide/partners',
      name: 'guide-partners',
      component: GuidePartners,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/guide/providers',
      name: 'guide-providers',
      component: GuideProviders,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/guide/specifications',
      name: 'guide-specifications',
      component: GuideSpecifications,
      meta: {
        requiresAuth: true,
      }
    },
  ]
})

// TODO: (bug) need submit twice on login page
router.beforeEach((to, from, next) => {
  const userIsAuthenticated = Boolean(getItem('accessToken'))
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (userIsAuthenticated) {
      next()
    } else next('login')
  } else if (
    userIsAuthenticated && (to.name == 'login' || to.name == 'register')
  ) {
    next('/')
  } else next()
})

export default router
