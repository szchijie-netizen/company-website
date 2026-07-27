<template>
  <div class="page-products">
    <section class="page-header">
      <p class="breadcrumb">Home / Products</p>
      <h1>Our Product Range</h1>
      <p class="subtitle">Specialized in premium eyewear, luxury watches, and smart accessories — backed by verified manufacturing partners and rigorous quality standards.</p>
    </section>

    <section class="section">
      <div class="section-inner">
        <div class="product-grid">
          <div class="product-card" v-for="p in products" :key="p.name">
            <div class="product-badge">{{ p.category }}</div>
            <h4>{{ p.name }}</h4>
            <p>{{ p.desc }}</p>
          </div>
        </div>
        <p class="retail-note">All products available for retail and wholesale.</p>
      </div>
    </section>
  </div>
</template>

<script setup>
const products = [
  { name: "Luxury Watches", category: "Timepieces", desc: "完全中国制造，保证100%还原。甚至于我们的手表质量更高细节更好，让您花费极小的金钱，买来那些你耳熟能详的手表。" },
  { name: "Eyeglass Frames", category: "Optical", desc: "Handcrafted frames in acetate, pure titanium, precious metal (gold/platinum), TR90 polymer, natural wood, and carbon fiber — lightweight, hypoallergenic, and precision-engineered." },
  { name: "Sunglasses", category: "Eyewear", desc: "Polarized and UV400 protection lenses in premium frames. Classic aviators, wayfarers, cat-eye, and sport wraparound styles with mirror, gradient, and photochromic options." },
  { name: "Smart Glasses", category: "Tech", desc: "Bluetooth-enabled smart eyewear with open-ear audio, voice assistant integration, UV protection lenses, 1080p video recording, and all-day battery life — where fashion meets functionality." },
]
</script>

<style scoped>
.section { padding: 80px 0; background: #fff; }
.section-inner { max-width: 1200px; margin: 0 auto; padding: 0 48px; }
.product-grid {
  display: grid; grid-template-columns: repeat(2, 1fr);
  gap: 1px; background: var(--color-border);
}
.product-card {
  background: #fff; padding: 48px 40px;
  transition: background 0.25s ease;
}
.product-card:hover { background: var(--color-cream); }
.product-badge {
  font-size: 0.64rem; letter-spacing: 2.5px; color: var(--color-accent);
  text-transform: uppercase; margin-bottom: 20px;
}
.product-card h4 {
  font-family: var(--font-serif); font-size: 1.2rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 12px;
}
.product-card p {
  font-size: 0.88rem; color: #888; line-height: 1.7;
}
.retail-note {
  text-align: center; font-size: 0.85rem; color: var(--color-accent);
  margin-top: 40px; letter-spacing: 0.5px;
}
@media (max-width: 768px) {
  .section-inner { padding: 0 24px; }
  .product-grid { grid-template-columns: 1fr; }
  .product-card { padding: 36px 28px; }
  .retail-note { margin-top: 28px; }
}
</style>
