// Setup Function
import { defineStore } from "pinia";
//import wikihowapi_pk as wha;
//import wikihowunofficialapi as wha

//import { ref, computed } from 'vue' // reactive,

export const useHomeStore = defineStore({
  id: 'home',
  state: () => ({
    results: [],
    post: null,
    loading: false,
    error: null
  }),
  getters: {
    getPostsPerAuthor: (state) => {
      return (authorId) => state.results.filter((post) => post.userId === authorId)
    }
  }, 
  actions: {
    async fetchSearchResults(query) {
      // do async/promise stuff
    
    //how_tos: list = wha.search_wikihow_link("housing bubble")
    //return JsonResponse({"results": how_tos})
      var someValue = [
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'An item', views: '17.093', date:'09.05.2023',},
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'A second item', views: '17.093', date:'09.05.2023',},
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'A third item', views: '17.093', date:'09.05.2023',},
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'A fourth item', views: '17.093', date:'09.05.2023',},
                 {thumbnail:'http://www.snut.fr/wp-content/uploads/2015/08/image-de-paysage.jpg', title:'And a fifth one', views: '17.093', date:'09.05.2023',},
                ]
      this.results = someValue
    //this.results = how_tos
    },

    /*async fetchPosts() {
      this.posts = []
      this.loading = true
      try {
        this.posts = await fetch('https://jsonplaceholder.typicode.com/posts')
        .then((response) => response.json()) 
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    },
    async fetchPost(id) {
      this.post = null
      this.loading = true
      try {
        this.post = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`)
        .then((response) => response.json())
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    }*/
  }
})