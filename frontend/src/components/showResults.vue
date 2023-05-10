<script setup>
import { useHomeStore } from "../store/modules/home";
//import { RouterLink } from 'vue-router'
import { storeToRefs } from 'pinia'

const { results, loading, error } = storeToRefs(useHomeStore())
const { fetchSearchResults } = useHomeStore()

fetchSearchResults()
</script>

<template>
  <div id="show-results" class="divide-y divide-gray-200">
    <!--<div class="pt-6 pb-8 space-y-2 md:space-y-5">
      <h1
        class="
          text-3xl
          leading-9
          font-extrabold
          text-gray-900
          tracking-tight
          sm:text-4xl sm:leading-10
          md:text-6xl md:leading-14
        "
      >
        {{ $frontmatter.title }}
      </h1>
      <p class="text-lg leading-7 text-gray-500">{{ $frontmatter.subtext }}</p>
    </div> -->
    
    
    
    <div class="container">

      <p v-if="loading">Loading posts...</p>
      <p v-if="error">{{ error.message }}</p>
      
      <div class="row" v-if="results">

        <div class="col-md-auto">
          
          <div class="container">
          </div>

        </div>

        <div class="col-8">
          
          <div class="container">
            <ul class="list-group">
              <li class="py-12" v-for="(item) in results" :key="item-list">

                <div class="card text-bg-white mb-3" style="max-width: 700px;">
                  <div class="row g-0">
                    <div class="col-md-4">
                      <img :src="item.thumbnail" class="img-fluid rounded-start" alt="...">
                    </div>
                    <div class="col-md-8">
                      <div class="card-header ">Header</div>
                      <div class="card-body">
                        <h5 class="card-title"> {{ item.title }}</h5>
                        <p class="card-text"> {{ item.views }} </p>
                        <p class="card-text"><small class="text-body-secondary"> {{ item.date }}</small></p>
                      </div>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>


        </div>
        <div class="col col-lg-2">

          Recommendations

        </div>
      </div>

      <div class="row">
        <div class="col">

        </div>
      </div>
    </div>


    



    <div class="container">

    </div>
    
  </div>
</template>



<script>
// Imports
//import axios from "axios";
//import wikihowapi_pk as wha

export default {
  name: 'showResults',
  data() {
    return {
      results: []
    }
  },

  methods: {
  },
}
</script>





<style>
ul {
  list-style-type: none;
}

.card-img{
   width: 100%!important;
   height: 200px!important;
   object-fit: cover;
}

p {
  margin-bottom: 20px;
  font-size: 20px;
}
button {
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  margin-left: 20px;
  border-radius: 5px;
  color: white;
}

button.increase {
  background-color: green;
}

button.decrease {
  background-color: red;
}
</style>