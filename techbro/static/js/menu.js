let navitems = document.querySelector('.navitem');
let fabars = document.querySelector('.fa-user');


fabars.addEventListener('click', ()=>{
    navitems.style.maxHeight=='0px'
    if(navitems.style.maxHeight=='0px'){
        navitems.style.maxHeight ='80rem'
    }else{
        navitems.style.maxHeight ='0px'
    }
});

let deleteall = document.querySelector('.deleteall');
let deleteall1  = document.querySelector('.deleteall1');

deleteall1.addEventListener('click', ()=>{
    deleteall.classList.toggle('display')
    }
    )

