// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
// import router from './router'

// 创建一个app: 传入一个组件
const app = createApp(App)
// 使用路由器
// app.use(router)
// 将app挂载到页面中
app.mount('#app')
