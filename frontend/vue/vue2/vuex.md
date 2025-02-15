# Vuex: 集中式状态管理

1. 如何配置 vuex？
   - state: 数据(无法直接修改，只能通过 mutation 修改)
   - mutations: 修改数据的函数
   - actions: 异步修改数据的函数
   - getters: 计算属性
   - modules: 子模块

```js
// store.js
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    count: 0,
    firstName: "John",
    lastName: "Doe",
  },
  // 类似于vue中的methods，方法名称一般定义为大写，使用箭头函数
  mutations: {
    INCREMENT: (state) => state.count++,
  },
  // actions的第一个参数是context，包含了state和commit方法，可以解构出state和commit方法
  actions: {
    do_increment: ({ commit }) => {
      // 触发一个 mutation
      commit("INCREMENT");
    },
  },
  // getters相当于vue中的computed
  getters: {
    fullName(state) {
      return state.firstName + " " + state.lastName;
    },
    // 当然，也可以直接使用子模块中的数据和方法
    // fullName: (state) => state.user.firstName + " " + state.user.lastName,
  },
  modules: {}, // 子模块
});

export default store;
```

2. 如何使用 vuex？
   - 如何获取 vuex 中的 state？只有 mutations 才能修改 state
     - `this.$store.state.count`
   - 如何触发 mutations？
     - `this.$store.commit("INCREMENT")`
   - 如何触发 actions？
     - `this.$store.dispatch("do_increment")`
   - 如何使用 getters？
     - `this.$store.getters.fullName`
   - 如何将 vuex 中的 state，mutations，actions，getters 映射到组件中（帮助我们定义 computed，methods）
     - mapState
     - mapMutations
     - mapGetters
     - 因为 vue 组件中只能使用自己定义的 computed, methods, 才能使用。当然可以自己实现，但是语法糖可以直接将 vuex 中的数据，方法映射到组件中。

```js
// main.js
import Vue from "vue";
import App from "./App.vue";
import store from "./store";

new Vue({
  el: "#app",
  store,
  render: (h) => h(App),
});
```

```html
<!-- App.vue -->
<template>
  <div>
    <h1>{{ count }}</h1>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
  import { mapState, mapMutations } from "vuex";

  export default {
    name: "App",
    data() {
      return {
        hello: "hello",
        count2: 2,
      };
    },
    // computed不能传参
    computed: {
      // mapState是什么？它可以将 store 中的 state 映射到组件的 computed 属性中
      // 使用mapState获取vuex中的state的数据
      // 1. 数组形式
      // ...mapState(["count"]),  // count() { return this.$store.state.count;},
      // 2. 对象形式
      ...mapState({
        count,
        count1: count1,
        repeatCount: count2, // count2在data中定义过了，所以要换个名字repeatCount
        count3: (state) => state.count3, // state 等价于 this.$store.state
        helloName: function (state) {
          return this.hello + " " + state.name;
        },
      }),
      ...mapGetters(["fullName"]),
    },
    methods: {
      // mapMutations是什么？它可以将 store 中的 mutations 映射到组件的 methods 方法中
      // 如何调用 mutations？
      // increment() {
      //   this.$store.commit("increment");
      // },
      ...mapMutations(["increment"]),
      // 如何调用 actions？
      // this.$store.dispatch("do_increment");
    },
  };
</script>
```

3. vuex 子模块

   - 如何配置子模块？
     - `modules: {user: { namespaced: true, state: {...}, mutations: {...}, actions: {...}, getters: {...}}}`
   - 如何使用子模块？
     - `this.$store.state.user.count`
     - `this.$store.commit("user/INCREMENT")`
     - `this.$store.dispatch("user/do_increment")`
     - `this.$store.getters["user/fullName"]`
   - 如何使用 mapState，mapMutations，mapGetters？
     - `...mapState("user", {count})`
     - `...mapMutations("user", ["increment"])`
     - `...mapGetters("user", ["fullName"])`

```js
// store.js
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    user: {
      namespaced: true,
      state: {
        count: 0,
        firstName: "John",
        lastName: "Doe",
      },
      mutations: {
        INCREMENT: (state) => state.count++,
      },
      actions: {
        do_increment: ({ commit }) => {
          commit("INCREMENT");
        },
      },
      getters: {
        fullName(state) {
          return state.firstName + " " + state.lastName;
        },
      },
    },
    product: {
      namespaced: true,
      state: {
        count: 0,
        firstName: "John",
        lastName: "Doe",
      },
      mutations: {
        INCREMENT: (state) => state.count++,
      },
      actions: {
        do_increment: ({ commit }) => {
          commit("INCREMENT");
        },
      },
      getters: {
        fullName(state) {
          return state.firstName + " " + state.lastName;
        },
      },
    },
  },
});

export default store;
```

```html
<!-- App.vue -->
<template>
  <div>
    <h1>{{ count }}</h1>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
  import { mapState, mapMutations } from "vuex";

  export default {
    name: "App",
    data() {
      return {
        hello: "hello",
        count2: 2,
      };
    },
    // mapState的第二个参数是命名空间，可以将 store 中的 state 映射到组件的 computed 属性中
    computed: {
      ...mapState("user", {
        count,
        count1: count1,
        repeatCount: count2, // count2在data中定义过了，所以要换个名字repeatCount
        count3: (state) => state.count3,
        helloName: function (state) {
          return this.hello + " " + state.name;
        },
      }),
      ...mapGetters("user", ["fullName"]),
    },
    methods: {
      ...mapMutations("user", ["increment"]),
    },
  };
</script>
```
