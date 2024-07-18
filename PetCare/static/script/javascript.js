let pet1s = document.getElementById('pet1');
let pet2s = document.getElementById('pet2');
let pets = document.getElementById('pet');

pet1s.addEventListener('click',()=>{
    pets.style.backgroundImage="url('/static/images/img2.jpeg')";
})

pet2s.addEventListener('click',()=>{
    pets.style.backgroundImage="url('/static/images/img.jpeg')";
})