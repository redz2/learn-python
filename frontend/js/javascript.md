# js

## javascript 基础

1. 变量和值

```js
let js = "amazing" // 小驼峰
console.log(typeof js)

let year
console.log(type year) // undefined

// const: 尽量使用const，当你确认变量修改修改时，再用let
// let: 函数内部的变量，用let
// var: never use var

// 模板字符串
const stringTemplate = `javascript is ${js}`

// if-else
const age = 23
if (age > 20){
    console.log("you can driving car")
}

'18' == 18 // true，loose equal，never use this，may cause bug
'18' === 18 // false，always use strict equal

// 类型转换
let year = '1993'
console.log(Number(year)+30)
console.log(Number(js)) // NaN: Not a Number 类型还是Number，但是是一个无效的Number

// AND && 、OR || 、NOT !

// switch
const day = 1
switch(day){
    case 1:
        console.log("1")
        break  // 如果没有这个break，会继续执行之后的代码，并且不要匹配，我觉得是语言层面的bug
    case 2:
    case 3:
        console.log("2 or 3")
        break
    default:
        console.log("Not a valid day")

}

// 表达式: 产生一个值
// 语句: 干一件事情，不一定会产生一个值
```

2. 值的类型

   - 对象
     1. const obj = {}
     2. const obj = new Object({})
   - 基本数据类型
     1. String: used for text
     2. Boolean: true or false
        - false: NaN、0、''、undefined、null
     3. Number: all number
     4. undefined: 声明了变量未赋值
     5. null: empty value（和 golang 不同，变量没有初始值）
     6. Symbol: Value that is unique and can not be changed[not useful for now]
     7. bigint: Larger integers than the Number type can hold
   - 值具有类型，变量没有类型，变量只是存储具有类型的值

3. 函数
   - 一个变量可以保存一个值
   - 一个函数可以保存逻辑（语句或表达式）

```js
function add(a, b){
    return a + b
}

// 为什么要写函数？直接写表达式不好吗？代码可读性更好，复用，更容易修改
const sum = func(a, b){
    return a + b
}

// arrow funciton
sum = (a, b) => a + b
addOne = a => a + 1

function addNumbers(...nums){
    let sum = 0
    for(let i = 0; i < nums.length; i++){
        sum += nums[i]
    }
    return sum
}
```

4. array
   - js 的数组可以保存不同类型的值（一般都是保存同类型的元素）

```js
const arr1 = [1, 2, 3, 4, 5]
const arr2 = new Array(1, 2, 3, 4, 5)

arr1[1] = 10 # 修改数组元素
arr1.push(6) # 向数组末尾添加元素
arr1.pop() # 删除数组末尾元素
arr1.unshift(0) # 向数组开头添加元素
arr1.shift() # 删除数组开头元素
arr1.splice(2, 1, 'a') # 从索引2开始删除1个元素，并插入'a'
arr1.slice(2, 4) # 从索引2到索引4的元素
arr1.map(x => x*2) # 数组元素映射
arr1.filter(x => x > 3) # 数组元素过滤
arr1.reduce((acc, cur) => acc + cur, 0) # 数组元素求和
arr1.sort() # 数组元素排序
arr1.join('-') # 数组元素连接成字符串

// 遍历数组
for(let i = 0; i < arr1.length; i++){
    console.log(arr1[i])
}

// ES6 for-of loop
for(let item of arr1){
    console.log(item)
}

// 数组解构
const [a, b, c] = arr1
console.log(a, b, c)

oldArr = [1, 2, 3]
newArr = [...oldArr, 4, 5]
```

5. Object
   - js 的对象，看起来和 python 中的字典很像，实际上和 python 的对象一样
   - js 中有类似于 python 的 class 吗？用来创建一个对象

```js
// 增强对象字面量语法
const person = {
  firstName: "John",
  age: 30,
  // 方法和函数最大的区别在于，是否可以修改数据
  // 函数的不可变性: 指的是函数内部的变量不能被修改，只能读取(读取数据，函数处理后返回全新的数据)
  greet: function () {
    console.log(`Hello, my name is ${this.name}`); // this指的是当前对象
  },
};

// 访问对象属性: dot notation or bracket notation
console.log(person.firstName);
console.log(person["first" + "Name"]); // 属性名称需要拼接时不能使用点号

// 对象解构
const { firstName, age } = person;
console.log(firstName, age);

// optional chaining
const boy = {
  name: "John",
  age: 30,
  address: {
    street: "123 Main St",
    city: "Anytown",
    state: "CA",
    zip: "12345",
  },
};
console.log(boy.address?.street); // 访问对象属性，如果对象不存在，则返回 undefined

// object loop
Object.keys(person); // 返回一个数组，包含对象的所有键
Object.values(person); // 返回一个数组，包含对象的所有值
Object.entries(person); // 返回一个数组，数组的每一项是一个数组，包含键值对
```

6. loop
   - 代码: 基于条件做出选择，重复执行
   - 图形: 基于事件，执行代码（人的操作频率远低于计算机的执行速度）

```js
// for loop: continue/break
for (let i = 0; i < 5; i++) {
  console.log(i);
}

// while loop
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}

// do-while loop
let i = 0;
do {
  console.log(i);
  i++;
} while (i < 5);
```

7. sets and maps

   - 集合: 无序的，不重复的值的集合
   - 映射: 键值对的集合，键必须唯一，值可以重复

```js
const set1 = new Set([1, 2, 3, 4, 5]); // 和数组很像，但是元素不能重复
// what is difference between Map and Object?
// Map: key-value pairs, can have any type of value, keys can be any type of value
// Object: key-value pairs, values can only be primitive types, keys must be strings or symbols
const map1 = new Map([
  ["name", "John"],
  ["age", 30],
  ["city", "Anytown"],
]);
```

## how to think like a developer

- 不要着急

- 如何解决问题？

  1. 确保你 100%理解问题: we need a function that reverses whatever we pass into it.
  2. 分解成小问题: 分解问题的同时，也会帮助你更好地理解问题
  3. 先尝试自己解决，实在不行先 google，stackoverflow，mdn，使用别人的方案
  4. 先写一些伪代码

- 数据从哪里来？

  1. from the program itself
  2. from the UI: data input from the user
  3. from external sources(APIs, databases, etc.)

- 数据更适合哪种数据结构？

  1. simple list or key/value pairs?
  2. other data structures? 如何选择合适的数据结构来处理问题？
