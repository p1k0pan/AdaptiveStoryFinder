import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import 'jquery/src/jquery.js';
// import 'popper.js/dist/popper.min.js';

import PrimeVue from 'primevue/config'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
// Vuetify
Vue.use(PrimeVue)
// PrimeVue
Vue.use(PrimeVue)

// theme
// import 'primevue/resources/themes/lara-light-indigo/theme.css'
// core
// import 'primevue/resources/primevue.min.css'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
