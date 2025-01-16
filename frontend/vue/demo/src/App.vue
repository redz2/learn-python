<script setup>
const msg = "hello, world"
const rawHtml = '<span style="color: red">This should be red.</span>'
</script>

<template>
  <!-- 1. 文本插值 -->
  <span>Message: {{ msg }}</span>
  <br>

  <!-- 2. 原始HTML -->
  <div>Using text interpolation: {{ rawHtml }}</div>
  <div>Using v-html directive: <span v-html="rawHtml"></span></div>
</template>

<style scoped>

</style>
