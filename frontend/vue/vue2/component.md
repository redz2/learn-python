# 自己封装一个 Vue 组件

```vue
<template>
  <span ref="countup"></span>
</template>

<script>
import CountUp from "countup.js";

export default {
  name: "CountUp",
  data() {
    return {
      count: 0,
    };
  },
  mounted() {
    this.initCountUp();
  },
  methods: {
    initCountUp() {
      this.count = new CountUp(this.$refs.countup, 0, 2000);
      this.count.start();
    },
  },
};
</script>
```
