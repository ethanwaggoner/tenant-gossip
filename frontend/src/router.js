import { createWebHistory, createRouter } from 'vue-router'

import HomepageView from "@/views/HomepageView.vue";
import TermsAgreementView from "@/views/TermsAgreementView.vue";
import ResourcesView from "@/views/ResourcesView.vue";
import ForumsCategoriesView from "@/views/ForumsCategoriesView.vue";
import ForumsPostsView from "@/views/ForumsPostsView.vue";


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
    {
      path: '/forums',
      name: 'Forums',
      component: ForumsCategoriesView,
    },
    {
      path: '/forums/:category_id',
      name: 'Posts',
      component: ForumsPostsView,
    },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router