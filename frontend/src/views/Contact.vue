<template>
  <div class="page-contact">
    <section class="page-header">
      <p class="breadcrumb">Home / Contact</p>
      <h1>Get in Touch</h1>
      <p class="subtitle">We welcome inquiries from distributors, retailers, and brands worldwide.</p>
    </section>

    <section class="contact-body">
      <div class="contact-info">
        <div class="info-block">
          <h4>Address</h4>
          <p>
            A1813, Tang Shang Building<br>
            35 Xinqiao Section, Guangshen Road<br>
            Shangxing Community, Xinqiao Street<br>
            Bao''an District, Shenzhen
          </p>
        </div>
        <div class="info-block">
          <h4>Contact</h4>
          <p>
            Tel: +86 18631076789<br>
            Email: szchijie@gmail.com<br>
            WhatsApp: +852 54654752
          </p>
        </div>
        <div class="info-block">
          <h4>Hours</h4>
          <p>24/7 — Available Around the Clock</p>
          <p class="note">GMT+8 · We respond to all inquiries within 24 hours.</p>
        </div>
      </div>

      <div class="contact-form">
        <h3>Send a Message</h3>
        <form @submit.prevent="handleSubmit">
          <div class="form-row">
            <div class="form-group">
              <input id="name" v-model="form.name" type="text" required placeholder="Full Name" :disabled="submitting">
            </div>
            <div class="form-group">
              <input id="company" v-model="form.company" type="text" placeholder="Company" :disabled="submitting">
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <input id="email" v-model="form.email" type="email" required placeholder="Email Address" :disabled="submitting">
            </div>
            <div class="form-group">
              <input id="phone" v-model="form.phone" type="tel" placeholder="Phone / WhatsApp" :disabled="submitting">
            </div>
          </div>
          <div class="form-group full">
            <select id="inquiry" v-model="form.inquiryType" :disabled="submitting">
              <option value="">Inquiry Type</option>
              <option value="sourcing">Product Sourcing</option>
              <option value="oem">OEM / ODM</option>
              <option value="logistics">Logistics & Shipping</option>
              <option value="wholesale">Wholesale / Distribution</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div class="form-group full">
            <textarea id="message" v-model="form.message" required placeholder="Tell us about your project, requirements, and timeline..." rows="5" :disabled="submitting"></textarea>
          </div>
          <button type="submit" class="btn-dark full-width" :disabled="submitting">
            {{ submitting ? 'Sending...' : 'Send Inquiry' }}
          </button>
        </form>
        <p v-if="submitError" class="form-error">{{ submitError }}</p>
        <p v-if="submitted" class="form-success">Thank you. Our team will contact you within 24 hours.</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive } from "vue"
import axios from "axios"

const form = reactive({
  name: "", company: "", email: "", phone: "", inquiryType: "", message: "",
})
const submitting = ref(false)
const submitted = ref(false)
const submitError = ref("")

async function handleSubmit() {
  if (submitting.value) return
  submitError.value = ""
  submitting.value = true
  try {
    const apiBase = import.meta.env.VITE_API_URL || ''
    await axios.post(`${apiBase}/api/contact/`, {
      name: form.name,
      company: form.company,
      email: form.email,
      phone: form.phone,
      inquiry_type: form.inquiryType || undefined,
      message: form.message,
    })
    submitted.value = true
    Object.assign(form, { name: "", company: "", email: "", phone: "", inquiryType: "", message: "" })
  } catch (err) {
    const data = err.response?.data
    if (data && typeof data === "object") {
      // 提取 DRF 错误信息的第一条
      const msgs = Object.values(data).flat()
      submitError.value = msgs[0] || "Submission failed. Please try again."
    } else {
      submitError.value = "Network error. Please check your connection and try again."
    }
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.contact-body {
  display: grid; grid-template-columns: 1fr 1.2fr; gap: 80px;
  max-width: 1200px; margin: 0 auto; padding: 80px 48px;
}
.contact-info { display: flex; flex-direction: column; gap: 40px; }
.info-block h4 {
  font-size: 0.7rem; letter-spacing: 2.5px; color: var(--color-accent);
  text-transform: uppercase; margin-bottom: 14px;
}
.info-block p { font-size: 0.92rem; color: var(--color-dark); line-height: 1.9; }
.info-block .note { font-size: 0.78rem; color: #aaa; margin-top: 6px; }

.contact-form h3 {
  font-family: var(--font-serif); font-size: 1.6rem; font-weight: 400;
  color: var(--color-dark); margin-bottom: 32px;
}
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.form-group { margin-bottom: 20px; }
.form-group.full { grid-column: 1 / -1; }
.form-group input, .form-group select, .form-group textarea {
  width: 100%; padding: 16px 18px;
  border: 1px solid var(--color-border); background: #fff;
  font-size: 0.9rem; color: var(--color-dark); font-family: inherit;
  outline: none; border-radius: 0;
  transition: border-color 0.25s ease;
}
.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
  border-color: var(--color-accent);
}
.form-group textarea { resize: vertical; min-height: 130px; }
.form-group select { appearance: none; background: #fff; cursor: pointer; }
.full-width { width: 100%; text-align: center; background: var(--color-dark); color: #fff; }
.full-width:hover { background: #333; }
.form-success {
  margin-top: 18px; padding: 16px; background: var(--color-cream);
  font-size: 0.85rem; color: var(--color-dark); text-align: center;
}
.form-error {
  margin-top: 18px; padding: 16px; background: #fff5f5; border: 1px solid #fecaca;
  font-size: 0.85rem; color: #b91c1c; text-align: center;
}
@media (max-width: 768px) {
  .contact-body { grid-template-columns: 1fr; padding: 48px 24px; gap: 48px; }
  .form-row { grid-template-columns: 1fr; }
}
</style>
