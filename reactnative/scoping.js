thisIsNotHoisted()

const thisIsAConst = 50
// thisIsAConst++ // error!

const constObj = {}
constObj.a = 'a'

let thisIsALet = 51
thisIsALet = 50

// let thisIsALet = 51 // errors!

var thisIsAVar = 50
thisIsAVar = 51
var thisIsAVar = 'new value!'

//function can be changed
function thisIsHoisted() {
    console.log("This is the function hoisted at the bottom of a file");
}

// const can't be changed
const thisIsNotHoisted = function() {
    console.log("Should not be Hoisted?")
}
