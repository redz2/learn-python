# dom

- 如何操作 DOM 元素？如何更新页面显示？

```js
// 通过操作DOM元素来修改元素内容
document.querySelector(".message").textContent = "Hello, World!";

function updateMessage(message) {
  const messageElement = document.querySelector(".message");
  messageElement.textContent = message;
}

updateMessage("Goodbye, World!");
```

```vue
<script setup>
import { ref } from "vue";
// 让开发人员不需要关注如何更新页面？也不需要获取DOM元素，只需要关注数据和逻辑
const message = ref("Hello, World!");
// 此函数不遵循函数不可变性
function updateMessage(message) {
  message.value = message; // 直接使用全局数据
}
</script>
```

- 猜数字游戏: 如何处理点击事件？

```js
const button = document.querySelector("button");
let secretNumber = Math.trunc(Math.random() * 20) + 1;
let score = 20;
let highScore = 0;

// 重置游戏
document.querySelector(".again").addEventListener("click", () => {
  secretNumber = Math.trunc(Math.random() * 20) + 1;
  score = 20;
  document.querySelector(".message").textContent = "Start guessing...";
  document.querySelector(".number").textContent = "?";
  document.querySelector(".score").textContent = score;
  document.querySelector(".highscore").textContent = highScore;
  document.querySelector("body").style.backgroundColor = "white";
});

// 注册事件
// 一个页面可以看作是一个对象，而页面是有状态的
button.addEventListener("click", () => {
  // 获取输入框的值
  const input = document.querySelector("input");
  let guess = input.value;
  guess = Number(guess);
  // js中，我们可以认为定义的变量，函数都是页面对象的属性，方法
  // 函数可以修改数据，数据变化后，还需要更新页面显示
  // vue通过setter函数捕获数据变化，自动更新页面显示（变量和页面如何保持一致性？）
  if (!guess) {
    document.querySelector(".message").textContent = "🤪 not a number";
  } else {
    if (guess === secretNumber) {
      document.querySelector(".number").textConent = secretNumber;
      displayMessage("👏 correct");
      if (score > highScore) {
        highScore = score;
        document.querySelector(".highscore").textContent = highScore;
      }
      // 如何修改CSS样式？
      document.querySelector("body").style.backgroundColor = "green";
    } else if (score > 1) {
      displayMessage(guess > secretNumber ? "👆🏼 too high" : "👎🏻 too low");
      score--;
    } else {
      document.querySelector(".message").textContent = "😭 out of tries";
    }
  }
});

// 简化代码
function displayMessage(message) {
  document.querySelector(".message").textContent = message;
}
```
