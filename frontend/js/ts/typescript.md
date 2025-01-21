# typescript
1. 基础知识
    * ts
    ```typescript
    // 基本数据类型
    let num: number = 10
    let str: string = "hello world"
    let bool: boolean = true
    let nullVal: null = null
    let undefinedVal: undefined = undefined

    let obj: {name: string, age: number} = {name: "John", age: 30}
    let date: Date = new Date()
    // Array类型
    let arr: number[] = [1, 2, 3]
    let arr2: Array<number> = [1, 2, 3]
    let tuple: [string, number] = ["hello", 10]
    let anyVal: any = "hello world"
    let log_hello: Function = function() {
        console.log("hello world")
    }
    ```
2. 接口
    * ts
    ```typescript
    interface Person {
        name: string
        age: number
        greet(): void
    }
    