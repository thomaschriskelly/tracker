document.addEventListener("DOMContentLoaded",function(){
    let deleteButtons = document.getElementsByClassName('delete');
    let headers = {"X-CSRFToken": csrfToken};
    let fetchOptions = {method: 'DELETE', credentials: 'same-origin', headers: headers};
    for ( let btn of deleteButtons ) {
        btn.onclick = function() {
            fetch(btn.dataset.url, fetchOptions)
            .then(res => {
                console.log(res);
                btn.parentNode.remove()
            })
            .catch(err => console.log(err));
        };
    }

    document.getElementById('filter').onclick = function(){
        let startDate = new Date(document.getElementById('startDate').value);
        let endDate = new Date(document.getElementById('endDate').value);
        if (isNaN(startDate.getTime()) || isNaN(endDate.getTime())){
            alert('Invalid date: ' + document.getElementById('startDate').value);
            return;
        }
        let locationRows = document.getElementsByClassName('locationRow');
        for ( let row of locationRows ){
            let rowDateTime = new Date(row.dataset.datetime);
            if (rowDateTime < startDate || rowDateTime > endDate){
                row.style.display='none';
            } else {
                row.style.display='table-row';
            }
        }
    };
});
