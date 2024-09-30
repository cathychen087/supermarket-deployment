function deleteGood(id) {

    var userChoice = window.confirm("Are you sure?");
    if (userChoice) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/deletGood/' + id, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                console.log(xhr.responseText);
            }
        }
        xhr.send();
        window.location.reload();
    } else {
        // 用户点击了取消按钮
    }
}

function goodInfo(id) {
    window.location.href = '/goodInfo/' + id
}


function updateInfo(id) {
    window.location.href = '/updateInfo/' + id
}


function update(id) {
    var name = document.getElementById('name').value;
    var price = document.getElementById('price').value;
    var stock = document.getElementById('stock').value;
    var place = document.getElementById('place').value;
    var store_time = document.getElementById('store_time').value;
    var expire_time = document.getElementById('expire_time').value;
    fetch('/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            good_id: id,
            name: name,
            price: price,
            stock: stock,
            place: place,
            store_time: store_time,
            expire_time: expire_time
        })
    })
        .then(response => response.json())
        .then(window.location.href = '/')
        .catch((error) => {
            console.error('Error:', error);
        });

}
function add() {
    window.location.href = '/addGood'
}
function addData() {
    var name = document.getElementById('name').value;
    var price = document.getElementById('price').value;
    var stock = document.getElementById('stock').value;
    var place = document.getElementById('place').value;
    var store_time = document.getElementById('store_time').value;
    var expire_time = document.getElementById('expire_time').value;
    fetch('/addGoodData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            price: price,
            stock: stock,
            place: place,
            store_time: store_time,
            expire_time: expire_time
        })
    })
        .then(response => response.json())
        .then(window.location.href = '/')
        .catch((error) => {
            console.error('Error:', error);
        });

}

function logInfo(){
    window.location.href = '/log'
}
