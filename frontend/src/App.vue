<template>
  <!---<img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>-->

  <div>
        <show-blogs></show-blogs>
        <!---<home></home>-->
  </div>
  <div>
        <show-results></show-results>
  </div>

</template>

<script>
// Imports
//import HelloWorld from './components/HelloWorld.vue'
import showBlogs from './components/showBlogs.vue';
import showResults from './components/showResults.vue';
//import home from './views/home-page.vue';

export default {
  name: 'App',
  components: {
    //HelloWorld,
    'show-blogs': showBlogs,
    'show-results': showResults,
    //'home': home,
  },
  data() {
    return {

    }
  },
  methods: {

  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

body{
    margin: 0;
    font-family: 'Nunito SemiBold';
}
</style>
