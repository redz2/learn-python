// 为啥不能导入模块？这不是一个项目文件，vue其实帮我们设置了环境变量
// 如何自己创建一个模块呢？
console.log("hello world")

function hello(name){
    console.log(name)
}

hello("shaw")

// 输出文档内容
// document.write("我是div标签")
// document.write("<h1>我是一级标题</h1>")
// alert("页面弹出警告弹窗")
// console.log('控制台输出')
// prompt("请输入你的年龄")

/* 浏览器对象模型
1. window是JS中的顶级对象
2. document、alert()、console.log()都是window的属性(写的时候可以省略window)
3. 所有通过var定义的全局变量、函数都会变成window的属性和方法
*/

/* 定时器
const IntervalID = window.setInterval(()=>{
    console.log('每5秒执行一次');
},5000)
clearInterval(id)
*/

/* 数据类型
1. Number
123 //整数
1.23 //浮点数
1.2345e3 //科学计数法
-99 //负数
NaN //Not a Number，当无法计算结果时使用
Infinity //无限大

2. 字符串
let name = 'zy' // js推荐单引号，"abc"也可以
console.log(`hello, {$name}`) //模板字符串
name[0]='s' //字符串不可变， 不会报错，也不会有任何效果
name.length
name.toUpperCase()
name.toLowerCase()

3. 布尔值
true
false

4. 比较运算符
2>1; //true
NaN==NaN; //false
isNaN(NaN); //true

5. null和undefined(声明变量未赋值时)
区分并没什么卵用


6. 数组
arr = [1,2,3,'hello',true]; //用这个，一般不用new Array(1,2,3)
arr[10]='world'; // 别的编程语言越界访问会报错
arr.push(5,6); // push尾部插入
arr.pop(); // pop尾部删除
arr.unshift(1,2); // unshift头部插入
arr.shift() // shift头部删除，就算是空数组也不会报错，返回undefined


7. 对象
var Person = {
    name: 'zy',
    age: 20
} //对象的键都是字符串类型

8. 变量
感觉和python类似，是一种标签，而非盒子

变量命名规则：只能是英文字母、数字、$、_
小驼峰：userName

let a=1 //变量的声明与赋值
let a //变量的声明
a=1 //变量的赋值

var or let

var不合理处
可以先使用，再声明
var声明变量可以重复声明
比如变量提升、全局变量、没有块级作用域

9. 常量
vue中为什么推荐使用const呢？ref是一个响应式引用对象
const name = "zy"

10. 检测数据类型
运算符写法(推荐)：typeof obj
函数写法：typeof(obj)

11. 类型转换
// 隐式转换：+ 两边只要有一个是字符串，会把另外一个也变成字符串
let strNum = '123'
console.log(+strNum) // 转换为数字型
// 显式转换：
console.log(Number(strNum))

12. 运算符
    赋值运算符：num += 3

    一元运算符：正号 +1   
    自增 console.log(i++ + i++ + 1)

    比较运算符(返回true或false)：
    console.log(NaN == NaN)
    console.log(2 == '2')  存在隐式转换
    console.log(2 === '2') 全等，要求值和类型都一致（推荐使用===）

    逻辑运算符
    && || !

    运算符优先级
    1. 小括号
    2. 一元运算符（++，--，!）
    3. 算术运算符（先 * / 后 +-）
    4. 关系运算符
    5. 相等运算符（5 > 3 == 2 > 1）
    6. 逻辑运算符（ 先&& 后||）
    7. 赋值运算符（ = ）
    8. 逗号运算符（ , ）

13. 语句
语句是一段可以执行的代码，不一定有值
表达式是可以被求值

分支语句
if 分支语句 ***
if( 条件 ){
    满足条件执行的代码
}
else if ( 条件2 ){
    满足条件执行的代码
}

三元运算符
条件 ? 代码1 : 代码2
数字补0: num < 10 ? '0' + num : num

switch 分支语句（分支超过5时，效率比if高）
判断是全等
switch(val){
    case 1:
        执行代码
    case 2:
        执行代码
    default:
        执行默认代码
}

循环语句
while循环（不确定次数时使用）
while ( 条件 ){
    执行代码，必须有终止条件
    满足一定条件退出循环：break continue
}

for循环 ***（确定次数时使用）
for(let i = 1; i < 0; i++){
    执行代码
}
for(;;){ 死循环 }
*/



