function doSomething(callback) {
    setTimeout(function {callback(1)}, 1000)
}

doSomething(console.log)
