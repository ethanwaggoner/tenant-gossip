<script setup>

</script>

<template>
  <div class="container">
    <nav>
      <div class="nav-links">
        <router-link to="/" style="text-decoration: none; color: inherit;">
          <a><h2 href=#>Home</h2></a>
        </router-link>
        <div class="divider"></div>
        <router-link to="/resources" style="text-decoration: none; color: inherit;">
        <h2 href=#>Tenant Resources</h2>
        </router-link>
        <div class="divider"></div>
        <h2 href=#>Read Reviews</h2>
        <div class="divider"></div>
        <router-link to="/terms" style="text-decoration: none; color: inherit;">
          <h2>Forums</h2>
        </router-link>
        <div class="divider"></div>
        <router-link to="/terms" style="text-decoration: none; color: inherit;">
          <h2>Write a Review</h2>
        </router-link>
      </div>
    </nav>
  </div>
</template>

<style scoped>
.container {
  width: 70vw;
}
nav {
  background: linear-gradient(180deg, #4FC0D0, #1B6B93);
  opacity: 1.0;
  color: antiquewhite;
  font-weight: 800;
  display: flex;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  margin-top: 10px;
  font-family: Candara, sans-serif;
  border: #1a1a1a 2px solid;

}

.nav-links {
  display: flex;
  justify-content: center;
  width: 100%;
}

img {
  width: 100px;
  height: 100px;
}

h2, router-link {
  padding: 15px;
  font-size: 25px;
  margin: 0;
  transition: color 0.3s;
}

h2.active {
  color: #A2FF86;
}

h2:hover {
  color: #A2FF86;
  cursor: pointer;
}

.divider {
  border-right: 2px solid #1a1a1a;
}

</style>