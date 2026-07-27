<template>
  <div class="page-home">
    <section class="hero">
      <div class="hero-inner">
        <p class="hero-tag">Shenzhen · China</p>
        <h1>Global Trade,<br>Trusted Partnership</h1>
        <p class="hero-desc">Shenzhen Chijie International Trade Co., Ltd. — connecting markets worldwide with reliable sourcing, quality assurance, and seamless logistics since our founding.</p>
        <div class="hero-links">
          <router-link to="/products" class="btn-dark">Explore Products</router-link>
          <router-link to="/contact" class="btn-line">Get in Touch</router-link>
        </div>
      </div>
    </section>

    <section class="strip">
      <div class="strip-inner">
        <div class="strip-item">
          <p class="strip-num">24/7</p>
          <p class="strip-label">Service Availability</p>
        </div>
        <div class="strip-item">
          <p class="strip-num">China-Wide</p>
          <p class="strip-label">Sourcing Network</p>
        </div>
        <div class="strip-item">
          <p class="strip-num">100%</p>
          <p class="strip-label">Quality Commitment</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-inner">
        <h2 class="section-head">What We Offer</h2>
        <div class="offer-grid">
          <div class="offer-card">
            <h4>Product Sourcing</h4>
            <p>End-to-end procurement from verified Chinese manufacturers across electronics, hardware, and consumer goods.</p>
          </div>
          <div class="offer-card">
            <h4>Quality Control</h4>
            <p>Rigorous inspection protocols at every stage — factory audits, in-line checks, and pre-shipment verification.</p>
          </div>
          <div class="offer-card">
            <h4>Logistics & Shipping</h4>
            <p>Sea, air, and rail freight solutions with full customs clearance and door-to-door delivery options.</p>
          </div>
          <div class="offer-card">
            <h4>Brand Development</h4>
            <p>OEM and ODM services for clients looking to build or expand their own product lines under their brand.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="cta-block">
      <div class="cta-inner">
        <h2>Let''s Work Together</h2>
        <p>We partner with distributors, retailers, and brands of all sizes. Reach out to discuss your next project.</p>
        <router-link to="/contact" class="btn-dark">Start a Conversation</router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
/* ── Hero ── */
.hero {
  min-height: 92vh;
  display: flex; align-items: center;
  background: var(--color-cream);
  padding: 0;
}
.hero-inner {
  max-width: 1440px; margin: 0 auto; padding: 120px 80px;
  width: 100%;
}
.hero-tag {
  font-size: 0.7rem; letter-spacing: 4px; color: var(--color-accent);
  text-transform: uppercase; margin-bottom: 28px;
}
.hero h1 {
  font-family: var(--font-serif); font-size: 4.8rem; font-weight: 400;
  line-height: 1.1; color: var(--color-dark); margin-bottom: 32px;
  letter-spacing: -1px; max-width: 800px;
}
.hero-desc {
  font-size: 1.05rem; line-height: 1.8; color: #777;
  margin-bottom: 48px; max-width: 560px;
}
.hero-links { display: flex; gap: 20px; }

/* ── Shared buttons ── */
.btn-dark {
  display: inline-block; padding: 15px 38px;
  background: var(--color-dark); color: #fff;
  text-decoration: none; font-size: 0.82rem; letter-spacing: 1.5px;
  text-transform: uppercase; transition: background 0.25s ease;
}
.btn-dark:hover { background: #333; }
.btn-line {
  display: inline-block; padding: 15px 38px;
  border: 1px solid #ccc; color: var(--color-dark);
  text-decoration: none; font-size: 0.82rem; letter-spacing: 1.5px;
  text-transform: uppercase; transition: border-color 0.25s ease, color 0.25s ease;
}
.btn-line:hover { border-color: var(--color-dark); color: var(--color-dark); }

/* ── Strip ── */
.strip {
  background: var(--color-dark); color: var(--color-text);
  padding: 0;
}
.strip-inner {
  max-width: 1440px; margin: 0 auto; display: grid;
  grid-template-columns: repeat(3, 1fr);
}
.strip-item {
  padding: 52px 48px; text-align: center;
  border-right: 1px solid #333;
}
.strip-item:last-child { border-right: none; }
.strip-num {
  font-family: var(--font-serif); font-size: 2rem; color: var(--color-accent);
  margin-bottom: 8px; font-weight: 400;
}
.strip-label {
  font-size: 0.72rem; letter-spacing: 2px; color: var(--color-muted);
  text-transform: uppercase;
}

/* ── Sections ── */
.section { padding: 100px 0; background: #fff; }
.section-inner { max-width: 1200px; margin: 0 auto; padding: 0 48px; }
.section-head {
  font-family: var(--font-serif); font-size: 2.6rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 56px; text-align: center;
  letter-spacing: -0.5px;
}

/* ── Offer grid ── */
.offer-grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px;
  background: var(--color-border);
}
.offer-card {
  background: #fff; padding: 52px 48px;
}
.offer-card h4 {
  font-family: var(--font-serif); font-size: 1.3rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 12px;
}
.offer-card p {
  font-size: 0.9rem; color: #888; line-height: 1.7;
}

/* ── CTA ── */
.cta-block { background: var(--color-cream); }
.cta-inner {
  max-width: 720px; margin: 0 auto; padding: 100px 48px;
  text-align: center;
}
.cta-inner h2 {
  font-family: var(--font-serif); font-size: 2.6rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 20px; letter-spacing: -0.5px;
}
.cta-inner p {
  font-size: 1rem; color: #888; line-height: 1.7;
  margin-bottom: 36px;
}

@media (max-width: 768px) {
  .hero-inner { padding: 80px 24px; }
  .hero h1 { font-size: 2.8rem; }
  .hero-links { flex-direction: column; }
  .strip-inner { grid-template-columns: 1fr; }
  .strip-item { border-right: none; border-bottom: 1px solid #333; padding: 36px 24px; }
  .strip-item:last-child { border-bottom: none; }
  .offer-grid { grid-template-columns: 1fr; }
  .offer-card { padding: 36px 28px; }
  .section { padding: 64px 0; }
  .section-inner { padding: 0 24px; }
  .cta-inner { padding: 64px 24px; }
}
</style>
