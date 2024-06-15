const sayHello = (function  makeHelloFunction() {
    var message = "Hello!"

    function sayHello() {
        console.log(message)
    }
    return sayHello
}) ()

const counter = (function() {
    let count = 0

    return {
        inc: function() {count = count + 1},
        get: function() {console.log(count) },
    }
}) ()

counter.inc()
counter.get()
counter.inc()




