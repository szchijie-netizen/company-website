<template>
  <div class="page-factory">
    <section class="page-header">
      <p class="breadcrumb">Home / Factory</p>
      <h1>Our Operations</h1>
      <p class="subtitle">A modern approach to international trade — built on reliability, transparency, and efficiency.</p>
    </section>

    <section class="strip">
      <div class="strip-inner">
        <div class="strip-item">
          <span class="strip-num">50+</span>
          <span class="strip-label">Partner Factories</span>
        </div>
        <div class="strip-item">
          <span class="strip-num">30+</span>
          <span class="strip-label">Countries Served</span>
        </div>
        <div class="strip-item">
          <span class="strip-num">10K+</span>
          <span class="strip-label">Products Shipped</span>
        </div>
        <div class="strip-item">
          <span class="strip-num">ISO</span>
          <span class="strip-label">Certified Partners</span>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-inner">
        <h2 class="section-head">How We Work</h2>
        <div class="process-grid">
          <div class="process-card">
            <span class="step-num">01</span>
            <h4>Consultation</h4>
            <p>We analyze your requirements, target markets, and specifications to match you with the right suppliers.</p>
          </div>
          <div class="process-card">
            <span class="step-num">02</span>
            <h4>Sourcing & Audit</h4>
            <p>Our team vets factories, negotiates terms, and arranges samples for your approval before production begins.</p>
          </div>
          <div class="process-card">
            <span class="step-num">03</span>
            <h4>Quality Assurance</h4>
            <p>In-line inspections and pre-shipment checks ensure every order meets your specifications and international standards.</p>
          </div>
          <div class="process-card">
            <span class="step-num">04</span>
            <h4>Logistics</h4>
            <p>We handle freight, customs, and final delivery — providing real-time tracking from factory floor to your door.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
.strip { background: var(--color-dark); }
.strip-inner {
  max-width: 1440px; margin: 0 auto;
  display: grid; grid-template-columns: repeat(4, 1fr);
}
.strip-item {
  padding: 56px 40px; text-align: center; border-right: 1px solid #333;
}
.strip-item:last-child { border-right: none; }
.strip-num {
  display: block; font-family: var(--font-serif); font-size: 2rem;
  color: var(--color-accent); margin-bottom: 8px; font-weight: 400;
}
.strip-label {
  font-size: 0.7rem; letter-spacing: 2px; color: var(--color-muted); text-transform: uppercase;
}

.section { padding: 100px 0; background: #fff; }
.section-inner { max-width: 1200px; margin: 0 auto; padding: 0 48px; }
.section-head {
  font-family: var(--font-serif); font-size: 2.6rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 56px; text-align: center;
}
.process-grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px;
  background: var(--color-border);
}
.process-card { background: #fff; padding: 48px; }
.step-num {
  font-size: 0.64rem; letter-spacing: 3px; color: var(--color-accent);
  display: block; margin-bottom: 16px;
}
.process-card h4 {
  font-family: var(--font-serif); font-size: 1.2rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 12px;
}
.process-card p { font-size: 0.9rem; color: #888; line-height: 1.7; }
@media (max-width: 768px) {
  .strip-inner { grid-template-columns: repeat(2, 1fr); }
  .strip-item { border-bottom: 1px solid #333; padding: 36px 20px; }
  .process-grid { grid-template-columns: 1fr; }
  .process-card { padding: 36px 28px; }
  .section { padding: 64px 0; }
  .section-inner { padding: 0 24px; }
}
</style>
