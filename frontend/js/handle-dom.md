# dom

- 原生 js 如何操作 DOM 元素？

```js
// 原生js
// document.querySelector(".message").textContent = "Hello, World!";
// 通过操作DOM元素来修改元素内容
function updateMessage(message) {
  const messageElement = document.querySelector(".message");
  messageElement.textContent = message;
}
updateMessage("Goodbye, World!");
```

- jQuery 如何操作 DOM 元素？

```js
// jQuery
// $("#message").text("Hello, World!");

// 1. click事件
$("#btn1").click(function () {
  console.log("clicked");
});

// 2. on事件: 可以同时绑定多个事件
$("#btn2").on("click mouseenter", function () {
  console.log("clicked");
});

// 3. 事件委托: 父元素(ul)绑定事件，子元素(li)触发事件，事件冒泡到父元素
$("ul").on("click", "li", function () {
  console.log($(this).text());
});

// 4. 移除事件
$("#btn1").off("click"); // 移除所有click事件
$("#btn1").off(); // 移除所有事件

// 5. 常用事件
// 鼠标事件：click、dblclick、mousedown、mouseup、mousemove、mouseover、mouseout
// 键盘事件：keydown、keyup、keypress
// 表单事件：focus、blur、change、submit、reset
// 动画事件：animationstart、animationend、animationiteration
// 变换事件：transitionend
// 其他事件：load、unload、error、resize、scroll
```

- 如何使用 vue 更新页面显示？
  - vue 如何操作 DOM 元素？通过模板引用，使用 ref 属性

```vue
<script setup>
import { ref } from "vue";
// 让开发人员不需要关注如何更新页面？也不需要获取DOM元素，只需要关注数据和逻辑
const message = ref("Hello, World!");
// 这个函数不是纯函数（有状态）
// js 中，把页面当成一个对象，变量都是对象的属性，函数都是对象的方法
function updateMessage(message) {
  message.value = message; // 直接使用全局数据
}
updateMessage("Goodbye, World!");
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

- modal: 模态框的显示和隐藏

```js
// 通过类来修改网站样式
const btnCloseModal = document.querySelector(".btn-close-modal");
for (let i = 0; i < btnCloseModal.length; i++) {
  btnCloseModal[i].addEventListener("click", function () {
    modal.classList.remove("hidden"); // 显示模态框
    overlay.classList.remove("hidden"); // 显示遮罩层
  });
}

// 如何监听键盘事件
document.addEventListener("keydown", function (event) {
  // 按下ESC键
  if (event.keyCode === 27 && !modal.classList.contains("hidden")) {
    modal.classList.add("hidden"); // 隐藏模态框
    overlay.classList.add("hidden"); // 隐藏遮罩层
  }
});
```
