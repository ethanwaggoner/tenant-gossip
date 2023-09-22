<script setup>

</script>

<template>
<div class="container">
  <h1>Terms and Conditions</h1>

  <p>By using the Tenant Gossip website and services, you agree to the following terms and conditions:</p>

  <h2>Reviews and Forum Conduct</h2>

  <ul>
    <li>Reviews and forum posts must be based on first-hand experiences with a landlord or property. Do not post hearsay or rumors.</li>

    <li>Keep reviews and discussions civil. Do not use profane, offensive, or discriminatory language. Any hate speech will be removed.</li>

    <li>Do not threaten or incite harm against others. Comments intended to harass or intimidate will not be tolerated.</li>

    <li>Do not post private contact information or addresses without permission. Always respect others' privacy.</li>

    <li>We reserve the right to remove any review or post deemed inappropriate or that violates site rules.</li>
  </ul>

  <h2>Liability</h2>

  <ul>
    <li>Tenant Gossip is not liable for any interactions between users occurring offline or independently of our website. We do not endorse or investigate users.</li>

    <li>Opinions expressed on Tenant Gossip are solely those of individual users. Reviews and forum posts do not represent the views of Tenant Gossip.</li>

    <li>Users are legally responsible for their own content. Do not post anything defamatory, libelous, offensive, or illegal.</li>
  </ul>

  <h2>Intellectual Property</h2>

  <ul>
    <li>All content posted remains the intellectual property of the original author. Do not plagiarize or copy others' work.</li>

    <li>By posting on Tenant Gossip, you grant us a non-exclusive license to display your content. We reserve the right to modify or remove content when necessary.</li>
  </ul>

  <p>Violating these terms can lead to account suspension or banning at our discretion. Please contact us if you have any questions.</p>

  <div class="buttons">
    <router-link to="/" style="text-decoration: none; color: inherit;">
      <div class="back-button">Back</div>
    </router-link>
    <div class="agree-button">Agree</div>
  </div>
</div>
</template>

<style scoped>
.container {
  color: antiquewhite;
  font-size: 18px;
  font-family: Candara, sans-serif;
  padding: 50px 100px 0 100px;
  opacity: 1.0;
  position: relative;
  width: 1000px;
  height: 90vh;
  background: linear-gradient(180deg, #4FC0D0, #1B6B93);
  border: #1a1a1a 2px solid;
  overflow-y: auto;
}

.buttons {
  display: inline-flex;
  justify-content: center;

}
.agree-button {
  margin-left: 600px;
  background: linear-gradient(to bottom, #4FC0D0, #1B6B93);
  color: antiquewhite;
  font-size: 24px;
  padding: 20px 20px 0 20px;
  border-radius: 10px;
  border: #1a1a1a 2px solid;
}

.back-button {
  background: linear-gradient(to bottom, #4FC0D0, #1B6B93);
  color: antiquewhite;
  font-size: 24px;
  padding: 20px 20px 20px 20px;
  border-radius: 10px;
  border: #1a1a1a 2px solid;

}
.back-button:hover {
  color: #A2FF86;
  cursor: pointer;
}
.agree-button:hover {
  color: #A2FF86;
  cursor: pointer;
}
</style>