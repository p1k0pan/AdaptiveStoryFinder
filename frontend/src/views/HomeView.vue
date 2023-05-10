<template>
  <div>
    <div id="app">
      <NavigationMobile />
      <div class="content" :class="{'open':showNav}">
        <div class="top-bar">
          <Navigation v-if="!mobileView" />
        </div>
        <Content />
      </div>
    </div>
  </div>
  <div>
        <RankingResults></RankingResults>
  </div>
</template>

<script lang="ts">
// Imports
import { defineComponent } from "vue";
//import Navigation from "@/components/NavigationBar.vue";
import RankingResults from '@/components/showResults.vue';
//import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src

export default defineComponent({
  name: "HomeView",
  components: {
    //Navigation,
    RankingResults,
  },
  data: () => {
    return {
      mobileView: true,
      showNav: false
    };
  },
  methods: {
    handleView() {
      this.mobileView = window.innerWidth <= 990;
    }
  },

  created() {
    this.handleView();
    window.addEventListener('resize', this.handleView);
  },
});
</script>


<style lang="scss">
@import url("https://use.fontawesome.com/releases/v5.9.0/css/all.css");
* {
  font-size: 1rem;
}
body {
  width: 100%;
  height: 100vh;
  margin: 0;
  padding: 0;
  font-family: "Segoe UI", Tahoma;
  background-color: #7ca971;
}
.top-bar {
  display: flex;
  width: 100%;
}
#navigation-icon {
  padding: 10px 10px 20px;
  margin-right: 10px;
  cursor: pointer;
  i {
    font-size: 2rem;
  }
}
.open {
  transform: translateX(300px);
}
</style>