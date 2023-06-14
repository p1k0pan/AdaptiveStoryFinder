<template>
  <div>
    <hello-world />
    
    <h1> Test Vuetify </h1>
    <v-file-input
      multiple
      label="File input"
    ></v-file-input>

    <h1> Test Bootstrap</h1>
    <div class="mb-3">
      <label for="formFileSm" class="form-label">Small file input example</label>
      <input class="form-control form-control-sm" id="formFileSm" type="file">
    </div>

    <h1> Test PrimeVue</h1>
    <div class="card flex justify-content-center">
        <FileUpload mode="basic" name="demo[]" url="./upload.php" accept="image/*" :maxFileSize="1000000" @upload="onUpload" />
    </div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  // import { useToast } from "primevue/usetoast";
  // const toast = useToast();
  import HelloWorld from '../components/HelloWorld.vue'

  import FileUpload from 'primevue/fileupload';


  export default Vue.extend({
    name: 'Home',

    components: {
      HelloWorld,
      
      FileUpload,
    },

    data () {
      return {
      }
    },
    beforeMount () {
      // this.fetch()
    },
    methods: {
      onUpload: () => {
        console.log("upload file")
      },
      fetch () {
        this.$store.dispatch('websocketChangeFunctionality', 'all vaccinations')
      }
    }
  })
</script>
