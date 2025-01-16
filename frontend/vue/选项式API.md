# 选项式API
* vue2
```vue
<template>
    <div class="person">
        <h2>命名: {{name}}</h2>
        <h2>年龄: {{age}}</h2>
        <button @click="changeName">修改姓名</button>
        <button @click="changeAge">修改年龄</button>
        <button @click="showTel">查看联系方式</button>
    </div>
</template>

<script lang="ts">
export default {
    name: 'Person',
    data(){
        return {
            name: '张三',
            age: 18,
            tel: '13888888888'
        }
    },
    methods: {
            changeName(){
                this.name = 'zhangsan'
            },
            changeAge(){
                this.age += 1
            },
            showTel(){
                alert(this.tel)
            }
    },
    watch:{

    },
    computed: {

    }
}
</script>
```

* vue3
```vue
<template>
    <div class="person">
        <h2>命名: {{name}}</h2>
        <h2>年龄: {{age}}</h2>
        <button @click="changeName">修改姓名</button>
        <button @click="changeAge">修改年龄</button>
        <button @click="showTel">查看联系方式</button>
    </div>
</template>

<script lang="ts">
import {ref} from 'vue'

export default {
    name: 'Person3',
    // setup()和data()，method可以一起写吗？可以一起写，但不建议这么做！！！
    data(){
        // Vue2中data可以读取到setup中定义的变量
        // Vue3中setup中不能读取data中的数据
        return {
            count: 1,
            a: this.name
        }
    },
    methods: {
        plus(){
            this.count++
        }
    },
    setup(){
        // setup()中的this是undefined，在Vue3中已经弱化this
        // setup()执行要比beforeCreate更早

        // 数据
        // Vue2中是写在data中，就是响应式的

        // 如果不用ref或者reactive包裹，数据不是响应式的
        let name = ref("张三") // 响应式数据
        let age = "18" // 不是响应式数据
        let tel = "1388888888" // 不是响应式数据

        // 方法
        function changeName(){
            name.value = 'zhangsan'
        }
        function changeAge(){
            // 注意：这样修改age，页面是没有变化的，因为age不是响应式的
            age += 1 
            // 不过age确实已经修改了
            console.log(age) 
        }
        function showTel(){
            alert(tel)
        }

        // 此处必须返回变量和函数，在模板中才能使用
        return {
            name,
            age,
            changeName,
            changeAge,
            showTel,
        }
        
        // setup()返回值可以是一个函数，可以直接渲染页面内容（和django中的render函数差不多）
        // return ()=> "<div>我是页面内容</div>"
    }
}
</script>
```