# js
1. 变量和值
```js
let js = "amazing" // 小驼峰
console.log(typeof js)

let year
console.log(type year) // undefined

// const: 尽量使用const，当你确认变量修改修改时，再用let
// let
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
    * 对象
        1. const obj = {}
        2. const obj = new Object({})
    * 基本数据类型
        1. String: used for text
        2. Boolean: true or false
            * false: NaN、0、''、undefined、null
        3. Number: all number
        4. undefined: 声明了变量未赋值
        5. null: empty value（和golang不同，变量没有初始值）
        6. Symbol: Value that is unique and can not be changed[not useful for now]
        7. bigint: Larger integers than the Number type can hold
    * 值具有类型，变量没有类型，变量只是存储具有类型的值
3. 函数
    * 一个变量可以保存一个值
    * 一个函数可以保存逻辑（语句或表达式）
```js
function add(a, b){
    return a + b
}

const sum = func(a, b){
    return a + b
}

// arrow funciton
sun = (a, b) => a + b 
```

