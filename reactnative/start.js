const o = new Object()
o.firstname = "Jordan"
o.lastname = "Hayashi"
o.isTeaching = true
o.greet = function() {
    console.log('hi!')
}

const o2 = {}
o.firstname = "Jordan"
o['lastname'] = 'Hayashi'
const key = "isTeaching"
o[key] = true
o['greet'] = function() {
    console.log('hi!')
}


const o3 = {
    1: 'Test',
    firstname: 'Jordan',
    lastname: 'Hayashi',
    isTeaching: true,
    function() {
        console.log('hi!')
    },
    address: {
        street: 'Main St. ',
        number: 123,
    },
}

