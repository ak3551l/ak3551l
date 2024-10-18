const  heading = document.querySelector('.hello');
heading.innerText = 'hello Mehul';

const allListItems = document.querySelectorAll('ul li');

for(let i=0; i<allListItems.length; i++) {
    const listItem = allListItems[i];
    listItem.innerText = 'YOOOOOO';
}
console.log(allListItems);
