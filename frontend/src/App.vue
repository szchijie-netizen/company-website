<script setup>
</script>

<template>
  <div id="app">
    <header class="nav-header">
      <div class="nav-inner">
        <router-link to="/" class="logo-link">
          <img src="./assets/logo.png" alt="Shenzhen Chijie International Trade Co., Ltd." class="logo-img">
        </router-link>
        <nav>
          <router-link to="/">Home</router-link>
          <router-link to="/products">Products</router-link>
          <router-link to="/factory">Factory</router-link>
          <router-link to="/customization">Customization</router-link>
          <router-link to="/contact">Contact</router-link>
        </nav>
      </div>
    </header>
    <main>
      <router-view />
    </main>
    <footer class="site-footer">
      <div class="footer-inner">
        <div class="footer-info">
          <p class="footer-co">Shenzhen Chijie International Trade Co., Ltd.</p>
          <p class="footer-addr">A1813, Tang Shang Building, 35 Xinqiao Section, Guangshen Road, Bao''an District, Shenzhen</p>
        </div>
        <p class="footer-copy">&#169; 2026 All Rights Reserved.</p>
      </div>
    </footer>
  </div>
</template>
