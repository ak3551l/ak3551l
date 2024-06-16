const person = {
    name: 'Jordan',
    greet: function() {console.log('hello, ' + this.name) },
}

person.greet()

const friend = {
    name: 'David',
}

friend.greet = person.greet

friend.greet()

const greet = person.greet.bind({name: 'This is a bound object. '})
person.greet.call({name: 'This is a bound object. '})
person.greet.apply({name: 'This is a bound object. '})


const newPerson = {
    name: 'newPerson',
    greet: () => {console.log('Hi, ' + this.name)}
}

newPerson.greet()

greet()
