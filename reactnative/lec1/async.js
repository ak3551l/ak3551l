function printOne() {
    console.log('one')
}

function printTwo() {
    console.log('Two')
}

function printThree() {
    console.log('Three')
}

setTimeout(printOne, 1000)
setTimeout(printTwo, 0)
printThree()


