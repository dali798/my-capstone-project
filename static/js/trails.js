'use strict';
const stateForm = document.querySelector('#state_form');
    function showParks(evt){
        evt.preventDefault();
        const state=document.querySelector('#state_name').value;
        
        const parks = document.querySelectorAll('li');
        for (const park of parks) {
                park.remove();
        }

        fetch('/parks.json')
        .then(response => response.json())
        .then(jsonData => {
            if (state === 'all') {
                for (const arr of Object.values(jsonData)){  
                    for (const idx in arr) {
                        
                        document.querySelector('#park-container-2').insertAdjacentHTML(
                        'beforeend', `<li><a href="/parks/${arr[idx]}">${arr[idx]}</a></li>`);
                    }            
                }
            }else{
                for (const i in jsonData[state]) {
                    document.querySelector('#park-container-2').insertAdjacentHTML(
                    'beforeend', `<li><a href="/parks/${jsonData[state][i]}">${jsonData[state][i]}</a></li>`);
                }
            } 
                                                          
        });

    }
    stateForm.addEventListener('submit', showParks)

