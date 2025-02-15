# oop

1. 如何创建一个对象？

```javascript
let person = {
  name: "John",
  age: 30,
  greet: function () {
    console.log("Hello, my name is " + this.name);
  },
};

{} === new Object(); // 完全等价
```

2. 如何创建一个类？

   - 抽象
   - 封装
   - 继承
   - 多态

```javascript
// ES6语法class只是原型链的语法糖

// attention:
// 1. class is not hoisted, so it should be defined before use
// 2. class is first-class citizen
// 3. class is executed in strict mode by default
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  greet() {
    console.log("Hello, my name is " + this.name);
  }
}

const john = new Person("John", 30);
```

3. prototype: 原型
   - 对象如何和构造函数的原型对象关联？
     `john.__proto__ === person.prototype === {greet: f}`

```javascript
// 每一个构造函数都有一个prototype属性，prototype属性是一个对象，包含所有属性和方法，通过构造函数创建的对象的实例都共享这些方法和属性
const person = function (name, age) {
  this.name = name;
  this.age = age;
};

// 原型链是啥？
// 1. 所有对象都有__proto__属性，默认值为Object.prototype
// 2. 对象的__proto__属性指向构造函数的prototype属性（原型对象）
// 3. 构造函数的prototype属性指向一个对象，这个对象包含所有实例共享的属性和方法，{greet: f}
// 4. 原型链的末端指向null

// 所有函数都有prototype属性，默认值为{}，包括构造函数
// person.prototype.constructor = person;
person.prototype.greet = function () {
  console.log("Hello, my name is " + this.name);
};

const john = new person("John", 30);
const matina = new person("Matina", 25);
// when use new, what happens?
// 1. an empty object is created
// 2. this keyword in constructor function call is set to the new object
// 3. the new object is linked to the the constructor function's prototype
// 4. the new object is automatically returned from the constructor function

// 如何查看一个object的原型链？
console.log(john.__proto__); // {greet: f}
console.log(person.prototype); // {greet: f}
// 如何判断一个object是否是某个构造函数的实例？
console.log(john instanceof person); // true
// 通过isPrototypeOf()方法查看原型链
console.log(person.prototype.isPrototypeOf(john)); // true
console.log(person.prototype.isPrototypeOf(person)); // false

const arr = [1, 2, 3]; // new Array([1, 2, 3])
console.log(arr.__proto__);
console.log(arr.__proto__ === Array.prototype);

// 添加一个unique方法到Array.prototype
Array.prototype.unique = function () {
  return [...new Set(this)];
};
```
