import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import Login from '@/views/Login.vue'

import Projects from '@/views/projects/Projects.vue'
import ProjectsCreate from '@/views/projects/ProjectCreate.vue'
import ProjectsEdit from '@/views/projects/ProjectEdit.vue'

import GuideProducts from '@/views/guide/products/Products.vue'
import CreateGuideProduct from '@/views/guide/products/ProductCreate.vue'
import EditGuideProduct from '@/views/guide/products/ProductEdit.vue'

import GuidePartners from '@/views/guide/partners/Partners.vue'
import CreateGuidePartner from '@/views/guide/partners/PartnerCreate.vue'
import EditGuidePartner from '@/views/guide/partners/PartnerEdit.vue'

import GuideProviders from '@/views/guide/providers/Providers.vue'
import GuideSpecifications from '@/views/guide/specifications/Specifications.vue'

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

    // PROJECTS
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
      path: '/projects/:id/edit',
      name: 'project-edit',
      component: ProjectsEdit,
      meta: {
        requiresAuth: true,
      }
    },

    // PRODUCTS
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

    // PARTNERS
    {
      path: '/guide/partners',
      name: 'guide-partners',
      component: GuidePartners,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/guide/partners/create',
      name: 'guide-partners-create',
      component: CreateGuidePartner,
      meta: {
        requiresAuth: true,
      }
    },
    {
      path: '/guide/partners/:id/edit',
      name: 'guide-partners-edit',
      component: EditGuidePartner,
      meta: {
        requiresAuth: true,
      }
    },

    // PROVIDERS
    {
      path: '/guide/providers',
      name: 'guide-providers',
      component: GuideProviders,
      meta: {
        requiresAuth: true,
      }
    },

    // SPECIFICATIONS
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
