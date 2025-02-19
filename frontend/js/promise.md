# 异步编程

0. 回调函数

```javascript
setTimeout(() => {
  console.log("first");
  setTimeout(() => {
    // 可以使用first获取的数据进行处理
    console.log("second");
    setTimeout(() => {
      console.log("third");
    }, 1000);
  }, 1000);
}, 1000);
```

1.  promise 是一个对象，用来包裹一个异步操作（需要想办法获取异步函数的结果）

    - 异步操作可以是 setTimeout, setInterval, XMLHttpRequest, fetch 等.
    - promise 中的异步操作何时执行？定义 promise 对象时，立即执行！！！
    - promise.then 方法何时执行？调用 resolve 方法时，修改 promise 状态为 fulfilled，执行 then 方法
    - promise.catch 方法何时执行？调用 reject 方法时，修改 promise 状态为 rejected，执行 catch 方法
    - 定义 promise 对象时，一定要 resolve 吗？
      - 不一定，如果异步操作完成后，不需要执行任何操作

    ```javascript
    // 如何创建 promise 对象？
    const promise = new Promise((resolve, reject) => {
      // 异步操作
      setTimeout(() => {
        // 异步操作成功, 必须告诉 promise 对象.
        resolve("success");
      }, 2000);
    });

    // promise 对象会执行异步操作，等待异步操作完成，并调用 then 方法.
    promise
      .then((result) => {
        console.log(result);
      })
      .catch((error) => {
        console.error(error);
      });

    // then 方法会返回一个新的 promise 对象，可以实现链式调用
    // 1. 将异步操作包裹成一个promise对象，并立即执行异步操作
    // 2. 调用then方法，生成一个promise，等待第一步中的promise完成 -> 异步操作调用resolve方法 -> 执行处理函数 -> return
    // 3. 调用第二个then方法，生成一个promise，等待第二步中的promise完成 -> 返回说明第二步的promise已经完成 -> 执行处理函数 -> return
    // promise
    //  .then((result) => { handle(result) }, (error) => { handle(error) })
    //  .then((result) => { handle(result) }, (error) => { handle(error) })

    // 使用 promise 来包裹其他异步操作
    const promise_fetch = new Promise((resolve, reject) => {
      // 何时执行then？fetch 完成后
      fetch("https://jsonplaceholder.typicode.com/todos/1")
        .then((response) => {
          // fetch complete, do something, resolve promise fetch
          resolve();
        })
        .catch((error) => {
          reject(error);
        });
    });

    // 当 promise_fetch 完成后, 调用 then 方法.
    promise_fetch.then(() => {
      // promise_fetch 完成后
      console.log("fetch success");
    });
    ```

2.  async/await: 异步编程的语法糖，可以让异步操作更加方便，更加像同步操作.

```javascript
// async 函数返回的是一个 promise 对象.
// async 函数可以用 await 关键字来等待 promise 对象.
// try...catch 块用来处理 promise 对象中的异常.
// 如果 promise 对象状态为 fulfilled, await 后面的语句会执行.
// 如果 promise 对象状态为 rejected, await 后面的语句不会执行, 而是直接抛出异常.
async function fetchData() {
  try {
    // 根据 promise 对象的状态，判断是否继续执行，还是抛出异常.
    // 如果 promise 状态一直是pending，则一直等待.
    const susccess = await new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve("success");
      }, 2000);
    });
    console.log(susccess);
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/todos/1"
    );
    // 之前如果 promise 的状态变成 fullFilled, 会执行 then 方法，对于数据的处理，比较麻烦
    // 如果处理完数据，需要继续执行其他异步操作，返回一个新的 promise 对象，就是链式处理
    // 也可以同时处理多个 promise 对象, Promise.all([promise1, promise2]).then(results => {console.log(results)})

    // 现在直接将result赋值给data，可以直接处理数据
    // 通过 await 关键字，可以像同步操作一样，顺序执行异步操作
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// fetchData 函数将多个异步操作，包裹成一个 promise 对象.
fetchData(); // 返回 promise 对象，开始执行函数
```

3. axios: 基于 promise 的 HTTP 客户端，可以更方便地处理 HTTP 请求.

4. fetch(和 axios 差不多，现代浏览器内置 API)
