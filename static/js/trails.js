'use strict';
const stateForm = document.querySelector('#state_form');
    function showParks(evt){
        evt.preventDefault();
        const state=document.querySelector('#state_name').value;
        fetch('/parks.json')
        .then(response => response.json())
        .then(jsonData => {
            // console.log((jsonData[state]));
            // console.log(typeof(jsonData[state]));
            for (const i in jsonData[state]) {
                
                document.querySelector('#park-container').insertAdjacentHTML('beforeend', `<li>${jsonData[state][i]}</li>`);
            }            
                                         
        });
    }
    stateForm.addEventListener('submit', showParks)

