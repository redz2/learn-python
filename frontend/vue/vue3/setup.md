# setup

1. setup() 钩子是在组件中使用组合式 API 的入口

```vue
<script>
import { ref } from "vue";

export default {
  setup() {
    const count = ref(0);

    // 返回值会暴露给模板和其他的选项式 API 钩子
    return {
      count,
    };
  },
  mounted() {
    console.log(this.count); // 0
  },
};
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>
```

2. setup 语法糖: 推荐使用

```vue
<script setup>
import { ref } from "vue";

const count = ref(0);

// 声明周期钩子
onMounted(() => {
  console.log(this.count); // 0
});
</script>

<template>
  <button @click="count++">{{ count }}</button>
</template>
```
