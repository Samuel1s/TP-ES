 document.addEventListener('DOMContentLoaded', function() {
    let controls = document.getElementById('magnifier-control').getElementsByTagName('p');

    for (let i = 0; i < controls.length; i++) {
        controls[i].onclick = function(event) {
            for (let j = 0; j < controls.length; j++) {
                if (controls[j].classList.contains('selected')) {
                    controls[j].classList.remove('selected');
                }
            }

            event.target.classList.add('selected');

            if (event.target.id == 'magnifier-mode1') {
                document.getElementById('magnifier').classList.remove('mode2');
                document.getElementById('magnifier').classList.add('mode1');

            } else {
                document.getElementById('magnifier').classList.remove('mode1');
                document.getElementById('magnifier').classList.add('mode2');
            }
        };
    }
})