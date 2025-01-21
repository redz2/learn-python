# what is promise？
***
0. 关键点：异步函数无法返回值（何为异步？）

1. 回调函数
```
setTimeout(()=>{
    // 1. 先获取歌单
    console.log('获取歌单') 
    setTimeout(()=>{
        // 2. 获取歌单列表
        console.log('获取歌单列表');
        setTimeout(() => {
            // 3. 获取歌曲
            console.log('获取歌曲')
        }, 1000);
    }, 1000)
},1000)
```

2. Promise(把异步操作包装成Promise对象)
```
func addNewStudent(name){
    return new Promise((resolv, reject) => {
        setTimeout(()=>{
            console.log(name)
        }, 1000)
    })
}

addNewStudent("aaa")
.then(()=> addNewStudent("bbb"))
.then(()=> addNewStudent("ccc"))
.then(()=> console.log("end"))
```

3. async/await
* 当异步操作之间是相关的，问题就是如何让这几个异步操作执行时是同步进行的
* 如果是不相关的操作，直接setTimeout()，想啥时候执行就啥时候执行
```
async func addTwoStudents(){
    let res1 = await addNewStudent("aaa")
    let res2 = await addNewStudent("bbb")
}

addTwoStudents()
```

4. axios（强大的第三方库，基于Promise对原生XMLHttpRequest的封装和加强）
```
axios.get('https://www.baidu.com', {
    params: {
        id: 1
    }
}).then(res => {
    console.log("ok")
})
.catch(err => {
    console.log("error")
})
```

```
axios({
    method: 'get',
    url: 'https://www.baidu.com',
    params: {
        id: 1,
    },
}).then(res => {
    console.log("ok")
}).catch(err => {
    console.log("error")
})
```

5. fetch(和axios差不多，现代浏览器内置API)
