# 模块化

1. 什么是模块化？

   - 将程序文件依据一定的规则拆分成多个文件
   - 拆分出来的每个文件就是一个模块，模块中的数据是私有的，模块之间隔离
   - 能通过一些手段，将数据交出去

   - 一些思考:
     - 有状态
       - 主程序
       - 对象
         - 为什么在 js 中写函数都是有状态的，本质上就是在扩充 html 对象的方法
     - 无状态: 可复用
       - 模块
       ```javascript
       // module.js
       class Num {
         constructor(num) {
           this.num = num;
         }
         function add(num) {
           return this.num + num;
         }
       }
       export default Num;
       ```
       - 函数
       - 类: 当使用元类时，其实就在更高层次添加了状态信息
         - 尽量减少副作用？
         - 如何看待有状态这件事情？
           - 如果考虑一个小功能，就是干一件事情，不需要状态
           - 如果考虑一个对象，有状态更好描述

2. 为什么需要模块化？
   - 全局污染问题: 全局变量容易造成冲突
   - 依赖混乱问题: 不同模块之间有依赖关系
   - 数据安全问题: 数据暴露在全局

```html
<script src="a.js"></script>
<script src="b.js"></script>
<script src="c.js"></script>
```

3. 模块化规范: 一开始 js 并没有模块化的技术

   - CommonJS: 服务端应用广泛
     - browserify: 打包工具，将多个模块打包成一个文件

   ```javascript
   // a.js
   let a = 1;
   let b = 2;
   let c = 3;

   // 模块内部的空对象: this, exports, module.exports
   // 最终导出的是 module.exports 对象

   // exports.a = a;
   // exports.b = b;
   module.exports = { a, b };

   console.log(arguments.callee.ToString()); // 证明模块在一个函数体中，也说明了exports是哪里来的？
   // function (exports, require, module, __filename, __dirname){...}
   ```

   ```javascript
   // index.js
   const { a, b } = require("./a.js"); // 浏览器不认识 require
   ```

   - AMD: 不用了
   - CMD: 不用了
   - ES6 模块化: 浏览器应用广泛
     - 如何在 node 中运行 ES6 模块化？package.json 中添加 `{"type": "module"}`

   ```javascript
   // a.js
   // export const a = 1;
   // export const b = 2;

   // export { a, b };  // 这不是对象，只是和对象写法差不多

   // 如果数据要导出，必须只读
   // ES6中导出的数据和导入的数据，共用一块内存空间
   export default { a, b }; // 默认导出，这里是对象
   ```

   ```javascript
   // index.js
   // import * as moduleName from "./a.js"; // 全部导入

   // 导入的变量都是只读的，不能修改
   // 分别导出和统一导出时，如何导入？
   // import { a, b } from "./a.js"; // 统一导出

   // 默认导出时，可以使用任意名称导入
   import WhateverName from "./a.js"; // 默认导入和命名导入可以混用
   console.log(WhateverName);

   // 动态导入: 返回一个 promise 对象，需要等待模块加载完成
   btn.onclick = async () => {
     const module = await import("./a.js");
     console.log(module.a);
   };

   // import 可以不接收任何数据，只是用来导入模块，会执行模块中的代码
   ```

   ```html
   <!-- index.html -->
   <!-- 正常js和模块化js的区别 -->
   <!-- <script type="text/javascript" src="index.js"></script> -->
   <script type="module" src="index.js"></script>
   ```

4. 导入和导出

   - 模块之间是隔离的，通过导入和导出来进行数据和功能的共享
