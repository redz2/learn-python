# vue2 基础

1. why vue2?

   - 很多项目和组件都是基于 vue2 的，比如 vue-element-admin

2. why vue?

   - vue.js 的核心是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统。

```vue
<template>
  <div>
    {{ message }}
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      message: "Hello Vue.js!",
    };
  },
};
</script>
```

3. this in vue2
   - 在 vue 中，this 指的是当前 Vue 实例的引用
   - 访问 data、methods、computed、props
   - this.$refs
   - this.$store
   - this.$emit
