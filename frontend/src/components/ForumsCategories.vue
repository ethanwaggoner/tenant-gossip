<script setup>
import { ref, onMounted } from "vue";

const categories = ref([]);

const fetchCategories = async () => {
  try {
    let response = await fetch("http://127.0.0.1:5001/forums/categories");
    if (response.ok) {
      const data = await response.json();
      categories.value = data.results;
    } else {
      console.log("error");
    }
  } catch (error) {
    console.log(error);
  }
}

onMounted(() => {
  fetchCategories();
});
</script>

<template>
<div class="container-fluid h-100">
  <div class="row justify-content-center h-100">
    <div class="col-8 d-flex flex-column">
      <div v-for="category in categories" :key="category.category_id" class="category-card mb-4">
         <router-link :to="{ name: 'Posts', params: { category_id: category.category_id}}" style="text-decoration: none; color: inherit;">
           <div>
            <h5>⬤ {{ category.name }}</h5>
            <p>{{ category.description }}</p>
            <small>{{ category.number_of_threads }} threads</small>
           </div>
         </router-link>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>
.category-card {
  background: linear-gradient(180deg, #4FC0D0, #1B6B93);
  border: #1a1a1a 2px solid;
  color: white;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  transition: 0.3s;
}

.category-card:hover {
  background: linear-gradient(180deg, #1B6B93, #4FC0D0);
  transform: scale(1.02);
  box-shadow: 0 8px 12px rgba(0,0,0,0.3);
}

h5 {
  font-weight: bold;
}

.container-fluid {
  padding: 40px 0 0;
}
</style>
