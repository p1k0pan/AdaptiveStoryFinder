<script setup>
//import posts from '../assets/metadata.json'
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

      <div class="row">
        <div class="col-10">
          
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
        <div class="col-1">

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

export default {
  name: 'showResults',
  data() {
    return {
      results: []
    }
  },

  mounted() {
    this.getData()
  },

  methods: {
    async getData() {
    // do async/promise stuff
    
    
    var someValue = [
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'An item', views: '17.093', date:'09.05.2023',},
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'A second item', views: '17.093', date:'09.05.2023',},
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'A third item', views: '17.093', date:'09.05.2023',},
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'A fourth item', views: '17.093', date:'09.05.2023',},
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'And a fifth one', views: '17.093', date:'09.05.2023',},
                ]
    this.results = someValue
    },
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
</style>