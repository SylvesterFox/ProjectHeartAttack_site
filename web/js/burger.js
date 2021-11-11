const mb = document.querySelector('#burger_btn');
const menu = document.querySelector('.burger__nav');

mb.addEventListener('mouseover', function () {
    menu.classList.toggle("active")
})

