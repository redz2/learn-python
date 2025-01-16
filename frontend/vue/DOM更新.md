* DOM更新
```js
// DOM更新时机: DOM更新不是同步的，而是在“next tick”更新周期中缓冲所有状态的修改，确保组件只更新一次（当数据变化时，会开启一个异步队列，将数据变化导致的DOM更新合并到一个更新任务中，避免频繁更新DOM，提高性能）
// 主要是因为异步的关系，比如说我设置了一个div的高度为100px，此时DOM并未更新，如果我在函数中需要获取div的高度，不一定能获取的
import { nextTick } from 'vue'

async function increment() {
  count.value++
  await nextTick()  // 等 DOM 更新
  // 现在 DOM 已经更新了
}
```