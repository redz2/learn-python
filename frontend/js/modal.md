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
  if (event.keyCode === 27) {
    modal.classList.add("hidden"); // 隐藏模态框
    overlay.classList.add("hidden"); // 隐藏遮罩层
  }
});
```
