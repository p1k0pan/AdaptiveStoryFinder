// import { createApp } from 'vue'
// createApp(App).mount('#app')



//import vuetify from './plugins/vuetify'
//import Vuesax from 'vuesax'
//import 'vuesax/dist/vuesax.css' //Vuesax styles

//Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js'
//import 'bootstrap-vue/dist/bootstrap-vue.css'
//import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'

//import '@/assets/css/tailwind.css'
import axios from 'axios'
import VueAxios from 'vue-axios'


// "http://localhost:8000"

// Make Vuesax available throughout your project
//Vue.use(Vuesax)
// Make BootstrapVue available throughout your project
//Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
//Vue.use(IconsPlugin)

import { createApp } from 'vue'
import App from './App.vue'
// uncomment 
//import router from './router'
//import store from './store'


/*new Vue({
        //router,
        //axios,
        //store,
        //vuetify,
        render: h => h(App)
}).$mount('#app');*/

//eslint-disable-next-line
const app = createApp(App)
app.use(bootstrap)
app.use(VueAxios, axios) // 👈
app.mount('#app')
//const app = createApp(App).use(store).use(router).mount('#app')
console.log(app)

app.config.warnHandler = function (msg, vm, trace) {
  msg, vm, trace = null
  return trace
}
//Vue.config.productionTip = false

app.config.globalProperties.$filters = {
    uppercase(value) {
      return value.toUpperCase()
    }
  }
//Vue.filter('uppercase', function (value){
//        return value.toUpperCase()
//});