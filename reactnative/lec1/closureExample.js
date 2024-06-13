function  makeHelloFunction() {
    const message = "Hello!"

    function sayHello() {
        console.log(message)
    }
    return sayHello
}

const functionArr = makeHelloFunction()

console.log(i)

functionArr()
