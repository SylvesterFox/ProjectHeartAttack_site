const mb = document.querySelector('#burger_btn');
const menu = document.querySelector('.burger__nav');

mb.addEventListener('click', function(e) {
    e.preventDefault();
    menu.classList.toggle("active");
})

