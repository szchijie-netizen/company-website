<template>
  <div class="page-customization">
    <section class="page-header">
      <p class="breadcrumb">Home / Customization</p>
      <h1>Custom Sourcing</h1>
      <p class="subtitle">Tailored procurement solutions for brands that demand consistency, quality, and competitive pricing.</p>
    </section>

    <section class="section">
      <div class="section-inner">
        <div class="intro">
          <h2>Built Around Your Business</h2>
          <p>Whether you need a single product line sourced or a full supply chain built, our team adapts to your requirements. We work with startups launching their first product and established brands scaling into new categories.</p>
        </div>
      </div>
    </section>

    <section class="section alt">
      <div class="section-inner">
        <h2 class="section-head">Service Capabilities</h2>
        <div class="cap-grid">
          <div class="cap-card">
            <h4>OEM Manufacturing</h4>
            <p>We coordinate with factories to produce goods under your brand, exactly to your specifications — from packaging design to material sourcing.</p>
          </div>
          <div class="cap-card">
            <h4>ODM Design Support</h4>
            <p>Have an idea but no technical drawings? Our partner factories offer design services to bring your concepts to market-ready products.</p>
          </div>
          <div class="cap-card">
            <h4>Private Label</h4>
            <p>Select from existing product lines and apply your branding. A faster path to market with lower minimum order quantities.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="section-inner">
        <h2 class="section-head">The Process</h2>
        <div class="workflow">
          <div class="wf-step">
            <span class="wf-num">1</span>
            <div>
              <h4>Brief & Feasibility</h4>
              <p>Share your requirements. We evaluate and respond with supplier options within 48 hours.</p>
            </div>
          </div>
          <div class="wf-step">
            <span class="wf-num">2</span>
            <div>
              <h4>Sampling & Refinement</h4>
              <p>Approve samples, iterate on details, and lock in final specifications before mass production.</p>
            </div>
          </div>
          <div class="wf-step">
            <span class="wf-num">3</span>
            <div>
              <h4>Production & QC</h4>
              <p>Full-scale manufacturing with weekly updates and multi-stage quality inspections.</p>
            </div>
          </div>
          <div class="wf-step">
            <span class="wf-num">4</span>
            <div>
              <h4>Delivery</h4>
              <p>Final inspection, secure packaging, and worldwide shipping with complete documentation.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
</script>

<style scoped>
.section { padding: 100px 0; background: #fff; }
.section.alt { background: var(--color-cream); }
.section-inner { max-width: 1200px; margin: 0 auto; padding: 0 48px; }
.section-head {
  font-family: var(--font-serif); font-size: 2.6rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 56px; text-align: center;
}

.intro { max-width: 720px; margin: 0 auto; text-align: center; }
.intro h2 {
  font-family: var(--font-serif); font-size: 2.2rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 20px;
}
.intro p { font-size: 1rem; color: #888; line-height: 1.8; }

.cap-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px;
  background: var(--color-border);
}
.cap-card { background: #fff; padding: 48px; }
.cap-card h4 {
  font-family: var(--font-serif); font-size: 1.2rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 12px;
}
.cap-card p { font-size: 0.9rem; color: #888; line-height: 1.7; }

.workflow { max-width: 720px; margin: 0 auto; }
.wf-step {
  display: flex; gap: 28px; padding: 32px 0; border-bottom: 1px solid var(--color-border);
}
.wf-step:last-child { border-bottom: none; }
.wf-num {
  flex-shrink: 0; width: 48px; height: 48px;
  border: 1px solid var(--color-accent); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.9rem; color: var(--color-accent); font-family: var(--font-serif);
}
.wf-step h4 {
  font-family: var(--font-serif); font-size: 1.05rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 6px;
}
.wf-step p { font-size: 0.9rem; color: #888; line-height: 1.7; }
@media (max-width: 768px) {
  .section { padding: 64px 0; }
  .section-inner { padding: 0 24px; }
  .cap-grid { grid-template-columns: 1fr; }
  .cap-card { padding: 36px 28px; }
}
</style>
