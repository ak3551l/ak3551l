function addOne(num) {
    throw new Error('Oh no, an Error!')
}

function getNum() {
    return addOne(10)
}

function c() {
    console.log(getNum() + getNum())
}

c()
