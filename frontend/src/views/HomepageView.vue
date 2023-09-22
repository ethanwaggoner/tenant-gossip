<script setup>
import SemiCircle from "@/components/SemiCircle.vue";
import HomepageSummary from "@/components/HomepageSummary.vue";
</script>

<template>
  <div class="container">
    <SemiCircle />
    <img class="logo" src="src/assets/logo2.png" alt="logo">
  </div>
  <HomepageSummary />

</template>

<style scoped>
.container {
  top: 45px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

img {
  border-radius: 10px;
  border: #1a1a1a 2px solid;
  position: relative;
  height: 250px;
  width: auto;
}
</style>