import { createWebHistory, createRouter } from 'vue-router'

import HomepageView from "@/views/HomepageView.vue";
import TermsAgreementView from "@/views/TermsAgreementView.vue";
import ResourcesView from "@/views/ResourcesView.vue";


const routes = [
    {
      path: '/',
      name: 'Home',
      component: HomepageView,
    },
    {
      path: '/terms',
      name: 'Terms',
      component: TermsAgreementView,
    },
    {
      path: '/resources',
      name: 'Resources',
      component: ResourcesView,
    },


]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router